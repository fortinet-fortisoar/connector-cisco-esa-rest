## About the connector
The Cisco Email Security Virtual Appliance significantly lowers the cost of deploying email security, especially in highly distributed networks. Spam and malware are part of a complex email security picture that includes inbound threats and outbound risks. The all-in-one Cisco ESA (Email Security Appliance) offers simple, fast deployment with few maintenance requirements, low latency, and low operating costs. 
<p>This document provides information about the Cisco ESA(REST) Connector, which facilitates automated interactions, with a Cisco ESA(REST) server using FortiSOAR&trade; playbooks. Add the Cisco ESA(REST) Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Cisco ESA(REST).</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-cisco-esa-rest</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Cisco ESA(REST) server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Cisco ESA(REST) server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Cisco ESA(REST)</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server Address</td><td>IP address or FQDN of the Cisco ESA endpoint server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Username</td><td>Username to access the Cisco ESA server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Password</td><td>Password to access the Cisco ESA server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Search Quarantine Messages</td><td>Retrieves the detailed list of quarantine messages based on the parameters that you have specified.</td><td>search_quarantine_messages <br/>Investigation</td></tr>
<tr><td>Get Quarantine Message By ID</td><td>Retrieves the details of quarantine message based on the parameters that you have specified.</td><td>get_quarantine_message <br/>Investigation</td></tr>
<tr><td>Release Quarantine Messages</td><td>Release the quarantine messages based on the parameters that you have specified.</td><td>release_quarantine_message <br/>Investigation</td></tr>
<tr><td>Delete Quarantine Messages</td><td>Delete the quarantine messages based on the parameters that you have specified.</td><td>delete_quarantine_message <br/>Investigation</td></tr>
<tr><td>Search Safelist or Blocklist Entries</td><td>Retrieves the detailed list of safelist or blocklist entries based on the parameters that you have specified.</td><td>search_safelist_or_blocklist_entries <br/>Investigation</td></tr>
<tr><td>Edit Safelist or Blocklist Entries</td><td>Add, edit or append safelist/blocklist entries based on the parameters that you have specified.</td><td>edit_safelist_or_blocklist_entries <br/>Investigation</td></tr>
<tr><td>Delete Safelist or Blocklist Entries</td><td>Delete safelist/blocklist entries based on the parameters that you have specified.</td><td>delete_safelist_or_blocklist_entries <br/>Investigation</td></tr>
<tr><td>Get Message DLP Details</td><td>Retrieves the details of DLP of messages based on the parameters that you have specified.</td><td>get_message_dlp_details <br/>Investigation</td></tr>
<tr><td>Get Message AMP Details</td><td>Retrieves the advanced malware protection details of messages based on the parameters that you have specified.</td><td>get_message_amp_details <br/>Investigation</td></tr>
<tr><td>Get Message URL Details</td><td>Retrieves the URL details of messages based on the parameters that you have specified.</td><td>get_message_url_details <br/>Investigation</td></tr>
<tr><td>Get Report</td><td>Retrieves report details based on the parameters that you have specified.</td><td>get_report <br/>Investigation</td></tr>
</tbody></table>

### operation: Search Quarantine Messages
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Start Datetime</td><td>Specify the start datetime of the duration from when the data should be fetched.
</td></tr><tr><td>End Datetime</td><td>Specify the end datetime of the duration till when the data should be fetched.
</td></tr><tr><td>Quarantine Type</td><td>Specify the quarantine type to filter the records.
</td></tr><tr><td>Order By</td><td>Specify the order by to sort the records.
</td></tr><tr><td>Sort</td><td>Specify the sorting order of the records.
</td></tr><tr><td>Offset</td><td>Specify the offset to fetch the records. Note: If you specify limit then you must specify this parameter.
</td></tr><tr><td>Limit</td><td>Specify the limit to fetch the records. Note: If you specify offset then you must specify this parameter.
</td></tr><tr><td>Recipient Filter Operator</td><td>Specify the recipient filter operator to filter the records.
</td></tr><tr><td>Recipient Filter Value</td><td>Specify the recipient filter value to filter the records.
</td></tr><tr><td>Filter Operator</td><td>Specify the filter operator to filter the records.
</td></tr><tr><td>Filter Value</td><td>Specify the filter value to filter the records.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "meta": {
        "totalCount": ""
    },
    "data": [
        {
            "attributes": {
                "envelopeRecipient": [],
                "toAddress": [],
                "subject": "",
                "date": "",
                "fromAddress": [],
                "size": ""
            },
            "mid": ""
        }
    ]
}</pre>
### operation: Get Quarantine Message By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Message ID</td><td>Specify the message ID to fetch the details.
</td></tr><tr><td>Quarantine Type</td><td>Specify the quarantine type to fetch the details.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "attributes": {
            "envelopeRecipient": [],
            "toAddress": [],
            "attachments": [],
            "messageBody": "",
            "date": "",
            "fromAddress": [],
            "subject": ""
        },
        "mid": ""
    }
}</pre>
### operation: Release Quarantine Messages
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Message ID</td><td>Specify comma separated message IDs to release the quarantine messages.
</td></tr><tr><td>Action</td><td>Specify the action to release the quarantine messages.
</td></tr><tr><td>Quarantine Type</td><td>Specify the quarantine type to release the quarantine messages.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "action": "",
        "totalCount": ""
    }
}</pre>
### operation: Delete Quarantine Messages
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Message ID</td><td>Specify comma separated message IDs to delete the quarantine messages.
</td></tr><tr><td>Quarantine Type</td><td>Specify the quarantine type to delete the quarantine messages.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "action": "",
        "totalCount": ""
    }
}</pre>
### operation: Search Safelist or Blocklist Entries
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Safelist or Blocklist</td><td>Specify whether you want to retrieve safelist entries or blocklist entries.
</td></tr><tr><td>Action</td><td>Specify the action to fetch the records.
</td></tr><tr><td>Quarantine Type</td><td>Specify the quarantine type to filter the records.
</td></tr><tr><td>View By</td><td>Specify the view by as sender or recipient to filter the records.
</td></tr><tr><td>Order By</td><td>Specify the order by as sender or recipient to filter the records.
</td></tr><tr><td>Offset</td><td>Specify the offset to fetch the records. Note: If you specify limit then you must specify this parameter.
</td></tr><tr><td>Limit</td><td>Specify the limit to fetch the records. Note: If you specify offset then you must specify this parameter.
</td></tr><tr><td>Sort</td><td>Specify the sorting order of the records.
</td></tr><tr><td>Search</td><td>Specify the value. This is only supported for the attribute orderBy=recipient.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "meta": {
        "totalCount": ""
    },
    "data": [
        {
            "senderList": [],
            "recipientAddress": ""
        }
    ]
}</pre>
### operation: Edit Safelist or Blocklist Entries
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Safelist or Blocklist</td><td>Specify whether you want to edit safelist entries or blocklist entries.
</td></tr><tr><td>Action</td><td>Specify the action to edit the entries.
</td></tr><tr><td>Quarantine Type</td><td>Specify the quarantine type to edit the records.
</td></tr><tr><td>View By</td><td>Specify the view by as sender or recipient to edit the entries.
</td></tr><tr><td>Recipient Addresses</td><td>Specify the comma separated recipient addresses to edit the entries.
</td></tr><tr><td>Recipient List</td><td>Specify the comma separated recipient values to edit the entries.
</td></tr><tr><td>Sender Addresses</td><td>Specify the comma separated sender addresses to edit the entries.
</td></tr><tr><td>Sender List</td><td>Specify the comma separated sender values to edit the entries.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "action": "",
    "quarantineType": "",
    "recipientAddresses": [],
    "senderList": [],
    "viewBy": ""
}</pre>
### operation: Delete Safelist or Blocklist Entries
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Safelist or Blocklist</td><td>Specify whether you want to delete safelist entries or blocklist entries.
</td></tr><tr><td>Quarantine Type</td><td>Specify the quarantine type to delete the entries.
</td></tr><tr><td>Recipient List</td><td>Specify the comma separated recipient values to delete the entries.
</td></tr><tr><td>Sender List</td><td>Specify the comma separated sender values to delete the entries.
</td></tr><tr><td>View By</td><td>Specify the view by as sender or recipient to delete the entries.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "quarantineType": "",
    "recipientList": "",
    "viewBy": ""
}</pre>
### operation: Get Message DLP Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Start Datetime</td><td>Specify the start datetime of the duration from when the data should be fetched.
</td></tr><tr><td>End Datetime</td><td>Specify the end datetime of the duration till when the data should be fetched.
</td></tr><tr><td>Serial Number</td><td>Specify the serial number of the email gateway.
</td></tr><tr><td>Message ID</td><td>Specify the mid of the message. Note: You must specify Injection Connection ID if you specify this parameter.
</td></tr><tr><td>Injection Connection ID</td><td>Specify the icid of the message. Note: You must specify Message ID if you specify this parameter.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "messages": {
            "direction": "",
            "smtpAuthId": "",
            "sender": "",
            "midHeader": "",
            "timestamp": "",
            "hostName": "",
            "mid": [
                ""
            ],
            "sendingHostSummary": {},
            "attachments": [],
            "messageSize": "",
            "dlpDetails": {
                "violationSeverity": "",
                "dlpMatchedContent": [
                    {
                        "messagePartMatch": [
                            {
                                "classifier": "",
                                "classifierMatch": []
                            }
                        ],
                        "messagePart": ""
                    }
                ],
                "mid": "",
                "riskFactor": "",
                "dlpPolicy": ""
            },
            "showDLPDetails": "",
            "senderGroup": "",
            "recipient": [],
            "subject": ""
        }
    }
}</pre>
### operation: Get Message AMP Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Start Datetime</td><td>Specify the start datetime of the duration from when the data should be fetched.
</td></tr><tr><td>End Datetime</td><td>Specify the end datetime of the duration till when the data should be fetched.
</td></tr><tr><td>Serial Number</td><td>Specify the serial number of the email gateway.
</td></tr><tr><td>Message ID</td><td>Specify the mid of the message. Note: You must specify Injection Connection ID if you specify this parameter.
</td></tr><tr><td>Injection Connection ID</td><td>Specify the icid of the message. Note: You must specify Message ID if you specify this parameter.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "messages": {
            "showAMPDetails": "",
            "direction": "",
            "smtpAuthId": "",
            "sender": "",
            "midHeader": "",
            "timestamp": "",
            "hostName": "",
            "mid": [
                ""
            ],
            "sendingHostSummary": {},
            "attachments": [],
            "messageSize": "",
            "ampDetails": [
                {
                    "timestamp": "",
                    "description": ""
                }
            ],
            "senderGroup": "",
            "recipient": [],
            "subject": ""
        }
    }
}</pre>
### operation: Get Message URL Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Start Datetime</td><td>Specify the start datetime of the duration from when the data should be fetched.
</td></tr><tr><td>End Datetime</td><td>Specify the end datetime of the duration till when the data should be fetched.
</td></tr><tr><td>Serial Number</td><td>Specify the serial number of the email gateway.
</td></tr><tr><td>Message ID</td><td>Specify the mid of the message. Note: You must specify Injection Connection ID if you specify this parameter.
</td></tr><tr><td>Injection Connection ID</td><td>Specify the icid of the message. Note: You must specify Message ID if you specify this parameter.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "messages": {
            "direction": "",
            "smtpAuthId": "",
            "sdrAge": "",
            "sender": "",
            "midHeader": "",
            "urlDetails": [
                {
                    "timestamp": "",
                    "description": ""
                }
            ],
            "sdrCategory": "",
            "hostName": "",
            "mid": [
                ""
            ],
            "sendingHostSummary": {},
            "attachments": [],
            "sdrReputation": "",
            "showURLDetails": "",
            "senderGroup": "",
            "recipient": [],
            "subject": ""
        }
    }
}</pre>
### operation: Get Report
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Report Type</td><td>Specify the report type to fetch the report details.
</td></tr><tr><td>Start Datetime</td><td>Specify the start datetime of the duration from when the data should be fetched.
</td></tr><tr><td>End Datetime</td><td>Specify the end datetime of the duration till when the data should be fetched.
</td></tr><tr><td>Device Type</td><td>Specify the device type to fetch the report details.
</td></tr><tr><td>Query Type</td><td>Specify the query type to fetch the report details.
</td></tr><tr><td>Order By</td><td>Specify the order by to sort the records. Note: If you specify this parameter then you must specify Sort.
</td></tr><tr><td>Sort</td><td>Specify the sorting order of the records. Note: If you specify this parameter then you must specify Order By.
</td></tr><tr><td>Offset</td><td>Specify the offset to fetch the records. Note: If you specify limit then you must specify this parameter.
</td></tr><tr><td>Limit</td><td>Specify the limit to fetch the records. Note: If you specify offset then you must specify this parameter.
</td></tr><tr><td>Data Retrieval</td><td>Specify the number of records with the highest values to return.
</td></tr><tr><td>Filter Value</td><td>Specify the filter value to fetch the report details.
</td></tr><tr><td>Filter By</td><td>Filter the data to be retrieved according to the filter property and value.
</td></tr><tr><td>Filter Operator</td><td>Specify the filter operator to fetch the report details.
</td></tr><tr><td>Device Group Name</td><td>Specify the device group name to fetch the report details.
</td></tr><tr><td>Device Name</td><td>Specify the device name to fetch the report details.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "meta": {
        "totalCount": ""
    },
    "data": {
        "type": "",
        "resultSet": ""
    }
}</pre>
## Included playbooks
The `Sample - cisco-esa-rest - 1.0.0` playbook collection comes bundled with the Cisco ESA(REST) connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Cisco ESA(REST) connector.

- Search Quarantine Messages
- Get Quarantine Message By ID
- Release Quarantine Messages
- Delete Quarantine Messages
- Search Safelist or Blocklist Entries
- Edit Safelist or Blocklist Entries
- Delete Safelist or Blocklist Entries
- Get Message DLP Details
- Get Message AMP Details
- Get Message URL Details
- Get Report

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
