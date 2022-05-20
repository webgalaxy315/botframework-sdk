# Multi turn interaction with a skill

> A consumer bot starts a multi turn interaction with a skill (e.g.: book a flight) and handles multiple turns (2 or more) until the skill completes the task.

## Variations

1. The consumer cancels the skill (sends EndOfConversation)
2. The consumer sends parameters to the skill
3. The skill sends a result to the consumer
4. The skill sends an event to the consumer (GetLocation) and the consumer sends an event back to the skill.
5. The skill throws and exception and fails (the consumer gets a 500 error)

## Testing matrix

- Skill: [Travel](../SkillsFunctionalTesting.md#travel-skill)
- Topology: [Simple](../SkillsFunctionalTesting.md#simple)

![Test matrix](../media/Simple.jpg)

## Variables

- Auth context: Public Cloud, Gov Cloud, Sandboxed
- Delivery mode: Normal, ExpectReplies

## Total test cases

96 (not including variations)
