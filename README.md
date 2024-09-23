[comment]: # "Auto-generated SOAR connector documentation"
# Proofpoint ITM

Publisher: Splunk Community  
Connector Version: 1.0.1  
Product Vendor: Proofpoint  
Product Name: ITM  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 6.2.0.355  

Proofpoint ITM 4 SOAR - Also know as ObserveIT by Proofpoint, or Proofpoint Insider Threat Management

# Proofpoint ITM SOAR App

Publisher: Splunk  
Connector Version: 1\.0\.0  
Product Vendor: Proofpoint  
Product Name: ITM  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 6\.2\.0  

Splunk SOAR app that integrates with the Proofpoint ITM. Proofpoint Insider Threat Management (ITM) is a people-centric SaaS solution that helps you protect sensitive data from insider threats and data loss at the endpoint. It combines context across content, behavior and threats to provide you with deep visibility into user activities. Proofpoint ITM helps security teams tackle the challenges of detecting and preventing insider threats. It can streamline their responses to insider-led incidents and provide insights that help prevent further damage.

[comment]: # " File: README.md"
[comment]: # "  Copyright (c) 2019-2023 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""

## Asset Configuration

To start working with such SOAR connector user need to collect **Client ID**, **CLient Secret** and of course Company **base url** and **API version** for API execution.

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a EC2 asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  required  | string | Company hostname for API execution
**client\_id** |  required  | string | Client ID
**client\_secret** |  required  | password | Client Secret
**api\_version** |  required  | string | API version

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using token generation  
[get email](#action-get-email) - Get an email from the server  
[assign owner](#action-assign-owner) - Update ticket (issue) to be owned by this person  
[get ticket](#action-get-ticket) - Get ticket (issue) information  
[add comment](#action-add-comment) - Add a comment to a ticket  
[get user](#action-get-user) - Get User details  
[set status](#action-set-status) - Set ticket (issue) status

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get email'
Get an email from the server 

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** |  required  | Message ID to get | string | 
**attachments** |  required  | Include Attachments | boolean | 
**stream** |  required  | Stream Response | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.fqid | string | 
action\_result\.parameter\.attachments | boolean | 
action\_result\.parameter\.stream | boolean | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'assign owner'
Update ticket (issue) to be owned by this person

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** |  required  | Issue ID | string | 
**assignee\_id** |  required  | Assign Ticket to this person by ID | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.fqid | string | 
action\_result\.parameter\.assignee\_id | string | 
action\_result\.data\.\_status\.code | string | 
action\_result\.data\.\_status\.status | string | 
action\_result\.data\.annotations\.comments\.\*\.text | string | 
action\_result\.data\.annotations\.history\.\*\.text | string | 
action\_result\.data\.annotations\.workflow\.state\.\* | string | 
action\_result\.data\.indicators\.\*\.name | string | 
action\_result\.data\.messages\.\*\.subject | string | 
action\_result\.data\.messages\.\*\.kind | string | 
action\_result\.data\.messages\.\*\.recipients\.\*\.email | string | 
action\_result\.data\.incident\.status | string | 
action\_result\.data\.incident\.name | string | 
action\_result\.data\.incident\.severity | string | 
action\_result\.data\.custom\.\* | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get ticket'
Get ticket (issue) information

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** |  required  | Ticket (Issue) FQID | string | 
**includes** |  optional  | Includes (Screenshots/---) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.fqid | string | 
action\_result\.parameter\.includes | string | 
action\_result\.data\.\_status\.code | string | 
action\_result\.data\.\_status\.status | string | 
action\_result\.data\.\_status\.message | string | 
action\_result\.data\.annotations\.comments\.\*\.text | string | 
action\_result\.data\.annotations\.history\.\*\.text | string | 
action\_result\.data\.annotations\.workflow\.state\.\* | string | 
action\_result\.data\.indicators\.\*\.name | string | 
action\_result\.data\.messages\.\*\.subject | string | 
action\_result\.data\.messages\.\*\.kind | string | 
action\_result\.data\.messages\.\*\.recipients\.\*\.email | string | 
action\_result\.data\.incident\.status | string | 
action\_result\.data\.incident\.name | string | 
action\_result\.data\.incident\.severity | string | 
action\_result\.data\.custom\.\* | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'add comment'
Add a comment to a ticket

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** |  required  | FQID for Alert | string | 
**comment** |  required  | Comment to add | string | 
**kind** |  required  | Kind | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.fqid | string | 
action\_result\.parameter\.comment | string | 
action\_result\.parameter\.kind | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get user'
Get User details

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username user.name@email.com (also note * is permited... *@blah.com) | string | 
**status** |  required  | User Status (Multi Value CSV eg: active,pending) | string | 
**assignments** |  required  | Assignments groups | string | 
**includeinactivepolicies** |  required  | includeInactivePolicies (use true / false) | string | 
**detailsuserfirstname** |  required  | select by firstName of user. Use * for wildcards | string | 
**detailsuserlastname** |  required  | select by lastName of user. Use * for wildcards | string | 
**includes** |  optional  | resource to get extra data like tenant, policy-assignments, etc | string | 
**parentstatuses** |  optional  | statuses of parent entity | string | 
**limit** |  optional  | max records to return (defaults to 100) | numeric | 
**offset** |  optional  | number of records to skip (defaults to 0) | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.username | string | 
action\_result\.parameter\.status | string | 
action\_result\.parameter\.assignments | string | 
action\_result\.parameter\.includeinactivepolicies | boolean | 
action\_result\.parameter\.detailsuserfirstname | string | 
action\_result\.parameter\.detailsuserlastname | string | 
action\_result\.parameter\.includes | string | 
action\_result\.parameter\.parentstatuses | string | 
action\_result\.parameter\.limit | numeric | 
action\_result\.parameter\.offset | numeric | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'set status'
Set ticket (issue) status

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** |  required  | Ticket (Issue) Key | string | 
**status\_id** |  required  | Status ID | string | 
**status\_title** |  required  | Alias / Status title | string | 
**status\_category** |  required  | Status Category | string | 
**assignee\_id** |  required  | Assignee ID | string | 
**kind** |  required  | Kind | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.fqid | string | 
action\_result\.parameter\.status\_id | string | 
action\_result\.parameter\.status\_title | string | 
action\_result\.parameter\.status\_category | string | 
action\_result\.parameter\.assignee\_id* | string | 
action\_result\.parameter\.kind | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a ITM asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base_url** |  required  | string | Base URL / Domain, i.e https://xyz.proofpoint.com
**api_version** |  optional  | string | API version: v1 / v2 / v3
**client_id** |  required  | string | Client ID
**client_secret** |  required  | password | Client Secret

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[get email](#action-get-email) - Get an email from the server  
[assign owner](#action-assign-owner) - Update ticket (issue) to be owned by this person  
[get ticket](#action-get-ticket) - Get ticket (issue) information  
[add comment](#action-add-comment) - Add a comment to a ticket  
[get user](#action-get-user) - Get User details  
[set status](#action-set-status) - Set ticket (issue) status  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get email'
Get an email from the server

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** |  optional  | Message ID to get | string |  `email id` 
**attachments** |  optional  | Include Attachments | boolean | 
**stream** |  optional  | Stream Response | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data | string |  |  
action_result.summary | string |  |  
action_result.parameter.fqid | string |  `email id`  |  
action_result.parameter.attachments | string |  |  
action_result.parameter.stream | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
summary.total_objects | numeric |  |  
summary.total_objects_successful | numeric |  |    

## action: 'assign owner'
Update ticket (issue) to be owned by this person

Type: **generic**  
Read only: **False**

Assign Ticket to user as per the UI values in PP ITM Portal.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** |  required  | Issue ID | string | 
**assignee_id** |  optional  | Assign Ticket to this person by ID | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data | string |  |  
action_result.summary | string |  |  
action_result.parameter.fqid | string |  |  
action_result.parameter.assignee_id | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
action_result.data.0._status.code | string |  |  
action_result.data.0._status.status | string |  |  
action_result.data.0.annotations.comments.\*.text | string |  |  
action_result.data.0.annotations.history.\*.text | string |  |  
action_result.data.0.annotations.workflow.state.\* | string |  |  
action_result.data.0.indicators.\*.name | string |  |  
action_result.data.0.messages.\*.subject | string |  |  
action_result.data.0.messages.\*.kind | string |  |  
action_result.data.0.messages.\*.recipients.\*.email | string |  |  
action_result.data.0.incident.status | string |  |  
action_result.data.0.incident.name | string |  |  
action_result.data.0.incident.severity | string |  |  
action_result.data.0.custom.\* | string |  |  
summary.total_objects | numeric |  |  
summary.total_objects_successful | numeric |  |    

## action: 'get ticket'
Get ticket (issue) information

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** |  required  | Ticket (Issue) FQID | string | 
**includes** |  optional  | Includes (Screenshots/---) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.summary | string |  |  
action_result.data.0._status.code | string |  |   it:error:some-error 
action_result.data.0._status.status | string |  |   400 
action_result.data.0._status.message | string |  |   Error obtaining data for event '4242cfb7-edc4-47e0-b8a1-aa547562bcba' with name 'Nice Name' 
action_result.data.0.annotations.comments.\*.text | string |  |   This is a note or comment in PP ITM 
action_result.data.0.annotations.history.\*.text | string |  |  
action_result.data.0.annotations.workflow.state.\* | string |  |   status : incident:status:new 
action_result.data.0.indicators.\*.name | string |  |   Whatever you configure in PP ITM 
action_result.data.0.messages.\*.subject | string |  |   Greetings from Nigeria 
action_result.data.0.messages.\*.kind | string |  |   email 
action_result.data.0.messages.\*.recipients.\*.email | string |  |   user.name@domain.name.com 
action_result.data.0.incident.status | string |  |   incident:status:new 
action_result.data.0.incident.name | string |  |   EMAIL-DLP-PCI 
action_result.data.0.incident.severity | string |  |   incident:severity:850:critical 
action_result.data.0.custom.\* | string |  |   Do you think i will have to take this out? 
action_result.parameter.fqid | string |  |  
action_result.parameter.includes | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
summary.total_objects | numeric |  |  
summary.total_objects_successful | numeric |  |    

## action: 'add comment'
Add a comment to a ticket

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** |  required  | FQID for Alert | string | 
**comment** |  required  | Comment to add | string | 
**kind** |  required  | Kind | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data | string |  |  
action_result.summary | string |  |  
action_result.parameter.fqid | string |  |  
action_result.parameter.comment | string |  |  
action_result.parameter.kind | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
summary.total_objects | numeric |  |  
summary.total_objects_successful | numeric |  |    

## action: 'get user'
Get User details

Type: **investigate**  
Read only: **True**

Get a list of all users and their user attributes, or search the system for a single user id by username/string all values are optional.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  optional  | Username user.name@email.com (also note \* is permited... \*@blah.com) | string | 
**status** |  optional  | User Status (Multi Value CSV eg: active,pending) | string | 
**assignments** |  optional  | Assignments groups | string | 
**includeinactivepolicies** |  optional  | IncludeInactivePolicies (use true / false) | string | 
**detailsuserfirstname** |  optional  | Select by firstName of user. Use \* for wildcards | string | 
**detailsuserlastname** |  optional  | Select by lastName of user. Use \* for wildcards | string | 
**includes** |  optional  | Resource to get extra data like tenant, policy-assignments, etc | string | 
**parentstatuses** |  optional  | Statuses of parent entity | string | 
**limit** |  optional  | Max records to return (defaults to 100) | numeric | 
**offset** |  optional  | Number of records to skip (defaults to 0) | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data | string |  |  
action_result.summary | string |  |  
action_result.parameter.username | string |  |  
action_result.parameter.status | string |  |  
action_result.parameter.assignments | string |  |  
action_result.parameter.includes | string |  |  
action_result.parameter.parentstatuses | string |  |  
action_result.parameter.includeinactivepolicies | boolean |  |  
action_result.parameter.limit | numeric |  |  
action_result.parameter.detailsuserfirstname | string |  |  
action_result.parameter.detailsuserlastname | string |  |  
action_result.parameter.offset | numeric |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
summary.total_objects | numeric |  |  
summary.total_objects_successful | numeric |  |    

## action: 'set status'
Set ticket (issue) status

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fqid** |  required  | Ticket (Issue) Key | string | 
**status_id** |  required  | Status ID | string | 
**status_title** |  required  | Alias / Status title | string | 
**status_category** |  required  | Status Category | string | 
**assignee_id** |  required  | Assignee ID | string | 
**kind** |  required  | Kind | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data | string |  |  
action_result.summary | string |  |  
action_result.parameter.fqid | string |  |  
action_result.parameter.status_id | string |  |  
action_result.parameter.status_title | string |  |  
action_result.parameter.status_category | string |  |  
action_result.parameter.assignee_id | string |  |  
action_result.parameter.kind | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
summary.total_objects | numeric |  |  
summary.total_objects_successful | numeric |  |  