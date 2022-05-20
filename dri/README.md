# Git Stats for Bot Framework

Command line tool to view active/aging issues associated with the Bot Framework Github repos.

Requires Python.

Currently performs the following (for repos managed by the Bot Framework):
- Filters out Microsoft employees or vendors
- Count of  **total issues** after `7/1/1019`.
- Issues that don't contain the **`Bot Services`** label.
- Issues that don't contain the **`customer-reported`** label.
- Issues that don't contain the  **`customer-replied-to`** label.
- Issues that are endanger of not being closed within 90 days.
- Outputs to local console and generates a HTML report.

### Setup

Install dependent package **(note: admin mode may be required.)**

```bash
pip install -r requirements.txt
```
### Set your Git Credentials
This tool uses a personal access token to authenticate with Github.

- Go to https://github.com/settings/tokens
- Click on "Generate new token"
  - Give note like "Bot DRI tool"
  - Check the "`repo`" check box (and all items underneath)
  - Copy the token value (don't worry you can regen if you forget it)
 - On command line:
          Windows: `set GIT_PERSONAL_TOKEN=<your token>`

          Powershell: `$env:GIT_PERSONAL_TOKEN="<your token>"` (Note the quotes)

          Linux: `export GIT_PERSONAL_TOKEN=<your token>`

 - To permanently set into your environment variables in Windows:

          `setx GIT_PERSONAL_TOKEN <your token>`

### Run
```bash
python report.py
```
  >Note: The first time you run, the Microsoft organizations members will be cached on disk.  This will take **several** minutes.

Sample Output:
```bash
PS D:\python\github\botframework-sdk\dri> python report.py
Bot Framework SDK Github Report
===============================
Repo: microsoft/BotFramework-DirectLine-DotNet:
   Total issues after 2019-07-01 00:00:00 : 0
   No "Bot Services": Count: 0
   No "Customer Reported": Count: 0
   No "Customer Replied": Count: 0
   90-day stale : Customer issues older than 60 days: 0
Repo: microsoft/BotFramework-Composer:
   Total issues after 2019-07-01 00:00:00 : 76
   No "Bot Services": Count: 0
   No "Customer Reported": Count: 0
   No "Customer Replied": Count: 0
   90-day stale : Customer issues older than 60 days: 0
...
```


### Care and feeding

To filter out people (ie, consultants) which aren't subject to monitoring, edit the `report.py` and add the github alias (all lowercase) to the `MICROSOFT_EMPLOYEES` list.

To add new milestones labels (issues with milestone labels are filtered out), edit the `helpers.py` file and add the milestone label to `MILESTONE_LABELS` list.

Enjoy!
