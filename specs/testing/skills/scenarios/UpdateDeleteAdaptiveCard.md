# A skill can update and delete an adaptive card

> The skill renders an adaptive card with two buttons and one text field. 
> The text field shows the current number of times the "Update" button has been clicked
> The first button is "Update" which increases the number in the text field by 1
> The second button is "Delete" which deletes the adaptive card  

## Variations

1. **Note** There is probably channel specific behavior that exists here. Need to understand how cards work in various channels
2. **Note** We should also cross reference what kinds of cards work in what channels
 
## Testing matrix

- Skill: [Teams skill](../SkillsFunctionalTesting.md#teams-skill)
- Topology: [Simple](../SkillsFunctionalTesting.md#simple)

![Test matrix](../media/Simple.jpg)

## Variables

- Auth context: Public Cloud, Gov Cloud, Sandboxed
- Delivery mode: Normal, ExpectReplies

## Total test cases

96 (not including variations)
