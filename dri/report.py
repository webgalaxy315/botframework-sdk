# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
report.py

Generates report on Bot Framework issues.

See README.md for details on installing/using.

"""
import os
import sys
from datetime import datetime
from github import Github
from colorama import Fore, Style
from output import print_status, print_issue, print_stale_issue, \
OUTPUT_FILE, FILE_NAME, OutputRepository, OuputIssuesJson, OutputIssue, \
setup_html
from helpers import get_msorg_members, last_touched_by_microsoft, filter_azure, \
filter_bot_service_label, filter_adaptive_label, filter_customer_replied_label, \
filter_customer_reported_label, filter_stale_customer_issues, add_last_comment, \
filter_milestone_label, filter_exempt_from_dri_label


HOW_TO_SET_CREDS = """
To set your Git credentials:
    Go to https://github.com/settings/tokens
    Click on "Generate new token"
     - Give note like "SDK tool"
     - Check the repo (and everything underneath)
     - Copy the token value (and store in safe place).
    On command line:
      Windows: set GIT_PERSONAL_TOKEN=<your token>
      Powershell: $env:GIT_PERSONAL_TOKEN="<your token>" (Note the quotes)
      Linux: export GIT_PERSONAL_TOKEN=<your token>

"""

GIT_PERSONAL_TOKEN = os.getenv('GIT_PERSONAL_TOKEN')

if not GIT_PERSONAL_TOKEN:
    print(Fore.RED + '\nYour GIT CREDENTIALS are not set!!\n' + Style.RESET_ALL)
    print(HOW_TO_SET_CREDS)
    sys.exit(2)

# Github Repos being monitored
REPOS = [
    'BotFramework-DirectLine-DotNet',
    'BotBuilder-V3',
    'BotFramework-sdk',
    'botbuilder-dotnet',
    'botbuilder-js',
    'botbuilder-python',
    'botbuilder-java',
    'botbuilder-samples',
    'botframework-composer',
    'botframework-samples',
    'botframework-solutions',
    'botframework-emulator',
    'botframework-webchat',
    'botbuilder-tools',
    'botframework-directlinejs',
    'botframework-cli',
    # 'azure/azure-cli',
]

# Do not apply user filters to these repos.
BYPASS_USERFILTER_REPOS = [
    'botbuilder-tools',
]

# Github people filtered out (must be lowercase!)
MICROSFT_EMPLOYEES = [
    'automationteamva',
    'awalia13',
    'omega1119',
    'Valentyn-Chornovol',
    'batta32',
    'bill7zz',
    'clearab',
    'gasparacevedozainsouthworks',
    'gasper-az',
    'jonathanfingold',
    'kumar2608',
    'shikhamishra11',
    'washingtonkayaker',
    'yochay', # Not a MSFT employee anymore, but still owner of lots of issues. Adding here until they are cleaned up.
    'vishwacsena', # Not a MSFT employee anymore, but still owner of lots of issues. Adding here until they are cleaned up.
    'ryanlengel',
    'zerryth',
    'stevkan',
    'diberry',
    'anusharavindrar',
    'diegocardozo94',
    'v-madhal',
    'v-kydela',
    'corinagum',
    'mrichardson',
    'mdrichardson',
    'github-actions[bot]',
    'zxyanliu',
]

# When to begin searching for issues.
START_DATE = datetime(2019, 7, 1, 0, 0)

# pylint: disable=line-too-long
def main():
    setup_html()
    print_status('Bot Framework SDK Github Report')
    print_status('===============================')
    g = Github(GIT_PERSONAL_TOKEN)

    # Filter out people associated with Microsoft
    microsoft_members = get_msorg_members(g) + MICROSFT_EMPLOYEES

    # Output for UI
    OUTPUT = OuputIssuesJson()

    for repo in REPOS:
        repo_name = repo if '/' in repo else f'microsoft/{repo}'
        repo = g.get_repo(repo_name)

        # Output for UI
        repository_output_element = OutputRepository(repo_name)
        OUTPUT.repositories.append(repository_output_element)

        # Set state='closed' to find closed issues that weren't tagged properly
        # Note: repo.get_issues() underlying library appears to have a bug where
        # `start` and `labels` don't seem to work properly, so we do it manually here.
        # Super inefficient on the wire!
        open_issues = [issue for issue in repo.get_issues(state='open')\
            if issue.created_at >= START_DATE and not filter_azure(repo_name, issue)]
        print_status(f'Repo: {repo.full_name}:')
        print_status(f'   Total open issues after {START_DATE} : {len(open_issues)}', 'tab1')

        # Filter out adaptive issues
        open_issues = [issue for issue in open_issues if not filter_adaptive_label(issue) and not filter_exempt_from_dri_label(issue)]

        user_filtered = True
        if repo.name in BYPASS_USERFILTER_REPOS:
            user_filtered_issues = [issue for issue in open_issues if not issue.pull_request]
            user_filtered = False
        else:
            user_filtered_issues = [issue for issue in open_issues if (not issue.user.login.strip().lower() in \
                microsoft_members and not issue.pull_request)]

        if repo_name.lower() != 'azure/azure-cli':
            no_bs_cr_label = [issue for issue in user_filtered_issues if not filter_bot_service_label(issue) or \
                not filter_customer_reported_label(issue)]

            if no_bs_cr_label:
                print_status(f'   No "Bot Services/Customer Reported": Count: {len(no_bs_cr_label)}', 'tab1')
                for issue in no_bs_cr_label:
                    if user_filtered or not filter_milestone_label(issue):
                        print_issue(issue)
                        repository_output_element.issues.append(OutputIssue("no_bot_services", issue))

            no_crt_label = [issue for issue in user_filtered_issues if not filter_customer_replied_label(issue)]
            if no_crt_label:
                print_status(f'   No "Customer Replied": Count: {len(no_crt_label)}', 'tab1')
                for issue in no_crt_label:
                    if user_filtered in microsoft_members or not filter_milestone_label(issue):
                        print_issue(issue)
                        repository_output_element.issues.append(OutputIssue("no_customer_reply", issue))

            # Start looking at stale (untouched with no comments) issues
            stale_days = 10
            stale_customer_issues = [add_last_comment(issue, stale_days) \
                for issue in user_filtered_issues if not filter_stale_customer_issues(issue, days_old=stale_days)]
            stale_no_nones = [i for i in stale_customer_issues if i]
            stale_descending = sorted(stale_no_nones, key=lambda issue: issue.last_comment, reverse=False)
            if stale_descending:
                print_status(f'   90-day stale : Customer issues not touched in more than {stale_days} days: Count: {len(stale_descending)}', 'tab1')
                print_status(f'      Last touched by {Fore.GREEN}CUSTOMER{Style.RESET_ALL}:', 'tab2')
                for issue in stale_descending:
                    if last_touched_by_microsoft(issue, microsoft_members):
                        print_stale_issue(issue)
                    repository_output_element.issues.append(OutputIssue("last_touch_customer", issue))
                print_status(f'      Last touched by {Fore.GREEN}MICROSOFT{Style.RESET_ALL}:', 'tab1')
                for issue in stale_descending:
                    if not last_touched_by_microsoft(issue, microsoft_members):
                        print_stale_issue(issue)
                    repository_output_element.issues.append(OutputIssue("last_touch_microsoft", issue))
        else:
            # azure/azure-cli just print active issues.
            for issue in user_filtered_issues:
                print_issue(issue)
                repository_output_element.issues.append(OutputIssue("azure_cli", issue))

    # Write JSON output for UI
    # OUTPUT.write_output()
    OUTPUT_FILE.write("</body></html>")
    OUTPUT_FILE.close()

    if sys.platform == 'win32':
        os.system('start "" "' + FILE_NAME + '"')
    else:
        os.system('open ' + FILE_NAME)


if __name__ == "__main__":
    main()
