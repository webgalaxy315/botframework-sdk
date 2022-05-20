# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

"""
helpers.py

Performs filtering and other git helpers.

See README.md for details on installing/using.

"""

import copy
import os
from datetime import datetime, timedelta

BOT_SERVICES_LABEL = 'Bot Services'
CUSTOMER_REPORTED_LABEL = 'customer-reported'
SUPPORTABILITY_LABEL = 'supportability'
CUSTOMER_REPLIED_TO_LABEL = 'customer-replied-to'
ADAPTIVE_LABEL = 'adaptive'
BUG_LABEL = 'bug'
EXEMPT_FROM_DAILY_DRI_REPORT_LABEL = 'ExemptFromDailyDRIReport'
MILESTONE_LABELS = [
    '4.5',
    '4.6',
    '4.7',
    '4.8',
    'R7',
    'R8',
    'R9',
    'R10',
    'R11',
    'Backlog',
    'backlog',
    'feature-request',
]

# pylint: disable=missing-docstring, line-too-long

def filter_stale_customer_issues(issue, days_old=60):
    """Filter stale customer issues.
    Return True if it should filter the issue.
    """
    if filter_milestone_label(issue):
        return True
    return not issue.created_at + timedelta(days=days_old) < datetime.now()

def last_touched_by_microsoft(issue, microsoft_members) -> bool:
    comments_paged = issue.get_comments()
    comment = [msg for msg in comments_paged][-1]
    assert comment
    return comment.user.login.strip().lower() in microsoft_members

def get_msorg_members(github, refresh_in_days=5):
    """Get members of the Microsoft github organization.
    This is cached in the `members.txt` file.
    If it gets stale (over `refresh_in_days` old), then refresh it.
    """

    # See if we need to refresh the cache
    members_fname = './members-do-not-check-in.txt'

    member_updated = datetime.fromtimestamp(os.path.getmtime(members_fname))\
        if os.path.exists(members_fname) else datetime.min
    if datetime.now() - timedelta(days=refresh_in_days) > member_updated:
        print('Your members cache is out of date.  Refreshing.. (Could take several minutes)')
        ms_org = github.get_organization('microsoft')
        members = ms_org.get_members()
        with open(members_fname, 'w') as member_file:
            for member in members:
                member_file.write(f'{member.login}\n')
    with open(members_fname, 'r') as member_file:
        members = member_file.readlines()
    return [line.strip().lower() for line in members]

def filter_azure(repo, issue):
    if repo.lower() == 'azure/azure-cli':
        for label in issue.labels:
            if label.name == 'Bot Service':
                return False
        return True
    return False

def strfdelta(tdelta, fmt):
    """Utility function.  Formats a `timedelta` into human readable string."""
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

def add_last_comment(issue, stale_days=10):
    """Takes an issue, adds the last comment time.
    Filters items, where the last comment is not at least stale_days old.
    Returns a copy of the issue.
    """
    comments_paged = issue.get_comments()
    if comments_paged.totalCount == 0:
        return None
    last_comment = ([msg for msg in comments_paged] or [None])[-1]
    assert last_comment
    if last_comment.created_at > (datetime.utcnow() - timedelta(days=stale_days)):
        # Filter items.
        return None
    result = copy.copy(issue)
    result.last_comment = last_comment.created_at
    return result

def filter_bot_service_label(issue):
    return any(label.name == BOT_SERVICES_LABEL for label in issue.labels)

def filter_customer_reported_label(issue):
    return any(label.name == CUSTOMER_REPORTED_LABEL for label in issue.labels)

def filter_customer_replied_label(issue):
    return any(label.name == CUSTOMER_REPLIED_TO_LABEL for label in issue.labels)

def filter_adaptive_label(issue):
    return any(label.name == ADAPTIVE_LABEL for label in issue.labels)

def filter_exempt_from_dri_label(issue):
    return any(label.name == EXEMPT_FROM_DAILY_DRI_REPORT_LABEL for label in issue.labels)

def filter_milestone_label(issue):
    if any(label.name in MILESTONE_LABELS or label.name == BUG_LABEL for label in issue.labels):
         return True
    elif issue.milestone:
         return True
    else:
         return False
