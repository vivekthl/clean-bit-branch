# import the installed Jira library
from jira import JIRA
import json
import argparse
import os
import shutil


def trim(ticketName):
    myList = ticketName.split("_");
    return myList[0];

def getClosedTicketList(ticketList, config):
    closedTicketList = [];
    ticketListString = ", " . join(ticketList);

    jiraOptions = {'server': "https://" + config["domain-name"] + ".atlassian.net"}

    jira = JIRA(options = jiraOptions, 
                basic_auth = (config["email"],
                              config["api-key"] ));


    issues = jira.search_issues("key in (" + ticketListString + ")", fields=[ 'status' ]);

    for issue in issues:
        if str(issue.get_field("status")) == "Closed":
            closedTicketList.append(issue.key);

    return closedTicketList;
    
def deleteTicketDirectory(ticket, path):
    ticketPath = os.path.join(path, ticket);
    shutil.rmtree(ticketPath);
    
def deleteTicketsDirectories(ticketList, path):
    print(ticketList);
    for ticket in ticketList:
        deleteTicketDirectory(ticket, path);
    
def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("--path", dest="path", required=True);
    args = parser.parse_args()

    
    configFile = open("config.json", "r");
    config = json.load(configFile);


    ticketList = [];
    for filename in os.listdir(args.path):
        f = os.path.join(args.path, filename)
        if os.path.isdir(f):
            ticketList.append(trim(filename));

    closedTicketList = getClosedTicketList(ticketList, config);

    deleteTicketsDirectories(closedTicketList, args.path);
    
    return;
    
    

if __name__ == '__main__':
    main()
