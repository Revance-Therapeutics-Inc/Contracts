# URL Data Contract
### Last Edited (dd/mm/yyyy):  06/30/2023
### By: [Jordan Hasulube](https://www.linkedin.com/in/jordan-hasulube-426814236) - Data Decisioning Intern

## Table of Contents
* Summary
* Metadata
* Dataset-&-Schema
* Roles
* Contract-Duration

## Summary
* Service-level objectives
  * Interval of change
  * Latency
  * Completeness
  * Freshness
  * Availability
  * Performance
  * Data volume
* Terms
  * Allowed usage and access patterns
  * Query frequency
* Roles
  * The IAM role definition to grant
* Contract duration
  * Start date
  * Notice period and end date
  * Next reassessment date

### What is _a data contract_?
* A data contract is a formal agreement between two parties (data product provider and data product consumer).
It specifies the guarantees about a provided data set and expectations concerning data product access.

### This Contract
* This contract describes the keys and values expected in the URL data contract. It is divided in multiple sections. Each section contains a [YAML](https://www.redhat.com/en/topics/automation/what-is-yaml) file followed by definitions for its keys.

## Metadata
This section contains general information about this Data Contract.

```YAML
# URL MASTER
domain: url
partionedOn: URL
domainOwner: Senthil Selvaraj
quantumName: **<tbd>** quantum
usagePurpose: Inventory; Analytical
version: 0.0.2
status: current
uniqueContractId: (fka uuid) For lineage/traceability purposes of this contract

# Contract Description
description:
  purpose: Tables and attributes related to URLs.(Is there more to purpose than just containing information?)
  limitations: null(limitations on what?)
  usage: null
tenant: revance

# Getting support(Do we need this? We have a section in the introduction where we provide an outlet for support)
pointOfContactName1:Senthil Selvaraj
relatedEmail: senthil.selvaraj@revance.com
pointofContactName2:Parker Hanna
relatedEmail: parker.hanna@revance.com
pointOfContactName3: Jordan Hasulube #To be removed after termination of internship
relatedEmail: jordan.hasulube@revance.com

# Physical parts Snowflake specific
sourcePlatform: snowflake
sourceSystem: snowflake
datasetProject: staging_test # snowflake database (Can we shange the key from dataSetProject to snowflakeDatabase or something similar?)
datasetName: cdp # snowflake schema (Same question as above)

kind: virtualDataset
type: tables

# Physical access
#DRIVER INFORMATION REMOVED. NOT APPLICABLE FOR REVANCE
database: staging
username: '${env.username}'
password: '${env.password}'
schedulerAppName: name_coming_from_scheduler # NEW 2.1.0 Required if you want to schedule stuff, comes from DataALM.

# Data Quality
quality: null # Do we need a section on Data Quality? George seemed to think so

# Tags
tags: null
```

|Key|Required|Description|
| --- | --- | --- |
| version|Yes|Current version of the data contract.|
| uuid|Yes| A unique identifier used to reduce the risk of dataset name collisions; initially the UUID will be created using a UUID generator tool ([example](https://www.uuidgenerator.net/)). However, we may want to develop a method that accepts a seed value using a combination of fields–such as name, kind and source–to create a repeatable value.|
|username|Yes|User credentials for connecting to the dataset; how the credentials will be stored/passed is outside of the scope of the contract.|
|userConsumptionMode|No|List of data modes for which the dataset may be used.  Expected sample values might be Analytical or Operational. <br/>Note: in the future, this will probably be replaced by ports.|
|type|Yes|Identifies the types of objects in the dataset.  For BigQuery the expected value would be tables.
tenant|No|Indicates the property the data is primarily associated with. Value is case insensitive. For PayPal, the expected sample values might be PayPal, Venmo, PPWC, etc.|
tags|No|a list of tags that may be assigned to the dataset, table or column; the `tags` keyword may appear at any level.
status|Yes|Current status of the dataset.
sourceSystem|Yes|The system where the dataset resides.  Expected value is bigQuery
sourcePlatform|Yes|The platform where the dataset resides. Expected value is googleCloudPlatform
server|Yes|The server where the dataset resides.|
quantumName|Yes|The name of the data quantum or data product.
productSlackChannel|No|Slack channel of the team responsible for maintaining the dataset.
productFeedbackUrl|No|The URL for submitting feedback to the team responsible for maintaining the dataset.|
productDl|No|The email distribution list (DL) of the persons or team responsible for maintaining the dataset.
password|Yes|User credentials for connecting to the dataset; how the credentials will be stored/passed is out of the scope of this contract.
kind|Yes|The kind of Rosewall dataset being cataloged; Expected values are `virtualDataset` or `managedDataset`.
driverVersion|Yes|The version of the connection driver to be used to connect to the dataset.|
driver|Yes|The connection driver required to connect to the dataset.|
description.usage|No|intended usage of the dataset, table, or column (depending on the level); the key may appear at the dataset, table, or column level.|
description.purpose|No|Purpose of the dataset, table or column (depending on the level); the key may appear at the dataset, table, or column level.|
description.limitations|No|Limitations of the dataset, table or column (depending on the level); the key may appear at the dataset, table, or column level.|
description|No|Object.|
datasetProject|Yes|GCP BigQuery dataset project name.|
datasetName|Yes|GCP BigQuery dataset name.|
|datasetDomain|No|Name of the logical domain dataset the contract describes. This field is only required for output data contracts. Examples: `imdb_ds_aggregate`, `receiver_profile_out`,  `transaction_profile_out`.|
database|Yes|The database where the dataset resides.|

**Example**

| Name                         | Value                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Data Product Provider**    | _Domain Team:_ Checkout<br>_Data Product:_ Webshop Orders<br>_Data Product Owner:_ Nicky Cree (nicky.cree@example.com)<br>_Output Port:_ bigquery_orders_latest_npii_v1                                                                                                                                                                                  |
| **Data Product Consumer**    | _Domain Team:_ Controlling<br>_Responsible contact:_ Aubrey Harlow (aubrey.harlow@example.com)                                                                                                                                                                                                                                                           |
| **Purpose**                  | Build a demand forecasting model                                                                                                                                                                                                                                                                                                                         |
| **Schema**                   | https://example.com/checkout/webshop-orders/bigquery_orders_latest_npii_v1/schema.yaml                                                                                                                                                                                                                                                                   |
| **Service-level objectives** | _Interval of change:_ Continuous streaming<br>_Latency:_ < 60 seconds<br>_Completeness:_ All orders since 2020-01-01T00:00:00Z<br/>_Freshness:_ Near real time, max. 60 seconds delay<br>_Availability:_ 99.9%<br>_Performance:_ Query all orders of last 12 months < 30 seconds<br>_Data volume:_ 5,000-10,000 orders per day expected, ~50 KiB / order |
| **Terms**                    | Max queries per minute: 10<br/>Max data processing per day: 1 TiB<br/>Pub/Sub subscriptions                                                                                                                                                                                                                                                              |
| **Security**                 | IAM service-account: serviceAccount:controlling-data-consumer@example-prod-data.iam.gserviceaccount.com                                                                                                                                                                                                                                                  |
| **Costs and Billing**        | Implementation and operational costs are covered by the checkout domain until 2023-12-31.                                                                                                                                                                                                                                                                |
| **Start date**               | 2023-04-01                                                                                                                                                                                                                                                                                                                                               |
| **End date**                 |                                                                                                                                                                                                                                                                                                                                                          |
| **Notice Period**            | 3 months                                                                                                                                                                                                                                                                                                                                                 |
| **Next reassessment date**   | 2024-04-01                                                                                                                                                                                                                                                                                                                                               | 


## Consequences

- A data contract gives clear expectations and requirements for building the  data product
- The contract must be fulfilled, but the internal implementation can change
- The data product can be extended as long as it is backward compatible with the contract
- A defined purpose is a motivation for the domain team to share the data with others in the first place
- Agreed service levels can be monitored, with an alerting system in place
- A contract can be canceled 


## Automation

- Data contracts can be provided to all potential customers by the data product developers and accepted through the data product consumer as a self-service. 
- Data platform automates the creation and revocation of IAM identities, roles, and access policies
- Reassessment reminder notification
