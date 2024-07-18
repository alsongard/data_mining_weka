# Political Data Analysis

## Description
Analyze the political_data.csv file to identify patterns that can be leveraged to influence public opinion in favor of a political candidate during an election campaign.


## Features
### Data attributes 
These refers to the data attributes of the political_data.csv file that will be used for analysing and acquiring insights from the data.

| field name | description |
| ---------- | ---------- |
| _unit_id   | unique id for the message|
| _trusted_judgments | number of trusted humans judgements that were entered for the message. Integer value 1 - 3|
| _last_judgement_at | final judgement |
| audience | national or constituency |
| bias  | neutral or partisan|
| bias:confidence | measure of confidence in bias judgement (float value : 0.5 - 1)
| message | aim of message(attack, policy, support, personal, other, media, information, constituency) |
| message:confidence | measure of confidence in message judgement : float value(0.5 -1) |
| bioid | Unique id for politician | 
| source | which platform message was collected |
| text | text message |


#### Elements to be used