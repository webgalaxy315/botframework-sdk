# Updating the botframework-channel swagger file

## Abstract
This document describe specific guidelines for updating the [swagger definition file](https://github.com/microsoft/botframework-sdk/blob/master/specs/botframework-protocol/botframework-channel.json) hosted in this repo. These guidelines specify the steps and requirements to maintaining a consistent source of truth that describes the state of connector-features in each SDK codebase. This source of truth is the combination of 2 concepts:
* The botframework-protocol.json file, representing the ideal state that all language SDKs should meet.
* A set of tracking issues per specific SDK that describes each codebase missing diff against the botframework-protocol.json file.

## Requirements
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119) [[1](#References)].

## Terminology

This document will use the following terms as described for the purpose of being succinct:

language repo(s)
> Any (every) of the BF SDK language repositories.

SDK repo
> This repository.

swagger file
> The [json file](https://github.com/microsoft/botframework-sdk/blob/master/specs/botframework-protocol/botframework-channel.json) describing the swagger definition, contained in the SDK repo.

schema update
> An individual change made to the swagger file.

schema label
> A specific standardized github label (same color, same name) with the text 'BF Channel Schema' that MUST exist in every language repo to categorize a PR/issue as related to the process mentioned on this spec.

version label
> A standardized github label (same color, same name) used in the language repos to relate an issue with a certain schema update. The text for the label MUST be the version number in the schema update.

endpoint
> Every json object under the base-level object 'paths' in the swagger file.

schema PR
> A PR containing a schema update.

implementation issue
> The issue opened in a language repo to track the implementation of an endpoint change.

## The process
The steps enumerated bellow MUST be executed every time that a schema PR is submitted.

### 1. Submitting the PR
Every schema PR MUST include **only** the schema update. This means that the only file changed in that PR should be the swagger file.

The schema PR MAY include changes in different parts of the json, it SHOULD NOT be one schema PR per change in json object, but every schema PR including content change (not just format, like indentation) MUST increment the 'version' object inside the 'info' base-level object. (Specific version system is still WIP)

The schema PR MUST be tagged with the schema label.

### 2. Tracking issues

Once a schema PR is approved, one implementation issue MUST be opened for **each endpoint changed** per language repo. The implementation issue MUST reference the schema PR that it comes from, as well as include the schema label and a version label. The implementation issue MAY provide additional context in the body text.

The implementation issue MUST NOT track more than one endpoint changed.

A 'main issue' MAY be opened in the SDK repo to track each language implementation issue of an endpoint change. The main issue MUST contain the schema version in the title. The main issue MUST list every language repo with a link to the corresponding implementation issue and 3 checkboxes, the boxes MUST be the following:
- [ ] PR
- [ ] Merged
- [ ] Irrelevant

### 3. Updating issues

In the case that a language repo receives an implementation issue that deletes, overrides or modifies the same endpoint referenced in another currently open implementation issue, the older issue MUST be closed after updating the first line of its description with '[Irrelevant]' and a link to the new issue.

In the case of having a 'main issue', the criteria for ticking the box under an implementation issue is the following:
* PR: a PR addressing the implementation issue is ready for review.
* Merged: a PR addressing the implementation issue was merged and the issue closed.
* Irrelevant: the implementation was closed with the description '[Irrelevant]'.

## References

1. [RFC 2119](https://tools.ietf.org/html/rfc2119) -- *Key words for use in RFCs to Indicate Requirement Levels*

# Appendix I - Changes

## Merging date - axsuarez@microsoft.com

* Initial draft
