# Skills: Validating skill functionality (DRAFT) <!-- omit in toc -->

## Summary <!-- omit in toc -->

Functional tests aim to ensure skills and skill consumers function correctly across the breadth of the Bot Framework.

### Goals <!-- omit in toc -->

1. Validate existing functionality consistently, identify issues and potential regressions.
2. New functionality can be easily tested, without the need to recreate the complex topologies required when working with skills.
3. The test infrastructure can be used either directly or as a template for support scenarios to repro customer issues.
4. Execute automated functional tests regularly (as part of the CI/CD pipeline, on a regular schedule or triggered manually).
5. Ensure a skill built with any of the languages supported by the SDK will work with any other bot built with a different language SDK.

To support these goals, the testing infrastructure used to validate the functional tests derived from this document must be carefully considered.

## Contents <!-- omit in toc -->

- [Scenarios](#scenarios)
- [Reference](#reference)
  - [Things a skill might want to do](#things-a-skill-might-want-to-do)
  - [Variables](#variables)
  - [Consumer/Skill architecture](#consumerskill-architecture)
    - [Simple](#simple)
    - [Multiple skills](#multiple-skills)
    - [Multiple consumers](#multiple-consumers)
    - [Skill chaining](#skill-chaining)
    - [Complex](#complex)
    - [Circular](#circular)
- [Implementation notes](#implementation-notes)
  - [Consumers](#consumers)
  - [Skills](#skills)
    - [GetWeather skill](#getweather-skill)
    - [Travel skill](#travel-skill)
    - [OAuth skill](#oauth-skill)
    - [Teams skill](#teams-skill)
    - [Proactive Skill](#proactive-skill)
    - [Cards Skill](#cards-skill)
    - [RemindMe Skill](#remindme-skill)
  - [Infrastructure](#infrastructure)
- [Glossary](#glossary)

## Scenarios

This section enumerates the testing scenarios for skills, for each one of them we provide a  high level description of the primary test case, the type of consumers used, the skill (or skills) involved and the [consumer/skill architecture](#consumerskill-architecture) used to deploy the testing components.

The different permutations between consumers, skills and their implementation language are represented using a test matrix.

The variables section lists the set of [variables](#variables) that apply to the test case and  need to be configured for each case in the matrix.

Wherever is relevant, we also include a list of variations that describe small variants in the scenario (e.g.: state of the consumer, state of the skill, error condition, special considerations, etc.).

Given these elements, the number of test cases for each scenario can be calculated by multiplying the number of permutations in the matrix by the number of values for each variable and then multiplied by the number of variations.

The list below provides links to each scenario speacification:

1. [Single turn interaction with a skill](scenarios/SingleTurnInteraction.md)
2. [Multi turn interaction with a skill](scenarios/MultiTurnInteraction.md)
3. [Skill sends a proactive message to the consumer](scenarios/ProactiveMessage.md)
4. [Card actions that generate invokes and message activities](scenarios/CardActionsWithInvokes.md)
5. [A skill can update and delete an adaptive card](scenarios/UpdateDeleteAdaptiveCard.md)
6. [The skill needs to authenticate the user with an OAuthCard](scenarios/AuthWithOAuthCard.md)
7. [The consumer authenticates the user and passes OAuth credentials to the skill using SSO](scenarios/AuthWithSSO.md)
8. [A skill uses team specific APIs](scenarios/TeamsAPI.md)
9. [A skill calls another skill](scenarios/SkillCallsSkill.md)
10. [A skill provides a teams task module](scenarios/TeamsSkillWithTaskModule.md)
11. [A skill receives an attachment](scenarios/SkillReceivesAttachment.md)
12. [Skill proactively starts a conversation with a user](scenarios/SkillStartsConversation.md)
13. [Draft scenarios](scenarios/DraftScenarios.md) (Collention of raw ideas for scenarios that need to be defined in more detail)

## Reference

### Things a skill might want to do

- Perform multi-turn dialogs, with child dialog/prompts
- Send proactive messages
- Receive and respond to invoke Activities
- Send cards and respond to card actions
  - Adaptive Card
    - Action.Submit
    - Action.Execute (AC 2.0)
  - Suggested Actions
  - Non-invoke actions (ImBack)
- Retrieve conversation members
  - Single member
  - All members
  - Paged members
- Update messages
- Delete messages
- Create a new conversation
- Use channel-specific functionality
  - Retrieve list of channels in a team
  - Get team info
- Authentication
  - SSO
  - OAuth prompt
  - OAuth card
  - OAuth input

### Variables

- Activity Handling (applies to both the skill and the consumer)
  - Waterfall
  - Adaptive
  - Prompts
  - Raw activity handling
- Consumer sent the Activity to the skill with "expectReplies"
- Skill is currently active
- Skill is currently inactive
- Some _other_ skill is currently active
- Parent bot is engaged in a _different_ dialog
- Authentication context, the skill and consumer are deployed to the public cloud, gov cloud, or a sandboxed environment.
- Network protocol: the consumer is accessed over straight HTTP (webchat) or Web Sockets (streaming clients)
- BotFramework version for the skill: 4.x or 3.x.
- Bot runtime: Composer bot, PVA or SDK coded bot.
- Channel: Emulator, Teams, DirectLine, DirectLine ASE (App Service Extension)
- Bot programming language: C#, JS, Python or Java.
- Bot Adapter: Skill or consumer use a OOTB adapter or custom channel adapter

### Consumer/Skill architecture

This section describes the most common consumer/skill topologies that can exist. The topologies given below are further complicated based on the variables above, as well as the SDK language of any particular bot (consumer or skill) in the topology.

One of the most important things to keep in mind here is that any bot can act as a stand-alone bot, a consumer, or a skill, and may very well fulfill all three models at different times.

#### Simple

In the simplest case there is a single consumer and a single skill.

```
C -----> S
```

#### Multiple skills

A single consumer with multiple skills.

```
      ----> S1
C --<
      ----> S2
```

#### Multiple consumers

A single skill is consumed by multiple consumers.

```
C1 --\
      ------> S
C2 --/
```

#### Skill chaining

A consumer uses a skill, which in turn consumes another skill.

```
C1 -----> C2/S1 ----> S2
```

#### Complex

Combining multiple skills, multiple consumers, and skill chaining.

```
C1 --\                              ----> S3
      ------> C3/S1 ----> C4/S2 --<
C2 --<              \               ----> S4
      ------> S5     -----> S6
```

#### Circular

A consumer uses a skill, which in turn consumes another skill, which in turn consumes the original consumer as a skill. In practice, this topology should probably be avoided, however nothing directly prevents it from occurring.

```
C1/S1 ----> C2/S2 --
   ^                \----> C3/S3 --
   |                               |
   |------------------------------/

```

## Implementation notes

Based on the scenarios described above we will need to build the following artifacts to implement and run functional tests on skills:

### Consumers

- Composer consumer bot (C# only for now)
- VA consumer bot (C# and TS)
- PVA consumer bot (C#)

### Skills

#### GetWeather skill

Composer, C# no dialogs, JS no dialogs, Python no dialogs.

#### Travel skill

Composer, C# waterfall, JS waterfall, Python waterfall.

#### OAuth skill

C#, JS, Python

#### Teams skill

Teams skill should implement the update and delete functionality from the [Teams conversation bot](https://github.com/microsoft/BotBuilder-Samples/tree/main/samples/csharp_dotnetcore/57.teams-conversation-bot) sample.

C#, JS, Python

#### Proactive Skill

C#, JS, Python 

**Note:** Implement as a refactor of [proactive messages sample](https://github.com/microsoft/BotBuilder-Samples/tree/main/samples/csharp_dotnetcore/16.proactive-messages)

#### Cards Skill

C#, JS, Python

**Note** Implement as a refactor of [This controller](https://fuselabs.visualstudio.com/TeamsIntegrationTesting/_git/TeamsIntegrationTesting?path=%2FDotnetIntegrationBot%2FIntegrationCommandHandler.cs)

#### RemindMe Skill

C#, JS, Python

**Note** Message bot to send message some time later

### Infrastructure

- Proactive service (C#)
- Transcript based test runner (C#)

## Glossary

- **Consumer:** A bot that passes Activities to another bot (a skill) for processing.
- **Skill:** A bot that accepts Activities from another bot (a consumer), and passes Activities to users through that consumer.
- **Active skill:** The consumer is currently forwarding Activities to the skill.
- **Inactive skill:** The consumer is not currently forwarding Activities to the skill.
