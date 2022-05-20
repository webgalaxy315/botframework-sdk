
# Testing bots (DRAFT) <!-- omit in toc -->

# Overview <!-- omit in toc -->

Testing a conversational application is often complex and it involves several different layers. The guidance, samples and tools required to test bots are diverse and scattered in different projects, documents and samples.  

A conversational application is made of of code, cognitive models, one or many target channels and several other external services.

This document describes the different types of tests that can be used in a conversational solution and outlines the requirements that we should address to make easier to test bots throughout their life cycle.

![Bot SDLC](images/bot-service-overview.png)

# Table of Contents <!-- omit in toc -->

- [Tenets](#tenets)
- [Testing scenarios](#testing-scenarios)
- [Roadmap](#roadmap)
- [Test types](#test-types)

# Tenets

1. It should be easy and intuitive to create coded unit tests.
2. It should be possible to write unit tests that don't rely on actual cognitive services calls.
3. It should be possible to validate the language models for a bot using tests.
4. Tests should take a relative short time to run.
5. Product owners should be able to write functional and language tests without having to write code.
6. Tests should be "scriptable" and it should be possible to execute them from the command line, the IDE of choice and/or as part of the Continuous Integration/Continuous Delivery pipelines [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/).
7. Whenever a test fails, it should be easy to understand the cause of the failure and the test output should be clean of stack traces and tech jargon (although those may still be available on demand).
8. It should be possible to run tests throughout the entire bot development life cycle: Build, Test, Deployment and Operations.
9. It should be possible to test bots using different languages and locales.
10. Tests should be measurable and should provide metrics that will help determine if the solution quality is improving or not.  

# Testing scenarios

- For a list of the bot testing scenarios targeted to v4.5 see the DCRs posted under [4.5 Preview](https://github.com/Microsoft/botframework-sdk/milestone/1).
- For a complete list of testing scenarios see [Bot Testing Issues](https://github.com/Microsoft/botframework-sdk/issues?q=is%3Aopen+is%3Aissue+project%3AMicrosoft%2Fbotframework-sdk%2F11).

**Note:** The testing DCRs use the format "As a ***role*** I would like to ***requirement*** so I can ***benefit***".

# Roadmap

Our approach is to enhance our samples, documentation and tools to provide clear guidance on how to test bots. We will also extend the SDK with new features where needed to make things easier.

You can see our roadmap and work in progress stories in the [Bot Testing](https://github.com/Microsoft/botframework-sdk/projects/11?fullscreen=true) project.

The **4.5 Candidates** column enumerates a prioritized list of the scenarios targeted for the 4.5 release.

Note that anything on here is subject to change, and is not a guarantee of shipping.

# Test types

There are several test types involved in bot development and operations and different authors and communities use different terminology and naming to refer to them.

This section describes the types we use for testing bots. It doesn't try to provide a formal definition for each type, it is intended to serve as a broad categorization that we use to classify the different scenarios that we are supporting.

- **Unit Tests**
  
  Are written by developers and normally executed as part of the Continuous Integration build pipeline.
  
  Their main purpose is to ensure that the coded logic for a bot executes as expected.

- **Natural Language Understanding Tests**

    Can be written by developers, NLU engineers or Product owners and can be executed as part of the CI pipeline or when the language model for the bot changes.

    Their main purpose is to ensure that the bot understands what the user is asking and that there are no regressions in the language models when they are extended or modified.

    These tests typically target LUIS and QnAMaker.

- **Language Generation tests**

   They are written by NLU engineers or Product owners and are executed as part of the CI pipeline of the underlying Language Generation files (.lg files) for the bot change.

   Their main goal is to ensure the bot constructs meaningful, variable and grammatically correct responses to the user.

   See [this page](https://github.com/Microsoft/botbuilder-dotnet/tree/ComposableDialog/doc/LanguageGeneration) for an overview of LG files.

- **Functional tests**

    Also called End to End tests, these tests target the entire bot and its dependent services.

    Non-technical audiences should be able to write and execute these type of tests.

- **UI Testing**

    Coded UI tests are used for UI-driven functional automation of bots deployed to different channels.

    These tests use open source frameworks like [Selenium](https://docs.seleniumhq.org/) or [Appium](http://appium.io/) to automate UI execution of the client app and playback pre-created scripts.

    These tests are written by developers in conjuntion with product owners.

- **Load Tests**

    These tests validate that the solution will work under the expected user load. They are typically written by testers and developers and cover end to end scenarios under a variable set of load conditions.

    **Note**: VS 2019 will be the last version of Visual Studio that will provide load testing tools. For customers requiring load testing tools, Microsoft is recommending using alternate load testing tools such as Apache JMeter, Akamai CloudTest, Blazemeter (see [Changes to load test functionality in Visual Studio](https://docs.microsoft.com/en-us/azure/devops/test/load-test/overview?view=azure-devops)).

- **Health checks**

    Helth checks are executed on deployed bots and ensure that all the bot and its related services are working as expected in production.

    These tests can be integrated with operation dashboard and trigger alerts if something in the bot is broken.