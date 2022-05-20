# Microsoft.Bot.Builder.AI.Orchestrator

Embedded recognizer package for detecting and routing user intents. 

## Getting started

To use Orchestrator is an intent router:

1. Install this Orchestrator package.
2. Select it as the dialog recognizer where you want to perform the routing.
3. Author your LU as you would normally do for **intents only**. 
4. Connect your intents to subsequent handlers such as skills, or LUIS dialogs. 

## Notes
* Orchestrator is highly recommended and is the default recognizer when creating multi-bot solutions or when adding a remote skill. 
* You may use Orchestrator for intent detection only as you would for routing or if entity extraction is not required.
* Orchestrator does not process entity declarations or does any entity extraction today.

## See Also
* [Dotnet package sources](https://github.com/microsoft/botbuilder-dotnet/tree/main/libraries/Microsoft.Bot.Builder.AI.Orchestrator)
* [JS package sources](https://github.com/microsoft/botbuilder-js/tree/main/libraries/botbuilder-ai-orchestrator)
* [Orchestrator main documentation](https://aka.ms/bf-orchestrator)
* [Orchestrator in Github](https://github.com/microsoft/botframework-sdk/tree/main/Orchestrator)

## Feedback and issues

If you encounter any issues with this package, or would like to share any feedback please open an Issue in our [GitHub repository](https://github.com/microsoft/botframework-components/issues/new/choose).