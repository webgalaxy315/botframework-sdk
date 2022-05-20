
# Bot Framework Labeling Guidelines <!-- omit in toc -->

Labels help us organize and prioritize work. We use the same set of labels across the different sections in a repository, such as issues and pull requests. It is important to keep the labels consistent so that we can maintain a standard workflow. Standardized labels also help us query useful data from repos to collect customer feedback for analysis.

This article describes the naming conventions and categorization guidelines of the labels in the Bot Framework repositories to tag issues and PRs. It also provides guidance on how to use them.

This document includes:

- [Labels naming conventions and format](#labels-naming-conventions-and-format)
  - [Wording](#wording)
  - [Multi-category labels format](#multi-category-labels-format)
  - [Label usage](#label-usage)
  - [Label colors](#label-colors)
- [Label categories](#label-categories)
  - [Status](#status)
  - [Area](#area)
  - [Type](#type)
  - [Priority](#priority)
  - [Community](#community)
  - [Size (proposal)](#size-proposal)
  - [Automation (proposal)](#automation-proposal)
- [DRI labels](#dri-labels)
- [Repo specific labels](#repo-specific-labels)
- [Release labels](#release-labels)

# Labels naming conventions and format

There is no official GitHub documentation as to how we should name the labels. This section provides some basic guidelines and examples, which we follow in this article.  

## Wording

- Keep names clear and concise.
- Keep names short. Use acronyms when necessary and provide a description.
- Always provide a description for a label so user know when to use them.
- Multiple-category labels should use sentence case (i.e.: use `Area: Functional tests` instead of `Area: Functional Tests`).

## Multi-category labels format

In order to be able to parse some labels in reports we use a colon followed by a whitespace (`": "`) to separate the categories and subcategories in a label.

The general format of a multi-category label is:

```bash
Main category: Some subcategory
```

There's no limit to the number of subcategories but it is recommended to avoid creating more than two levels.

## Label usage

Some labels can be applied multiple times to an issue and some others shouldn't. For example, an issue can be labeled as `Area: Adaptive` **and** `Area: Skills` but it should **only** have one priority label `P0` or `P1`. Check the intended usage for each label category in the sections below.

GitHub doesn't provide a way of restricting or validating the labels applied to an issue so this will be a manual check that the person updating the issue should perform.

## Label colors

Labels should use the same colors across repos to improve readability and in most cases, all labels within the same main category should use the same color.

# Label categories

We use labels to sort and describe issues, pull requests, and more. It is a good practice to categorize the issues with comprehensible types so that we can easily identify them for different purposes.

This section describes the main label categories being used in the SDK repos:

| Category | Description | Usage | Example |
|---|---|---|---|
|[Status](#status)|Describes the status of an issue throughout its lifecycle.| Single |`needs-triage`|
|[Area](#area)|Defines a functional area or feature of the product for the issue.| Multiple |`Area: Skills`|
|[Type](#type)|Provides additional information on the issue type.| Single |`bug`|
|[Priority](#priority)|The priority for the issue.| Single |`P0`|
|[Community](#community)|Used to describe community related issues.| Single |`Community: Help wanted`|
|[Size](#size)|Provides an estimate for the level of effort required to resolve the issue.| Single |`Size: M`|
|[Automation](#automation) | Labels used to trigger GitHub actions and workflows.| Single |`Automation: No parity`|
|[DRI](#dri)|This is a special set of labels used for DRI tracking and reporting on issues created by customers.| Multiple |`Bot Service`|

## Status

Use these labels for providing information on the progress of the issue. The status label is used to triage and track issues throughout its lifecycle.

Color: This subcategory uses different colors for each label.

| Name | Description | Color | Example |
|---|---|:-:|:--|
|Draft| The issue definition is still being worked on and it is not ready to start development.<br/>Once the issue is ready the label should be removed or the status changed to `needs-triage` or `backlog`.| ![#ededed](https://via.placeholder.com/15/ededed/000000?text=+) `#ededed` | `draft` |
|New| The issue has just been created and it has not been reviewed by the team. <br/>Once the issue is reviewed the label should be removed or changed to `backlog`, `needs-author-feedback` or just closed.| ![#f7ffa3](https://via.placeholder.com/15/f7ffa3/000000?text=+) `#f7ffa3` | `needs-triage` |
|Needs author information| The issue as described is incomplete or not well understood. It is waiting for further information before it can continue.<br>Keep in mind that the issue author may not always flip the tag back to `needs-team-attention` when it responds so scan the issues periodically to see if the author has responded.| ![#f7ffa3](https://via.placeholder.com/15/f7ffa3/000000?text=+) `#f7ffa3` | `needs-author-feedback` |
|Needs team information| The issue has a comment from the author and needs SDK Team or service team’s attention.| ![#f7ffa3](https://via.placeholder.com/15/f7ffa3/000000?text=+) `#f7ffa3` | `needs-team-attention` |
|Backlog| The issue is out of scope for the current iteration but it will be evaluated in a future release. | ![#fbca04](https://via.placeholder.com/15/fbca04/000000?text=+) `#fbca04` | `backlog` |
|Blocked| Current progress is blocked on something else.<br>Make sure you add a note in the issue history when you apply this tag describing what's blocking it for future reference.| ![#ff8c00](https://via.placeholder.com/15/FF8C00/000000?text=+) `#ff8c00` | `blocked` |
|Stale| The issue hasn't been updated in a long time and will be automatically closed. | ![#ededed](https://via.placeholder.com/15/ededed/000000?text=+) `#ededed` | `stale` |

### Repo specific labels for status <!-- omit in toc -->

Do not create repo specific labels for this category.

## Area

These labels are used to map issues to a feature or functional area in the product. This category informs several reports, the labels in this category should only be created by feature and product owners and documented in the table below.

All the issues assigned to a milestone should have at least one of these labels before they can be worked on.

### Area labels <!-- omit in toc -->

Color: All the labels in this category should use ![#1d76db](https://via.placeholder.com/15/1d76db/000000?text=+) `#1d76db`

| Name | Description | Example |
|---|---|---|
|Adaptive| The issue is related to Adaptive dialogs | `Area: Adaptive` |
|Adaptive Expressions| The issue is related to Adaptive expressions | `Area: Adaptive expressions` |
|AI-LUIS| The issue is related to LUIS | `Area: AI-LUIS` |
|AI-Orchestrator| The issue is related to Orchestrator | `Area: AI-Orchestrator` |
|AI-QnAMaker| THe issue is related to QnA Maker | `Area: AI-QnAMaker` |
|Authentication| The issue is related to authenticating users (SSO, OAuth, etc.) | `Area: Authentication` |
|Engineering| Used to categorize internal issues that are related to improving code quality, refactorings, code cleanup, etc. Normally this issues will be also tagged as `technical-debt` or `team-agility` | `Area: Engineering` |
|Custom Adapters| The issue is related to custom adapters (Twilio, Facebook, etc.) | `Area: Custom adapters` |
|Docs| Documentation issue (missing needs updates, etc.) | `Area: Docs` |
|Functional Tests| The issue is related to end to end tests | `Area: Functional tests` |
|LG| Language generation issues | `Area: LG` |
|Samples| The issue is related to the product samples | `Area: Samples` |
|Schema| The issue is related to schemas (bot schemas, skill manifest, etc.) | `Area: Schema` |
|SDK| General SDK issues that don't clearly map to other areas (e.g.: waterfall dialogs, prompts, middleware, and helper methods).<br/> In general, we use this label when we don't have a clear match to other area.| `Area: SDK` |
|Skills| The issue is related to skills | `Area: Skills` |
|Streaming| Issues related to streaming support | `Area: Streaming` |
|Teams| The issue is related to Teams support | `Area: Teams` |
|Telemetry| Issues related to telemetry support | `Area: Telemetry` |
|Testing Framework| Issues related to the bot testing framework | `Area: Testing framework` |

### Repo specific labels for area <!-- omit in toc -->

It is OK to create repo specific sub categories for area, for example, composer may need `Area: UX design` and BF CLI may need `Area: BF config`.

## Type

Use these labels to describe the type of the issue.

All the issues assigned to a milestone should have one of these labels before they can be worked on.

Color: This subcategory uses different colors for each label.

| Name | Description | Color | Example |
|---|---|:-:|:--|
|Bug| Indicates an unexpected problem or an unintended behavior.| ![#d73a4a](https://via.placeholder.com/15/d73a4a/000000?text=+) `#d73a4a` | `bug` |
|Feature request|  A request for new functionality or an enhancement to an existing one.| ![#8f31ed](https://via.placeholder.com/15/8f31ed/000000?text=+) `#8f31ed` | `feature-request` |
|Parity| The issue describes a gap in parity between two or more platforms.| ![#fbca04](https://via.placeholder.com/15/fbca04/000000?text=+) `#fbca04` | `parity` |
|Technical debt| The issue involves refactoring existing code to make it easier to maintain, follow best practices, improve test coverage, etc.| ![#fbca04](https://via.placeholder.com/15/fbca04/000000?text=+) `#fbca04` | `technical-debt` |
|Team agility| An issue targeted to reduce friction to the SDK's development process.| ![#fbca04](https://via.placeholder.com/15/fbca04/000000?text=+) `#fbca04` | `team-agility` |

### Repo specific labels for type <!-- omit in toc -->

Do not create repo specific labels for this category.

## Priority

Describes the priority of the issue. This label is required for any issue that is in scope for an iteration. High priority issues will be addressed first. 

All the issues assigned to a milestone should have one of these labels before they can be worked on.

Color: This subcategory uses different colors for each label.

| Name | Description | Color | Example |
|---|---|:-:|:--|
|P0| Must Fix.  Release-blocker | ![#ee0701](https://via.placeholder.com/15/ee0701/000000?text=+) `#ee0701` | `P0` |
|P1| Painful if we don't fix, won't block releasing | ![#ff8c00](https://via.placeholder.com/15/FF8C00/000000?text=+) `#ff8c00` | `P1` |
|P2| Nice to have | ![#ffff00](https://via.placeholder.com/15/ffff00/000000?text=+) `#ffff00` | `P2` |

### Repo specific labels for priority <!-- omit in toc -->

Do not create repo specific labels for this category.

## Community

Use these labels to tag issues that involve the community.

Color: All the labels in this category should use ![#874faf](https://via.placeholder.com/15/874faf/000000?text=+) `#874faf`.

| Name | Description | Example |
|---|---|---|
|Help wanted| This is a good issue for a contributor to take on and submit a solution | `Community: Help wanted` |

### Repo specific labels for community <!-- omit in toc -->

Do not create repo specific labels for this category.

## Size (proposal)

**Note:** these labels are experimental and may change

Use these to assign an estimated level of effort to resolve an issue and assist with the estimation process.

Color: All the labels in this category should use ![#91e3ea](https://via.placeholder.com/15/91e3ea/000000?text=+) `#91e3ea`.

| Name | Description | Example |
|---|---|---|
|Small| The issue is simple and well understood, it will take a day or less to complete | `Size: S` |
|Medium| The issue is not very complex and it is well understood, it will take 1 to 3 days to complete | `Size: M` |
|Large| The issue is complex but it is well understood, it will take 4 to 8 days to complete | `Size: L` |
|Extra Large| The issue is very complex or not very well defined, it will take 9 to 14 days or more to complete. In this case, it is probably better to rethink the issue and break it down in smaller tasks | `Size: XL` |

### Repo specific labels for size <!-- omit in toc -->

Do not create repo specific labels for this category.

## Automation (proposal)

**Note:** these labels are experimental and may change

These labels are applied to PRs and used to trigger or disable GitHub workflows.

Color: All the labels in this category should use ![#cccccc](https://via.placeholder.com/15/cccccc/000000?text=+) `#cccccc`.

|Name| Description | Example |
|---|---|:--|
|no parity| PR does not need to be applied to other languages.<br>**Note:** if you don't apply the `No parity` to a dotnet PR, the automation workflow will generate parity issues in Python, JS and Java.  | `Automation: No parity` |
|parity with dotnet| The PR needs to be ported to dotnet. | `Automation: Parity with dotnet` |
|parity with JS| The PR needs to be ported to JS. | `Automation: Parity with JS` |
|parity with Python| The PR needs to be ported to Python. | `Automation: Parity with Python` |
|parity with Java| The PR needs to be ported to Java. | `Automation: Parity with Java` |

### Repo specific labels for Automation <!-- omit in toc -->

It is OK to create repo specific labels for this category to trigger repo specific workflows, just use prefix the label with `Automation:` (e.g.: `Automation: My action`).

# DRI labels

The DRI labels are used to support the Azure issue management process and track desired SLAs.

The DRI labels are used when an issue is opened by someone that is not a contributor of the repo.

DRI labels support reporting outside the bot framework repositories and their names don't always follow the standards described above. They should be applied based on the current DRI guide.

Issues created by anyone in the community that is not a collaborator in the repositories will initially be tagged as `customer-reported`.

Color: This subcategory uses different colors for each label.

| Category | Description  | Color | Labels |
|---|---|:-:|:--|
|Customer issue| Customer reported issues, this label is automatically applied when the issue is created by anyone that is not a collaborator in the repository.<br>**Note:** do not use this label to create an issue on behalf of a customer, ask the customer to post the issue instead so it can be tracked to the source.| ![#c2e0c6](https://via.placeholder.com/15/c2e0c6/000000?text=+) `#c2e0c6` | `customer-reported` |
|Service| Required for internal Azure reporting, indicates that the issue is related to the libraries and services managed by the Conversational AI team.<br>Do not change color.| ![#e99695](https://via.placeholder.com/15/e99695/000000?text=+) `#e99695` | `Bot Service` |
|Type| Indicates what the issue type is.<br>This is a subset of the types defined in the [types category](#type).<br/>Only use `bug`, `question` or `feature-request` for DRI issues.| Multiple | `bug`<br> `question`<br>`feature-request`<br>|
|Status| This is a subset of the statuses defined in the [status category](#status) and indicates who needs to take the next step.<br>- `needs-triage`: issue needs members of SDK Team to triage.<br>- `needs-team-attention`: the issue has a comment from the author and needs SDK Team or service team’s attention.<br>- `needs-author-feedback`: more info from the issue creator is needed to address the issue.|  ![#f7ffa3](https://via.placeholder.com/15/f7ffa3/000000?text=+) `#f7ffa3` | `needs-triage`<br>`needs-team-attention`<br>`needs-author-feedback`|
|customer-replied-to| Indicates that the team has replied to the issue reported by the customer.<br>Do not delete.| ![#2683a5](https://via.placeholder.com/15/2683a5/000000?text=+) `#2683a5` | `customer-replied-to` |
|ExemptFromDailyDRIReport| Use this label to exclude the issue from the DRI report.| ![#bde567](https://via.placeholder.com/15/bde567/000000?text=+) `#bde567` | `ExemptFromDailyDRIReport` |

## Repo specific labels for DRI <!-- omit in toc -->

Do not create repo specific labels for this category.

# Repo specific labels

Some repo owners may need to create custom tags that only apply to a particular platform. This is OK but you must be aware that these tags will be used only in that repo and won't be used in cross repo reporting and tracking.

It is recommended that you try to use one of the labels described in this document before creating new ones. Less is better.

If you create repo specific labels, make sure you document the additions on your repo and reference this article.

# Release labels

We should not use labels to tag releases, we should use GitHub milestones instead. 
