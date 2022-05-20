# Bot Framework SDK Product Pipelines Overview
Pipelines for building and releasing Bot Framework SDK products are found on the [Azure FuseLabs web site](https://fuselabs.visualstudio.com/) in two projects: 
 * The [SDK_v4 project](https://fuselabs.visualstudio.com/SDK_v4/_build?view=folders) is Microsoft internal viewable only. It contains most pipelines.
 * The [SDK_Public project](https://fuselabs.visualstudio.com/SDK_Public/_build?view=folders) is public facing. It contains continuous integration (CI) and pull request (PR) pipelines.

For a list of pipelines see the [Bot Framework SDK Pipelines List](SdkPipelinesList.md) document.

Packages are built and tested using _Build_ pipelines in the [SDK_v4](https://fuselabs.visualstudio.com/SDK_v4/_build?view=folders) and [SDK_Public](https://fuselabs.visualstudio.com/SDK_Public/_build?view=folders) projects.

Packages are published using _Release_ pipelines in the [SDK_v4](https://fuselabs.visualstudio.com/SDK_v4/_release?_a=releases&view=all&path=%5C) and [SDK_Public](https://fuselabs.visualstudio.com/SDK_Public/_release?_a=releases&view=all&path=%5C) projects.

Signing builds run nightly and automatically publish preview versions of packages to [MyGet](https://botbuilder.myget.org/gallery).

## AI

**[AI daily pipelines for DotNet and for JS](https://fuselabs.visualstudio.com/SDK_v4/_build?_a=allDefinitions&path=%5CAI%5C&treeState=XEFJ)** are scheduled to run once a night.

AI does not have continuous integration (CI) or pull request validation (PR) pipelines.

Pipelines for pushing to MyGet, NuGet and npmjs are [here](https://fuselabs.visualstudio.com/SDK_v4/_release?_a=releases&view=all&path=%5CAI).

Source repo: [https://github.com/microsoft/botframework-solutions](https://github.com/microsoft/botframework-solutions)

## CLI

CI builds for CLI are [here](https://fuselabs.visualstudio.com/SDK_Public/_build?definitionScope=%5Ccli).

Pipelines for pushing to MyGet and npmjs are [here](https://fuselabs.visualstudio.com/SDK_Public/_release?_a=releases&view=all&path=%5Ccli).

Source repo: [https://github.com/microsoft/botframework-cli](https://github.com/microsoft/botframework-cli)

## DotNet (C#)

**DotNet continuous integration pull request (CI-PR) pipelines [for Windows](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionId=499&_a=summary)** and **[for Linux](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionId=660&_a=summary)** are triggered when a pull request is created or when changes are merged to the master branch. 
Those builds run unit tests. The Windows pipeline additionally runs API compatibility validations. 

**Functional test pipelines** deploy a test bot to Azure, then run tests against the bot. A [nightly signed build](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionId=739&_a=summary) triggers functional test builds [on a Windows platform](https://fuselabs.visualstudio.com/SDK_v4/_release?_a=releases&view=all&definitionId=88) and [on a Linux platform](https://fuselabs.visualstudio.com/SDK_v4/_release?_a=releases&view=all&definitionId=87). A non-signed [test setup build](https://fuselabs.visualstudio.com/SDK_v4/_build/index?definitionId=740&_a=completed) runs whenever code changes are merged to master, and also nightly. It too triggers functional tests [on a Windows platform](https://fuselabs.visualstudio.com/SDK_v4/_release?_a=releases&view=all&definitionId=91) and [on a Linux platform](https://fuselabs.visualstudio.com/SDK_v4/_release?_a=releases&view=all&definitionId=92).

A **[Nightly signed build](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionId=739&_a=summary)** produces preview versions which are automatically published to MyGet. It can optionally create release versions if queued by hand, which are also automatically pushed to MyGet. Releases may be pushed to Nuget.org by manually queuing [this release pipeline]().

Source repo: [https://github.com/Microsoft/botbuilder-dotnet](https://github.com/Microsoft/botbuilder-dotnet)

## Java

Java has a CI pipeline and a daily pipeline [here](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionScope=%5CJava).

A publishing pipeline for MyGet is [here](https://fuselabs.visualstudio.com/SDK_v4/_release?view=all&path=%5CJava&_a=releases). One for the Maven Central Repository is not yet available.

Source repo: [https://github.com/Microsoft/botbuilder-java](https://github.com/Microsoft/botbuilder-java)

## JS

JS has CI, daily, and functional test pipelines [here](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionScope=%5CJS).

Publishing pipelines for MyGet and npmjs are [here](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionScope=%5CJS).

Source repo: [https://github.com/Microsoft/botbuilder-js](https://github.com/Microsoft/botbuilder-js)

## Python

Python has CI and daily pipelines [here](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionScope=%5CPython).

Publishing pipelines for the [botbuilder-python-daily Artifacts feed](https://fuselabs.visualstudio.com/SDK_v4/_packaging?_a=feed&feed=botbuilder-python-daily) and the Python Package Index are [here](https://fuselabs.visualstudio.com/SDK_v4/_release?view=all&path=%5CPython&_a=releases).

Source repo: [https://github.com/Microsoft/botbuilder-python](https://github.com/Microsoft/botbuilder-python)

## Samples

Daily and CI builds for DotNet, JS, and Python Samples are [here](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionScope=%5CSamples).

Pipelines for pushing to MyGet, NuGet and npmjs are [here](https://fuselabs.visualstudio.com/SDK_v4/_release?_a=releases&view=all&path=%5CSamples).

Source repo: [https://github.com/microsoft/BotBuilder-Samples/tree/master/samples](https://github.com/microsoft/BotBuilder-Samples/tree/master/samples)

## Tools

Daily and CI builds for DotNetand JS Tools are [here](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionScope=%5CTools).

Pipelines for pushing to MyGet, NuGet and npmjs are [here](https://fuselabs.visualstudio.com/SDK_v4/_release?_a=releases&view=all&path=%5CTools).

Source repo: [https://github.com/microsoft/botbuilder-tools](https://github.com/microsoft/botbuilder-tools)

## VSIX

VSIX templates for Visual Studio are built [here](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionScope=%5CVSIX).

Pipelines for pushing to MyGet are [here](https://fuselabs.visualstudio.com/SDK_v4/_release?_a=releases&view=all&path=%5CVSIX).

Source repos: 
<br/>&nbsp;&nbsp;[https://github.com/microsoft/botframework-solutions/tree/master/templates/csharp](https://github.com/microsoft/botframework-solutions/tree/master/templates/csharp)
<br/>&nbsp;&nbsp;[https://github.com/microsoft/BotBuilder-Samples/tree/master/generators/vsix-vs-win/BotBuilderVSIX-V4](https://github.com/microsoft/BotBuilder-Samples/tree/master/generators/vsix-vs-win/BotBuilderVSIX-V4)

## WeChat

Daily and CI builds for WeChat are [here](https://fuselabs.visualstudio.com/SDK_v4/_build?definitionScope=%5CWeChat). Public CI builds are [here](https://fuselabs.visualstudio.com/SDK_Public/_build?definitionScope=%5Cwechat).

Pipelines for pushing to MyGet are [here](https://fuselabs.visualstudio.com/SDK_v4/_release?_a=releases&view=all&path=%5CWeChat).

Source repo: [https://github.com/microsoft/BotFramework-WeChat](https://github.com/microsoft/BotFramework-WeChat)
