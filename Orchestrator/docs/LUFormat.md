# LU Format in Orchestrator



Orchestrator Recognizer is used today only for routing intents to subsequent skills or other language services such as to QnAMaker or LUIS based dialog. A key distinction between Orchestrator and LUIS is that Orchestrator does not process entities. Entities specified in LU file are simply ignored by Orchestrator during language processing. This works because Orchestrator only needs to identify the utterance's intent in order to pass it further to the owning processor per above.  Also, because Orchestrator ignores entities, the user may simply copy,  paste, and merge LU contents from child LUIS dialog or a connected skill to the Orchestrator based dispatcher parent dialog.

To learn more about LU file format please refer to the original documentation here: [.lu file format - Bot Service | Microsoft Docs](https://docs.microsoft.com/en-us/azure/bot-service/file-format/bot-builder-lu-file-format?view=azure-bot-service-4.0)

