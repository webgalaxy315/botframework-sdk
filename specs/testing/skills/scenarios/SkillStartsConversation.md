# Skill proactively starts a conversation with a user

> DRAFT: A user is in a Teams group chat with a bot and some other users. 
> The user says @reminderSkill remind me to finish my status report at 4 PM. 
> The skill schedules a task to fire at 4 PM. 
> At 4 PM, the skill starts 1:1 a conversation (CreateConversation) and sends the reminder to the user.

## Variations

1. The skill creates a conversation (in teams) and starts a 1:1 conversation with a user in the group. Note - the 1:1 conversations created persist, and there is no way to delete them. Repeated calls to createConversation will succeed however, and return the appropriate conversationId that can be re-used.

## Testing matrix

- Skill: [RemindMe](../SkillsFunctionalTesting.md#remindme-skill)
- Topology: [Simple](../SkillsFunctionalTesting.md#simple)

![Test matrix](../media/Simple.jpg)

## Variables

- Auth context: Public Cloud, Gov Cloud, Sandboxed
- Delivery mode: Normal, ExpectReplies

## Total test cases

96 (not including variations)
