# BF Orchestrator Command Usage

[BF Orchestrator Command ][1] is used to manage Orchestrator language understanding assets - retrieve, create, evaluate, and tune Orchestrator models to be used in bot development. Typical use is for intent routing to the appropriate language service, LUIS or QnA Maker for additional language tasks such as entity extraction or answer retrieval. This use was previously enabled by use of the legacy *dispatch* CLI. In addition, intent routing can be used to delegate conversations to a backend bot skill. Entity recognition is on the roadmap as a future capability.

## Primary Scenario

The mainstream bot language recognition development cycle with Orchestrator is generally as follows:

1. Create Intent label / utterance examples file in [.lu format][2]  (will be referred to as the *label file*). 
2. Download base model.
3. Combine the label file .lu from (1) with the base model from (2) to create a .blu file (will be referred to as the *snapshot* file). 
4. Test and refine quality of utterance to intent recognition.
5. Integrate Orchestrator language recognizer in your bot.

## Steps

We will use the primary workflow to illustrate how to use Orchestrator commands for full development cycle.

### 1. Create Intent label / utterance examples file in [.lu format][2]

If you are developing a new language model, simply refer to [Language understanding][8] documentation to author label files. Depending on how you plan to design your bot, you may use a single label file corresponding to a single snapshot file for the entire bot or multiple pairs, each for every adaptive dialog where you plan to use Orchestrator as a recognizer. 

In case of **migration from legacy dispatch**, simply add LUIS app(s) or QnAMaker kb(s) as Orchestrator data sources.  Refer to the Dispatch migration documentation [here][11] for more information.

Example:
```
> bf orchestrator:add -t luis --id <luis-app-id> --endpoint <luis-endpoint> -k <luis-subscription-key> -v <luis-app-version> --routingName l_<luis-app-name>
> bf orchestrator:add -t qna --id <kb-id> -k <qna-subscription-key> --routingName q_<kb-name>
```

### 2. Download base model

Create a new folder, say *models*, and download the default base model using: 

```
bf orchestrator:basemodel:get --out ./models
```

out parameter is optional.  If not specified, base model files will be downloaded to the current working directory.

See also the ```orchestrator:basemodel:list``` command if you wish to download and experiment with different base models.  (see descriptions [here][4] ).

### 3. Combine the label file .lu from (1) with the base model from (2) to create a .blu file

There are two ways to create Orchestrator snapshot file(s), depending on the usage scenarios:

- **To route utterances to LUIS/QnA language services**

  Use ```bf orchestrator:create``` command to combine the base model with the label file(s) to create snapshot file for use by the orchestrator recognizer. If using a single folder, create it prior, say *generated*, and specify it in --out parameter:

  ```
  bf orchestrator:create --model <base model folder> --in <label file/folder> --out <generated folder> --hierarchical
  ```

  The create command generates a single Orchestrator snapshot file as output.  If folder is specified as input, it scans the subfolder hierarchy for .lu/.json/.tsv/.qna files and combine all utterances/labels found into the snapshot file.  
  The *hierarchical* flag creates top level intents in the snapshot file derived from the .lu/.json/.tsv/.qna file names in the input folder.  This is useful to create a routing mechanism for further processing by subsequent skills or language services.
  
  In case of **migration from legacy dispatch**, runs orchestrate:create after orchestrator:add commands from (1).   If LUIS app(s) or QnA Maker kb(s) have been updated, add the **--refresh** flag to orchestrator:create command so latest application models will be downloaded to be used to create Orchestrator snapshot file.
  
  Example:
  
  ```
  > bf orchestrator:create 
  ```
  
  
  
  If you have previously used Dispatch CLI to create LUIS based Dispatch application, you could use .dispatch file (created by Dispatch CLI) as input to orchestrator:create command and skip step (1)  above.
  
  Example:
  
  ```
  > bf orchestrator:create --in c:\LuisDispatchBot.dispatch
  ```
  
  
  
- **To recognize intent from incoming user utterance (entity recognition is TBD)**

  Use ```bf orchestrator:create``` command to combine the base model with the label file(s) to create snapshot file for use by the orchestrator recognizer. If using a single folder, create it prior, say *generated*, and specify it in --out parameter:

  ```
  bf orchestrator:create --model <base model folder> --in <label file/folder> --out <generated folder>
  ```

  

### 4. Test and refine quality of utterance to intent recognition

Create a label .lu file with test data set of utterances. Run the following command to generate report for your language model

```
bf orchestrator:test --in <snapshot file> --model <base model file> --out <report folder> --test <test data file>
```

See also [bf orchestrator test](https://github.com/microsoft/botframework-cli/tree/main/packages/orchestrator#bf-orchestratortest) for full command line options.

See also [Report Interpretation][6] for how to use the report to fine tune your language model. 

You can improve your language model by adding or revising examples directly from [.lu][2] files, or interactively by using ```bf orchestrator:interactive``` command (see also [Interactive Command][7]).

### 5. Integrate Orchestrator language recognizer in your bot

Once satisfied with your language model performance, it is time to integrate the model in your bot by specifying Orchestrator as the recognizer. Depending on the flavor of solution there are several methods to hook up Orchestrator. 

See the specific variations for your solution below.

##### Composer Scenario

It is possible to specify  Orchestrator as a dialog recognizer in [Bot Framework Composer][5].  To use Orchestrator in Composer:

1. Enable Orchestrator feature in Composer's Application Settings.
2. Select Orchestrator in the recognizer dropdown menu.
3. Review, evaluate and adjust examples in language data as you would normally for LUIS / Orchestrator to ensure recognition quality.

See the [School skill navigator](https://github.com/microsoft/BotBuilder-Samples/tree/main/composer-samples/csharp_dotnetcore/projects/OrchestratorSchoolNavigator) bot sample for more. 



##### Non-Adaptive (V4) Scenario

The example [NLP with Orchestrator](https://github.com/microsoft/BotBuilder-Samples/tree/main/experimental/orchestrator/csharp_dotnetcore/01.dispatch-bot#nlp-with-orchestrator) illustrates how to use Orchestrator's recognizer in code using the scenario of migrating from legacy dispatch solution.



##### Declarative Dialog Scenario

The best example of declarative use is by inspecting the assets (.dialog files)  produced by Bot Framework Composer.



## Advanced Command

The advanced language recognition development cycle assumes some level understand of machine learning concepts and interactive iterations over the language example definition and potentially evaluation of different models.

For the advanced scenario please refer to the [Interactive Command][7] page.

## Report Interpretation

A particularly important step in tuning your language model is testing and evaluating your language model performance. Orchestrator command produces detailed report to assist in optimizing the language model.

See [Report Interpretation][6] for more.

## References

- [Orchestrator][1]
- [Language Understanding][3]
- [Composer][5]
- [Natural Language Representation Models][4]
- [Wikipedia: Training, validation, and test sets][9]
- [Machine Learning Mastery][10]



[1]:https://aka.ms/bforchestratorcli	"BF Orchestrator CLI"
[2]:https://docs.microsoft.com/en-us/azure/bot-service/file-format/bot-builder-lu-file-format?view=azure-bot-service-4.0 "LU File Format"
[3]:https://docs.microsoft.com/en-us/composer/concept-language-understanding "Language Understanding"
[4]:https://aka.ms/nlrmodels "Orchestrator Base Models"
[5]:https://docs.microsoft.com/en-us/composer/introduction "Composer"
[6]:https://aka.ms/bforchestratorreport "Orchestrator Report"
[7]:https://aka.ms/bforchestratorinteractive "Orchestrator Interactive Command"
[8]:https://docs.microsoft.com/en-us/composer/concept-language-understanding "Language understanding"
[9]:https://en.wikipedia.org/wiki/Training,_validation,_and_test_sets "ML testing"
[10]:https://machinelearningmastery.com/difference-test-validation-datasets/ "Machine Learning Mastery"
[11]:https://github.com/microsoft/botframework-sdk/blob/main/Orchestrator/docs/DispatchMigrationExample.md "Dispatch Migration"






