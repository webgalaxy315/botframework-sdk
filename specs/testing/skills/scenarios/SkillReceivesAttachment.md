# A skill receives an attachment

> As part of a multi turn conversation a skill is expecting a file that needs to be uploaded consumer bot and then relayed to the skill

## Variations

**Questions**

- Are there any unsupported file types?
- What happens if we upload the same file multiple times
- What happens if we upload a file that's too large
- What if the skill doesn't know what to do with an attachment

## Testing matrix

- Skill: TBD
- Topology: [Simple](../SkillsFunctionalTesting.md#simple)

![Test matrix](../media/Simple.jpg)

## Variables

- Auth context: Public Cloud, Gov Cloud, Sandboxed
- Delivery mode: Normal, ExpectReplies
- Channel: TODO not sure about this yet

## Total test cases

96 (not including variations)
