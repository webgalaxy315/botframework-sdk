---
title:  'Building bots from building blocks'
author: 'clearab'
---

# Building bots from building blocks

The component model for building bots enables developers to build bots with re-usable building blocks (components). This model consists of a configurable [adaptive runtime](#adaptive-runtime), that can be extended by importing [packages](#packages) of functionality or connecting to other bots as [skills](#skills). Getting started [templates](#templates) built on this model will unify the creation experience, and eliminate the "dead-end" that can happen for some existing getting started experiences that lock you in to building a particular type of bot.

**Our goals**:

* Encourage the reuse of bot components – either connecting to a skill or importing in a package.
* Enable the free movement of bots and components across hosting options and editing canvases.
* Use industry/language-standard concepts and tools wherever possible.
* Abstract away platform concepts for developers who do not wish to use them directly.
* Enable provisioning and deployment to the necessary infrastructure based on the components included in a bot.
* Publish a suite of packages, templates, and skills bot developers can use to build their bots from.
* Publish components that demonstrate conversational design best practices.

## Adaptive Runtime

At the core of the component model is the adaptive runtime - an extensible, configurable runtime that is treated as a black box to bot developers and taken as a dependency. The runtime provides extensibility points to add additional functionality by importing packages, connection to skills, or adding your own functionality.

## Packages

Packages are bits of a bot you want to share/import like declarative dialog assets, coded dialogs, custom adapters, middleware or custom actions. They are just packages  - NuGet / npm etc based on the code-language of your bot. You'll use the Bot Framework CLI tool to merge the package's declarative contents with your bot (package management in Composer will handle this for you). They can be made up of any combination of declarative assets (.dialog, .lu, .lg, .qna files) or coded extensions (custom actions, middleware, adapters).

In addition to the packages published by the Bot Framework team, you'll be able to create and share your own packages. We plan to provide tooling to make the entire package management lifecycle as simple as possible, from discovery and inclusion, to creation and publishing. Some examples of packages include:

* Common conversational constructs like greeting, cancel, help, unknown intent.
* Bundles of custom actions for working with an API like MS Graph, Dynamics, the Power Platform or GitHub.
* Vertically aligned solutions containing a combination of custom actions and adaptive assets like human hand-off, or working with your calendar.
* Bundles of custom actions for working with specific types of data or operations, like math functions or working with dates.
* Meta-packages, that just take dependencies on a bunch of other packages to group functionality for simpler management.

## Templates

Getting started templates will be created on top of the component model. They will be built primarily by composing packages - ensuring that no matter which template you start from you'll have the flexibility to grow and develop your bot to meet your needs.

For example, the Conversational Core template will take a dependency on four packages - greeting, help, cancel, and unknown intent. This represents the base set of functionality nearly all conversational bots include. If you were to start from the empty/echo bot template, you could choose to add these packages later - either way you'd get the same set of functionality (without the need to do something like compare code samples and try and stitch them together yourself).

## Skills

Skills are separate bots you connect your bot to in order to process messages for you. The skill manifest establishes a contract other bots can follow - defining messages and events the skill can handle and any data that will be returned when the skill completes its interaction with your user.
