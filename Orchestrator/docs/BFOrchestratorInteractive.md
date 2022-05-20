
# Interactive

[BF Orchestrator CLI][1] has an "interactive" command which enables a user to
dynamically interact with an Orchestrator base language model (see examples in [Start an interactive session without a training set](#start-an-interactive-session-without-a-training-set)) and
improve the accuracy of an existing language model (see examples in [Start an interactive session with a training set](#start-an-interactive-session-with-a-training-set)) through some CLI commandlets.

During an interactive session, the command loads an Orchestrator base model
into memory and manage several input cache variables that can be used by
ensuing commandlets for maintaining the base model's example set. These variables include:

- **"current" utterance**       -- A cache for storing an utterance that can be used by several commandlets
                              for interacting with an Orchestrator model.
- **"current" intent labels**   -- A cache for storing an array of intent labels that can be used by several
                              commandlet for interacting with an Orchestrator model.
- **"new" intent labels**       -- Another cache for storing an array of intent labels, which were mainly
                              used for changing an utterance's intent labels within an Orchestrator model.

## Scenarios

### Start an interactive session without a training set

An Orchestrator user can launch the interactive command without a training set.
During an session, the user can interactively add utterance examples, revise them, remove them,
validate and create an evaluation report, etc..

#### Argument setup

Below is a command snippet for a user to start the interactive command with two arguments:

    - "--model"     -- folder pointing to an Orchestrator base model
    - "--out"       -- out folder for validation evaluation reports.

```
> set ORCHESTRATOR_MODEL=<Orchestrator base model folder>
> set EVALUATING_OUTPUT=<Evaluation report output folder>
> bf orchestrator:interactive --out=%EVALUATING_OUTPUT% --model=%ORCHESTRATOR_MODEL%
```

After executing the command snippet, the command enters an interactive session shown below:
```
> "Current" utterance:          ""
> "Current" intent label array: ""
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Cache an utterance

The user can then use the 'u' commandlet to enter an utterance and cache it into the "current" utterance
variable. Below is what happened after a user enters "hi" as a new utterance using the 'u' commandlet.

```
Please enter a commandlet, "h" for help > u
Please enter an utterance > hi
> "Current" utterance:          "hi"
> "Current" intent label array: ""
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Cache an intent label

Then the user can issue the 'i' commandlet to enter a new intent label and cache it into the "current"
intent label variable. Notice that Orchestrator supports an utterance with multiple labels, so the 
intent variable cache is actually an array for holding multiple intent labels associated with
the "current" utterance. 
Below is what happened after a user enter "greeting" as a new intent label using the 'i' commandlet.

```
Please enter a commandlet, "h" for help > i
Please enter a "current" intent label > greeting
> "Current" utterance:          "hi"
> "Current" intent label array: "greeting"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Add example to Orchestrator core

After a user enter "hi" and "greeting" during the interactive session, she/he can add this example to
the Orchestrator core. It will become part of the example set Orchestrator core uses for
predicting the intent for new queries. In a sense, this new example was added to a "training" set
for a supervised machine learning model.
The commandlet for adding a new example is 'a'.

```
Please enter a commandlet, "h" for help > a
> Utterance 'hi' has been added to '[
    "greeting"
]'
> "Current" utterance:          "hi"
> "Current" intent label array: "greeting"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Show statistics of the example set

Once a user has entered a sufficient amount of intent/utterance examples into Orchestrator core,
she/he can then use the 's' commandlet to show some statistics of the example set.

```
Please enter a commandlet, "h" for help > s
> Per-label #examples: {
    "greeting": 1
}
> Total #examples:1
> "Current" utterance:          "hi"
> "Current" intent label array: "greeting"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Add examples to current cached intent label

A user can enter more intent/utterance examples.
Below is what happened if the user enters and added two more utterances ("hello" and "good morning")
for the same "greeting" intents. 

```
Please enter a commandlet, "h" for help > u
Please enter an utterance > hello
> "Current" utterance:          "hello"
> "Current" intent label array: "greeting"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > a
> Utterance 'hello' has been added to '[
    "greeting"
]'
> "Current" utterance:          "hello"
> "Current" intent label array: "greeting"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > u
Please enter an utterance > good morning
> "Current" utterance:          "good morning"
> "Current" intent label array: "greeting"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > a
> Utterance 'good morning' has been added to '[
    "greeting"
]'
> "Current" utterance:          "good morning"
> "Current" intent label array: "greeting"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Add example for a new intent label

A user can also enter some utterances with different intents.
Below is what happened if a user enters a new utterance "good bye" with 
a new intent "farewell." However the user forgot to clear the current intent labels, so
the "good bye" intent is actually associated with two intents ("greeting,farewell").
Even though this is not completely wrong semantically, but a user can always
clear the intent variable cache (with the 'ci' commandlet). Remember that the utterance and intents have
not been added to Orchestrator core yet.

```
Please enter a commandlet, "h" for help > u
Please enter an utterance > good bye
> "Current" utterance:          "good bye"
> "Current" intent label array: "greeting"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > i
Please enter a "current" intent label > farewell
> "Current" utterance:          "good bye"
> "Current" intent label array: "greeting,farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Clear intent label cache

The commandlet to clear the intent label cache is 'ci'.
Below is what happened if the user clear the intent label variable cache.
Similarly, the utterance variable cache can be cleared by the 'cu' commandlet.

```
Please enter a commandlet, "h" for help > ci
> "Current" utterance:          "good bye"
> "Current" intent label array: ""
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

The user can then reenter the "farewell" intent into the cache and add it to Orchestrator core:
```
Please enter a commandlet, "h" for help > i
Please enter a "current" intent label > farewell
> "Current" utterance:          "good bye"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > a
> Utterance 'good bye' has been added to '[
    "farewell"
]'
> "Current" utterance:          "good bye"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

After a while, a user can re-issue the 's' commandlet and see the label utterance tabulation:
From the session below, we can see that there are three utterances for the "greeting" intent,
and one for the "farewell" intent.

```
Please enter a commandlet, "h" for help > s
> Per-label #examples: {
    "greeting": 3,
    "farewell": 1
}
> Total #examples:4
> "Current" utterance:          "good bye"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Make prediction

After there are some intent/utterance entered to Orchestrator core, the user can use
Orchestrator core to make some prediction.
Below is what happened if "bye" is entered as the "Current" utterance and use the 'p'
commandlet for an prediction. Orchestrator core responded with a prediction
of the "farewell" intent, a high score of 0.977, and the closest example within the 
"farewell" intent, "good bye".
On the other hand, the "greeting" intent was predicted with a score of 0.691 and
the closest example was "good morning."

```
Please enter an utterance > bye
> "Current" utterance:          "bye"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > p
> Prediction:
[
    {
        "closest_text": "good bye",
        "score": 0.977452505191936,
        "label": {
            "name": "farewell",
            "label_type": 1,
            "span": {
                "length": 3,
                "offset": 0
            }
        }
    },
    {
        "closest_text": "good morning",
        "score": 0.6907451700060104,
        "label": {
            "name": "greeting",
            "label_type": 1,
            "span": {
                "length": 3,
                "offset": 0
            }
        }
    }
]
> "Current" utterance:          "bye"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Hints on new intent label needed

The same utterance, intent, add, predict commandlets can be repeated for a user
to build a sizeable example set within Orchestrator core.
A user try out some new utterance, such as "wake me up at 10AM" and he/she can
see the prediction based on the two existing intent labels.
As we can see for the prediction, the prediction scores are fairly low, 0.322 and 0.275.
The low scores indicate that this new utterance may need a new intent label.

```
Please enter an utterance > wake me up at 10AM
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > p
> Prediction:
[
    {
        "closest_text": "good morning",
        "score": 0.322484918357831,
        "label": {
            "name": "greeting",
            "label_type": 1,
            "span": {
                "length": 18,
                "offset": 0
            }
        }
    },
    {
        "closest_text": "good bye",
        "score": 0.2750571664975262,
        "label": {
            "name": "farewell",
            "label_type": 1,
            "span": {
                "length": 18,
                "offset": 0
            }
        }
    }
]
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

Below is what happened if the user enter a new intent label and add the
"wake me up at 10AM" utterances to Ochestrator core.

```
Please enter a commandlet, "h" for help > ci
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: ""
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > i
Please enter a "current" intent label > alarm
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "alarm"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > a
> Utterance 'wake me up at 10AM' has been added to '[
    "alarm"
]'
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "alarm"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

As we can see from issuing the 's' commandlet, now we have one more intents.

```
Please enter a commandlet, "h" for help > s
> Per-label #examples: {
    "greeting": 3,
    "farewell": 1,
    "alarm": 1
}
> Total #examples:5
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "alarm"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Evaluate the example set

After a while, the user can use the 'v' commandlet to evaluate the example set.
Below is what happened after issuing the 'v' commandlet.
The user can open the evaluation report file and review the progress thus far.
Since there are very few examples per intent, and the valuation is done in
leave-one-out cross validation (LOOCV), so the report does not look good.

```
Please enter a commandlet, "h" for help > v
> Leave-one-out cross validation is done and reports generated in 'experiment_evaluating_PrebuildDomain\orchestrator_predicting_set_summary.html'
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "alarm"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Remove utterance

However, if the user feels that the "wake me up at 10AM" is not what this chatbot is concerned with,
she/he can remove the utterance using the 'r' commandlet. The 'r' commandlet call Orchestrator core
to remove the intent and utterance example currently cached.
On the other hand, the user can reference the evaluation report and pick out the utterance
example and cache it into the "current" variables.
Below is what happened that the user issue the 'vm' (validation/misclassified) commandlet and
enter an index '2' for the No. 2 utterance and put it and its intent to the "Current" cache.
Similarly a user can issue the 'va' (validation/ambiguous), 'vl' (validation/low-confidence), and
the 'vd' (validation/duplicates) commands to pick up the utterance and intent examples and cache them
into the variables.

```
Please enter a commandlet, "h" for help > vm
Please enter an index from the Misclassified report > 2
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "alarm"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

Below is what happened after issuing the 'r' commandlet to remove the "wake me up at 10AM"
utterance. Since there is only one utterance for the "alarm" intent, the whole intent is
eliminated. However, a user can simply issue the 'rl' commandlet to eliminate an intent label
with all of its utterances.
Now there are two intent left in the Orchestrator core.
```
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "alarm"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > r
> Utterance 'wake me up at 10AM' has been removed from '[
    "alarm"
]'
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "alarm"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > s
> Per-label #examples: {
    "greeting": 3,
    "farewell": 1
}
> Total #examples:4
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "alarm"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Detailed configuration information

For more detailed configuration information for Orchestrator, a user can issue the 'd' commandlet.
Below is what happened after a user issue the 'd' commandlet, where
there are several threshold used for the 'v' commandlet during creating an evaluation report.

```
Please enter a commandlet, "h" for help > d
> Ambiguous closeness:           0.2
> Low-confidence closeness:      0.5
> Multi-label threshold:         1
> Unknown-label threshold:       0.3
> Obfuscation flag:              false
> Orchestrator configuration:    {
    "CDF": "{\"zero\":0.400000,\"unknown\":0.700000,\"one\":1.000000}",
    "EmbedderVersion": 1,
    "Framework": "onnx",
    "Layers": 6,
    "MinRequiredCoreVersion": "1.0.0",
    "ModelFile": "D:\\testsBfCliOrchestrator\\_model\\model_bert_6l\\model.onnx",
    "ModelType": "dte_bert",
    "Name": "pretrained.20200924.microsoft.dte.00.06.en.onnx",
    "Publisher": "Microsoft",
    "Version": "pretrained.20200924.microsoft.dte.00.06.en.onnx",
    "VocabFile": "D:\\testsBfCliOrchestrator\\_model\\model_bert_6l\\vocab.txt",
    "ignore_same_example": true,
    "knn_k": 3,
    "nlr_path": "D:\\testsBfCliOrchestrator\\_model\\model_bert_6l",
    "use_compact_embeddings": true,
    "use_gap": false,
    "use_unknown": true
}
> Current label-index map: {
    "farewell": 0,
    "greeting": 1
}
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "alarm"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

- The "Ambiguous closeness" threshold is currently set to 0.2, which means if an utterance
  is correctly predicted, but there are some other intent with a score close to 80% of the
  ground-truth intent label, then that close utterance will be listed as an "ambiguous" prediction
  in the evaluation report.

- The "Low-confidence" threshold is default to 0.5, which means that if an utterance's ground-truth
  intent label is predicted to have the highest score, but the score is lower than 0.5, then
  this utterance will be listed as "low confidence"

- The "Unknown-label" threshold is default to 0.3, which means that if the highest predicted
  intent score is lower than 0.3, then Orchestrator will simply declare that the intent is unknown.

- A user can use the 'vo' commandlet to set the "obfuscate" flag,
  so that the 'v' commandlet can create an evaluation report with all the intent and utterances obfuscated.
  An obfuscated report only show some metadata of the example set without any intent or utterance
  disclosed, so that the report might be shareable for benchmark and comparison purpose.
  The 'd' commandlet also list some internal information of the base model and settings used by 
  Orchestrator core. These information can be used for debugging purpose.
  These thresholds can be reset using the 'vat', 'vlt', 'vmt' and 'vut' commandlets.

#### Create a new snapshot (.BLU) file

After a user has reached a milestone, she/he can create a new snapshot (.BLU) file using the 'n' command.
In the future, the user can run an interactive session preloaded with this new snapshot file and
keep refining the intent and utterance examples.
Below is what happened after the running the 'n' command and the location of the new snapshot file.

```
Please enter a commandlet, "h" for help > n
> A new snapshot has been saved to 'experiment_evaluating_PrebuildDomain\orchestrator_predicting_snapshot_set.blu'
> "Current" utterance:          "wake me up at 10AM"
> "Current" intent label array: "alarm"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Exit the session

At the end, a user can enter the 'q' commandlet to exit the session.

### Start an interactive session with a training set

Since there is already a .blu snapshot file from the last session, a user can
use the interactive command to continue refining the example set by using the "--in" argument.

#### Argument setup

```
> set ORCHESTRATOR_MODEL=<Orchestrator base model folder>
> set EVALUATING_OUTPUT=<Evaluation report output folder>
> bf orchestrator:interactive --out=%EVALUATING_OUTPUT% --model=%ORCHESTRATOR_MODEL% --in=%EVALUATING_OUTPUT%\orchestrator_predicting_snapshot_set.blu
```

#### Show statistics of the example set

After a new interactive session, the user can issue the 's' commandlet and take a look
of the intent/utterance distribution.

```
> "Current" utterance:          ""
> "Current" intent label array: ""
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > s
> Per-label #examples: {
    "greeting": 3,
    "farewell": 1
}
> Total #examples:4
> "Current" utterance:          ""
> "Current" intent label array: ""
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Make predictions on utterances

The user can try out some more utterances.

```
Please enter a commandlet, "h" for help > u
Please enter an utterance > bye bye
> "Current" utterance:          "bye bye"
> "Current" intent label array: ""
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > p
> Prediction:
[
    {
        "closest_text": "good bye",
        "score": 0.9852574345531401,
        "label": {
            "name": "farewell",
            "label_type": 1,
            "span": {
                "length": 7,
                "offset": 0
            }
        }
    },
    {
        "closest_text": "good morning",
        "score": 0.7110401992969432,
        "label": {
            "name": "greeting",
            "label_type": 1,
            "span": {
                "length": 7,
                "offset": 0
            }
        }
    }
]
> "Current" utterance:          "bye bye"
> "Current" intent label array: ""
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Add examples to existing language model

The predicted intent label was "farewell" with a very high score of 0.985. However,
suppose it's a low score, then the user can improve model
by adding the utterance into the example set.
Below is what happened after the "bye bye" utterance is added.

```
Please enter a commandlet, "h" for help > i
Please enter a "current" intent label > farewell
> "Current" utterance:          "bye bye"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > a
> Utterance 'bye bye' has been added to '[
    "farewell"
]'
> "Current" utterance:          "bye bye"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > s
> Per-label #examples: {
    "greeting": 3,
    "farewell": 2
}
> Total #examples:5
> "Current" utterance:          "bye bye"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

Below is what happened when a user enters a new utterance "good day" and
makes a prediction of it.
As we can see that the prediction scores for the "greeting" and "farewell" intents are both very high and close.
The user then added the "good day" utterance to the "farewell" intent.

```
Please enter a commandlet, "h" for help > u
Please enter an utterance > good day
> "Current" utterance:          "good day"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > p
> Prediction:
[
    {
        "closest_text": "good morning",
        "score": 0.8536692972984349,
        "label": {
            "name": "greeting",
            "label_type": 1,
            "span": {
                "length": 8,
                "offset": 0
            }
        }
    },
    {
        "closest_text": "good bye",
        "score": 0.8114553301042285,
        "label": {
            "name": "farewell",
            "label_type": 1,
            "span": {
                "length": 8,
                "offset": 0
            }
        }
    }
]
> "Current" utterance:          "good day"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > a
> Utterance 'good day' has been added to '[
    "farewell"
]'
> "Current" utterance:          "good day"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > s
> Per-label #examples: {
    "greeting": 3,
    "farewell": 3
}
> Total #examples:6
> "Current" utterance:          "good day"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help >
```

#### Relabel utterances

However, the user may later decide to change the intent for "good day" from "farewell" to "greeting".
She/he can them use the 'ni' commandlet to enter "greeting" into the "New" intent label
cache. After that, the user can issue the 'c' commandlet to change the intent label for "good day".
As we can see below, the label/utterance distribution has changed afterward.
Notice that the user can use the 'cni' commandlet to clear the "New" intent label cache.

```
Please enter a commandlet, "h" for help > s
> Per-label #examples: {
    "greeting": 3,
    "farewell": 3
}
> Total #examples:6
> "Current" utterance:          "good day"
> "Current" intent label array: "farewell"
> "New"     intent label array: ""
Please enter a commandlet, "h" for help > ni
Please enter a "new" intent label > greeting
> "Current" utterance:          "good day"
> "Current" intent label array: "farewell"
> "New"     intent label array: "greeting"
Please enter a commandlet, "h" for help > c
> Utterance 'good day' has been moved from '[
    "farewell"
]' to '[
    "greeting"
]'
> "Current" utterance:          "good day"
> "Current" intent label array: "farewell"
> "New"     intent label array: "greeting"
Please enter a commandlet, "h" for help > s
> Per-label #examples: {
    "greeting": 4,
    "farewell": 2
}
> Total #examples:6
> "Current" utterance:          "good day"
> "Current" intent label array: "farewell"
> "New"     intent label array: "greeting"
Please enter a commandlet, "h" for help >
```

#### Check existence of an utterance in the language model

Also, the user can enter an utterance and see if it's in the Orchestrator Core's example set or not
using the 'f' commandlet.
Below is what happened when a user tries to find out if "good evening" is in the example set of not.

```
Please enter a commandlet, "h" for help > u
Please enter an utterance > good evening
> "Current" utterance:          "good evening"
> "Current" intent label array: "farewell"
> "New"     intent label array: "greeting"
Please enter a commandlet, "h" for help > f
> The "current" utterance 'good evening' is not in the model.
> "Current" utterance:          "good evening"
> "Current" intent label array: "farewell"
> "New"     intent label array: "greeting"
Please enter a commandlet, "h" for help >
```

## List of interactive commandlets
At any time, if a user needs to reference help messages for the many commandlets, he/she can issue
the 'h' command for a brief help page on all the commandlets.
Below is the list of the commandlets that can be issued during a 'interactive' session.

### 'h' - help command
    h   - print the help messages with short description of each command

### 'q' - quit command
    q   - quit

### 'd' - display command
    d   - display the utterance, intent label array input caches, Orchestrator config,
          and the label-index map

### 's' - statistics command
    s   - show label-utterance statistics of the model examples

### 'u' - utterance command
    u   - enter a new utterance and save it as the "current" utterance input

### 'cu' - clear utterance variable command
    cu  - clear the "current" utterance input cache

### 'i' - intent variable command
    i   - enter an intent and add it to the "current" intent label array input
          (can be an index for retrieving a label from the label-index map)

### 'ci' - clear intent variable command
    ci  - clear the "current" intent label array input cache

### 'ni' - new intent command
    ni  - enter an intent and add it to the "new" intent label array input
          (can be an index for retrieving a label from the label-index map)

### 'cni' - clear new intent command
    cni - clear the "new" intent label array input cache

### 'f' - find command
    f   - find the "current" utterance if it is already in the model example set

### 'p' - predict command
    p   - make a prediction on the "current" utterance input

### 'v' - validate command
    v   - validate the model and save analyses (validation report) to
          "experiment_predicting_va\orchestrator_predicting_set_summary.html"

### 'vd' - utterance/labels retrieval command (from the Duplicates section of the validation report)
    vd  - reference a validation Duplicates report
          (previously generated by the "v" command) and enter an index
          for retrieving utterance/intents into "current"

### 'va' - utterance/labels retrieval command (from the Ambiguous section of the validation report)
    va  - reference a validation Ambiguous report
          (previously generated by the "v" command) and enter an index
          for retrieving utterance/intents into "current"

### 'vm' - utterance/labels retrieval command (from the Misclassified section of the validation report)
    vm  - reference a validation Misclassified report and enter an index
          (previously generated by the "v" command)
          for retrieving utterance/intents into "current"

### 'vl' - utterance/labels retrieval command (from the Low Confidence section of the validation report)
    vl  - reference a validation LowConfidence report
          (previously generated by the "v" command) and enter an index
          for retrieving utterance/intents into "current"

### 'vat' - ambiguous threshold command
    vat - enter a new validation-report ambiguous closeness threshold

### 'vlt' - low-confidence threshold command
    vlt - enter a new validation-report low-confidence threshold

### 'vmt' - multi-label threshold command
    vmt - enter a new multi-label threshold

### 'vut' - unknown label threshold command
    vut - enter a new unknown-label threshold

### 'vo' - obfuscate command
    vo  - enter a boolean for obfuscating labels/utterances or not in evaluation reports
          generated by the "v" command'

### 'a' - add command
    a   - add the "current" utterance and intent labels to the model example set

### 'r' - remove command
    r   - remove the "current" utterance and intent labels from the model example set

### 'c' - change command
    c   - remove the "current" utterance's intent labels and then
          add it with the "new" intent labels to the model example set

### 'rl' - remove label command
    rl  - remove the "current" intent labels from the model example set

### 'n' - new snapshot command
    n   - create a new snapshot of model examples and save it to
          "experiment_predicting_va\orchestrator_predicting_training_set.blu"

## References

- [BF Orchestrator CLI](https://aka.ms/bforchestratorcli)

[1]:https://aka.ms/bforchestratorcli	"BF Orchestrator CLI"
