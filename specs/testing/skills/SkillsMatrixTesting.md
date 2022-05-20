# Automated Testing of Skills

Defines the short term goals around the automated testing of skills. 

# Goal

Automate the testing matrix for Bot/Skill interactions. The full testing matrix runs every night. Failures result in emails. 

# Version of the Botbuilder SDK

1. For each test run, the latest *preview* Bot Builder SDK should be consumed from the MyGet.
2. Alternatly, a specific version of the BotBuilder SDK could be specified via an Azure Devops variable. 

# Testing Matrix

## Phase 0, "Crawl"
|        |    |            |        | 
|--------|----|------------|--------|
|        | C# | Javascript | Python | 
| C#     |   1 |2            |3        | 
| JS     | 4   |5            |6       | 
| Python |7    |8            |9        | 

1. C# Bot acting as consumer, calling a C# Skill
2. C# Bot acting as consumer, calling a JS Skill
3. C# Bot acting as consumer, calling a Python Skill
4. JS Bot acting as consumer, calling a C# Skill
5. JS Bot acting as consumer, calling a JS Skill
6. JS Bot acting as consumer, calling a Python Skill
7. Python Bot acting as consumer, calling a C# Skill
8. Python Bot acting as consumer, calling a JS Skill
9. Python Bot acting as consumer, calling a Python Skill

## Phase 1

1. The test matrix runs in the Gov cloud.

Note: Python is not currently supported in Gov Cloud, so that portion of the matrix won't be moved over (yet). 

## Phase 2, "Run"

|                 | C# Net Core 3 | Javascript | Python | C# Net Core 2.1 | v3 Javascript | v3 C# |
|-----------------|---------------|------------|--------|-----------------|---------------|-------|
| C# Net Core 3   |     1         |    2        |  3      |    13             |    14           |  15     |
| JS              |      4         |   5         |   6     |        16         |     17          |    18   |
| Python          |     7          |   8         |   9     |       19          |       20        |    21   |
| C# Net Core 2.1 |      10         |    11        |  12      |      22           |      23         |  24     |

1. [Unchanged] C# Bot acting as consumer, calling a C# Skill
2. [Unchanged] C# Bot acting as consumer, calling a JS Skill
3. [Unchanged] C# Bot acting as consumer, calling a Pyton Skill
4. [Unchanged] JS Bot acting as consumer, calling a C# Skill
5. [Unchanged] JS Bot acting as consumer, calling a JS Skill
6. [Unchanged] JS Bot acting as consumer, calling a Python Skill
7. [Unchanged] Python Bot acting as consumer, calling a C# Skill
8. [Unchanged] Python Bot acting as consumer, calling a JS Skill
9. [Unchanged] Python Bot acting as consumer, calling a Python Skill
10. [New] C# Net Core 2.1 Bot acting as a consumer, calling a C# .Net core 3.1 Skill 
11. [New] C# Net Core 2.1 Bot acting as a consumer, calling a JS Skill 
12. [New] C# Net Core 2.1 Bot acting as a consumer, calling a Python Skill 
13. [New] C# Net Core 3.1 Bot acting as a consumer, calling a .Net Core 2.1 Skill 
14. [New] C# Net Core 3.1 Bot acting as a consumer, calling a v3 JS Skill 
15. [New] C# Net Core 3.1 Bot acting as a consumer, calling a v3 C# Skill
16. [New] JS Bot acting as consumer, calling a C# .Net Core 2.1 Skill
17. [New] JS Bot acting as consumer, calling a v3 JS Skill
18. [New] JS Bot acting as consumer, calling a v3 C# Skill
19. [New] Python Bot acting as consumer, calling a C# Net Core 2.1 Skill
20. [New] Python Bot acting as consumer, calling a v3 JS  Skill
21. [New] Python Bot acting as consumer, calling a v3 C#  Skill
22. [New] C# Net Core 2.1 acting as consumer, calling a C# .NEt Core 2.1 Skill
23. [New] C# Net Core 2.1 acting as consumer, calling a v3 JS Skill
24. [New] C# Net Core 2.1 acting as consumer, calling a v4 C# Skill

# Tests

* **Crawl** The only test run is an Echo + end utterance to trigger an EndOfConversation Activity. The Consumer sends a Message containing a GUID to the skill, and the skill echo that back. The skill then sends end the conversation. 
* **Walk** Scenario for Events and Invoke + InvokeResponse are added. 
* **Run** the test matrix grows to include C# .Net Core 2.1 (as a Skill Host and Skill), and v3 JS (as a Skill) and v3 C# (as as Skill)

# Bots we need
3 Bots (1 in C#, one in JS, one in Python). The Bot picks up "Skill" or "Consumer" from the ENV variables, which are set as part of the bot's deployment. 

The bots that may server as a starting point for development are here:
[C#](https://github.com/microsoft/BotBuilder-Samples/tree/master/samples/csharp_dotnetcore/80.skills-simple-bot-to-bot)
[JS](https://github.com/microsoft/BotBuilder-Samples/tree/master/samples/javascript_nodejs/80.skills-simple-bot-to-bot)
[Python](https://github.com/microsoft/BotBuilder-Samples/tree/master/samples/python/80.skills-simple-bot-to-bot)

OPEN ITEM: Unclear if we should have 3 bots or 6. 

# Repo
All bots are stored in the same git repo. The repo is hosted on Azure Devops, at the following location:
https://github.com/microsoft/BotFramework-FunctionalTests

Note: We are not using GitHub for this, as this repo needs to be public. We may revisit this decision, as it's easier for external vendors to work in a GitHub repo. 

# CI/CD and YAML
Each test case in the matrix has a dedicated YAML file and corresponding build in Azure Devops.

The testing is kicked off each night via a trigger from our nightly CI/CD build of the SDK. 

# Problems to Solve:

1. Picking up the latest SDK version from MyGet. Unclear how best to do this using Azure Devops.
2. How best to kick-off the build? Is there an easy way to kick off the build once each of the C# / JS / Python nightly builds are complete? 
3. How to apply to Gov Datacenter? 
4. Best way to register / manage / deploy the bots? 
5. What Azure Subscription? 
6. Setup/Teardown each night, re-using the AppID + Password? Use Certs? 
7. Which Azure Resource Group?
