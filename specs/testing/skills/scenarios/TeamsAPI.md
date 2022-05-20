# A skill uses team specific APIs

> - Retrieve list of channels in a team
> - Get team info
> - Get members from a non-team-scoped conversation
> - Retrieve the _paged_ list of uses in a group where the group is large enough to necessitate more than one page.

## Variations

- Trying to access Team specific information from a 1:1 or group chat
  - EX: Calling `GetTeamChannels` from a 1:1 chat

## Variables

- Auth context: Public Cloud, Gov Cloud, Sandboxed
- Delivery mode: Normal, ExpectReplies

## Testing matrix

- Skill: [Teams skill](../SkillsFunctionalTesting.md#teams-skill)
- Topology: [Simple](../SkillsFunctionalTesting.md#simple)

![Test matrix](../media/Simple.jpg)

## Total test cases

96 (not including variations)
