# clean-bit-branch
Script to cleanup local branch directories of closed tickets cloned from
remote with branch-name same as ticket.


### How to generate api-token 

* Go to https://id.atlassian.com/manage-profile/security/api-tokens

### How to get email-id

* Go to https://id.atlassian.com/manage-profile/email


### How to use

* Update `config.json`
* Run
```
python3 clean.py --path=<path-to-directory-with-directories-of-branches>
```
