# Proofpoint ITM

Publisher: Splunk Community \
Connector Version: 1.0.1 \
Product Vendor: Proofpoint \
Product Name: ITM \
Minimum Product Version: 6.2.0.355

Proofpoint ITM 4 SOAR - Also know as ObserveIT by Proofpoint, or Proofpoint Insider Threat Management

**TODO**: add support for API call to platform users, get User UUID for use in 'assign user'
**TODO**: check screenshots interface around files<br>
**TODO**: update status / progress movement - nothing around in-progress / close/postivie/negative/beginine yet<br>
**TODO**: get users function defined, but does nothing, should faile, untested, its just a remidner to action

Thanks to **JOHN WANG** of **SPLUNK** - you really made this happen a billion times faster than it would have without you. And it was WAY EASIER for me having you on hand to ask questions of. I bet you are so happy it is done now!<br>
Thanks **ARAVIND** & **ALBERT** & **JOSHUA** for always being online when i just happened to need you<br>

So this app does stuff yea! Well its supposed to<br>

**ACTIONS** as listed in the app... a bucketload of **JSON** is in the get ticket puppy BUT also really cool is the timeline_url that is returned which i generate for you to be able to jump into the timeline of the alert and see whats happening asap<br><br>
There is no check real check for the get files thing, so basically, its really beta, pre-beata, alpha, pre-alpha... anyway go hard or go home right? wait! that doesnt work anymore, every is working from home already... ok - go hard or go to the office! since all we do in the office is socialise and i never get anything more than less than two lunhces, and 50 coffies on a work from office day, this seems right<br><br>

- Added support for oct/stream recognition - use case is download origional email, will expand to support screenshots later<br>
- the timeline_url to the output of get-ticket (need to get the ticket details to calculate the timeline url)<br>
- Added support for assigning owner (need to enhance, currently just a select list of users are pre-configured)<br>
- created oAuth process around token and token use, needs to be made better, we dont reuse token beyond the single call to the app, should at least last the whole playbook run if we call the mapp more than once in a run, but for now...

### Configuration variables

This table lists the configuration variables required to operate Proofpoint ITM. These variables are specified when configuring a ITM asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base_url** | required | string | Base URL / Domain, i.e https://xyz.proofpoint.com |
**api_version** | optional | string | API version: v1 / v2 / v3 |
**client_id** | required | string | Client ID |
**client_secret** | required | password | Client Secret |

### Supported Actions

[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration \
[get email](#action-get-email) - Get an email from the server \
[assign owner](#action-assign-owner) - Update ticket (issue) to be owned by this person \
[get ticket](#action-get-ticket) - Get ticket (issue) information \
[add comment](#action-add-comment) - Add a comment to a ticket \
[get user](#action-get-user) - Get User details \
[set status](#action-set-status) - Set ticket (issue) status

## action: 'test connectivity'

Validate the asset configuration for connectivity using supplied configuration

Type: **test** \
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'get email'

Get an email from the server

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** | optional | Message ID to get | string | `email id` |
**attachments** | optional | Include Attachments | boolean | |
**stream** | optional | Stream Response | boolean | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data | string | | |
action_result.summary | string | | |
action_result.parameter.fqid | string | `email id` | |
action_result.parameter.attachments | string | | |
action_result.parameter.stream | string | | |
action_result.status | string | | success failed |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

## action: 'assign owner'

Update ticket (issue) to be owned by this person

Type: **generic** \
Read only: **False**

Assign Ticket to user as per the UI values in PP ITM Portal.

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** | required | Issue ID | string | |
**assignee_id** | optional | Assign Ticket to this person by ID | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data | string | | |
action_result.summary | string | | |
action_result.parameter.fqid | string | | |
action_result.parameter.assignee_id | string | | |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.data.0.\_status.code | string | | |
action_result.data.0.\_status.status | string | | |
action_result.data.0.annotations.comments.\*.text | string | | |
action_result.data.0.annotations.history.\*.text | string | | |
action_result.data.0.annotations.workflow.state.\* | string | | |
action_result.data.0.indicators.\*.name | string | | |
action_result.data.0.messages.\*.subject | string | | |
action_result.data.0.messages.\*.kind | string | | |
action_result.data.0.messages.\*.recipients.\*.email | string | | |
action_result.data.0.incident.status | string | | |
action_result.data.0.incident.name | string | | |
action_result.data.0.incident.severity | string | | |
action_result.data.0.custom.\* | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

## action: 'get ticket'

Get ticket (issue) information

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** | required | Ticket (Issue) FQID | string | |
**includes** | optional | Includes (Screenshots/---) | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.summary | string | | |
action_result.data.0.\_status.code | string | | it:error:some-error |
action_result.data.0.\_status.status | string | | 400 |
action_result.data.0.\_status.message | string | | Error obtaining data for event '4242cfb7-edc4-47e0-b8a1-aa547562bcba' with name 'Nice Name' |
action_result.data.0.annotations.comments.\*.text | string | | This is a note or comment in PP ITM |
action_result.data.0.annotations.history.\*.text | string | | |
action_result.data.0.annotations.workflow.state.\* | string | | status : incident:status:new |
action_result.data.0.indicators.\*.name | string | | Whatever you configure in PP ITM |
action_result.data.0.messages.\*.subject | string | | Greetings from Nigeria |
action_result.data.0.messages.\*.kind | string | | email |
action_result.data.0.messages.\*.recipients.\*.email | string | | user.name@domain.name.com |
action_result.data.0.incident.status | string | | incident:status:new |
action_result.data.0.incident.name | string | | EMAIL-DLP-PCI |
action_result.data.0.incident.severity | string | | incident:severity:850:critical |
action_result.data.0.custom.\* | string | | Do you think i will have to take this out? |
action_result.parameter.fqid | string | | |
action_result.parameter.includes | string | | |
action_result.status | string | | success failed |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

## action: 'add comment'

Add a comment to a ticket

Type: **generic** \
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** | required | FQID for Alert | string | |
**comment** | required | Comment to add | string | |
**kind** | required | Kind | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data | string | | |
action_result.summary | string | | |
action_result.parameter.fqid | string | | |
action_result.parameter.comment | string | | |
action_result.parameter.kind | string | | |
action_result.status | string | | success failed |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

## action: 'get user'

Get User details

Type: **investigate** \
Read only: **True**

Get a list of all users and their user attributes, or search the system for a single user id by username/string all values are optional.

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** | optional | Username user.name@email.com (also note * is permited... \*@blah.com) | string | |
**status** | optional | User Status (Multi Value CSV eg: active,pending) | string | |
**assignments** | optional | Assignments groups | string | |
**includeinactivepolicies** | optional | IncludeInactivePolicies (use true / false) | string | |
**detailsuserfirstname** | optional | Select by firstName of user. Use * for wildcards | string | |
**detailsuserlastname** | optional | Select by lastName of user. Use * for wildcards | string | |
**includes** | optional | Resource to get extra data like tenant, policy-assignments, etc | string | |
**parentstatuses** | optional | Statuses of parent entity | string | |
**limit** | optional | Max records to return (defaults to 100) | numeric | |
**offset** | optional | Number of records to skip (defaults to 0) | numeric | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data | string | | |
action_result.summary | string | | |
action_result.parameter.username | string | | |
action_result.parameter.status | string | | |
action_result.parameter.assignments | string | | |
action_result.parameter.includes | string | | |
action_result.parameter.parentstatuses | string | | |
action_result.parameter.includeinactivepolicies | boolean | | |
action_result.parameter.limit | numeric | | |
action_result.parameter.detailsuserfirstname | string | | |
action_result.parameter.detailsuserlastname | string | | |
action_result.parameter.offset | numeric | | |
action_result.status | string | | success failed |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

## action: 'set status'

Set ticket (issue) status

Type: **generic** \
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** | required | Ticket (Issue) Key | string | |
**status_id** | required | Status ID | string | |
**status_title** | required | Alias / Status title | string | |
**status_category** | required | Status Category | string | |
**assignee_id** | required | Assignee ID | string | |
**kind** | required | Kind | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data | string | | |
action_result.summary | string | | |
action_result.parameter.fqid | string | | |
action_result.parameter.status_id | string | | |
action_result.parameter.status_title | string | | |
action_result.parameter.status_category | string | | |
action_result.parameter.assignee_id | string | | |
action_result.parameter.kind | string | | |
action_result.status | string | | success failed |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2025 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
