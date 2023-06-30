# URL Data Contract
### Last Edited (dd/mm/yyyy):  06/30/2023
### By: [Jordan Hasulube](https://www.linkedin.com/in/jordan-hasulube-426814236) - Data Decisioning Intern

## Table of Contents
* Summary
* Metadata
* Dataset-&-Schema
* Stakeholders
* Roles
* Consequences
* Automation

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
domainOwner: Senthil Selvaraj
partionedOn: URL
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
|domain| Yes | The domain that the current contract is responsible for describing|
|domainOwner| Yes | The owner of the current domain. Person responsible for the accuracy and continuity of the contract|
| partitionedOn | No | The column of the master table that its rows were partitioned on.|
| quantumName | No | ??? |
| uniqueContractId |Yes| A unique identifier used to reduce the risk of dataset name collisions; currently we do not have a way to generate the unique ID|
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

## Dataset & Schema
This section describes the dataset and the schema of the data contract.

```YAML
dataset: 
  - table: url master
    physicalName: URL_MASTER # default value is table name + version separated by underscores, as table_1_2_0
    priorTableName: null # if needed (When and why was this used?)
    description: Master dimension of all practices 
    tags: null
    dataGranularity: One row per practice
    columns:
      - column: url_key
        isPrimary: true # NEW in v2.1.0, Optional, default value is false, indicates whether the column is primary key in the table.
        businessName: url primary identifier
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: null
        partitionStatus: fasle(Is any of our master tables partitioned? are all of them partitioned?)
        clusterStatus: null (How will this look specifically in our database?) Not needed
        criticalDataElementStatus: null #is this column critical for the table
        tags: null
        classification: null #ask dave
        transformSourceTables: null (Is this the same information I am recording in Data Dictionaries?)
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: url
        isPrimary: false # NEW in v2.1.0, Optional, default value is false, indicates whether the column is primary key in the table.
        businessName: url
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: null
        partitionStatus: false
        clusterStatus: null
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        encryptedColumnName: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
        - column: domain
        isPrimary: false # NEW in v2.1.0, Optional, default value is false, indicates whether the column is primary key in the table.
        businessName: url domain name
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: null
        partitionStatus: false
        clusterStatus: null
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        encryptedColumnName: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
        - column: hp_score
        isPrimary: false 
        businessName: url business score
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: null
        partitionStatus: false
        clusterStatus: null
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        encryptedColumnName: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
        - column: source
        isPrimary: false # NEW in v2.1.0, Optional, default value is false, indicates whether the column is primary key in the table.
        businessName: url source
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: method used to attain the url ex: webscrape, linkedin, etc.
        partitionStatus: false
        clusterStatus: null
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        encryptedColumnName: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
        - column: url_status
        isPrimary: false 
        businessName: ???
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: ???
        partitionStatus: false
        clusterStatus: null
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        encryptedColumnName: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
        - column: load_date
        isPrimary: false # NEW in v2.1.0, Optional, default value is false, indicates whether the column is primary key in the table.
        businessName: date added
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: null
        partitionStatus: false
        clusterStatus: null
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        encryptedColumnName: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
        - column: modified_date
        isPrimary: false # NEW in v2.1.0, Optional, default value is false, indicates whether the column is primary key in the table.
        businessName: modified date
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: true
        description: date the url was modified(if not modified, set to null)
        partitionStatus: false
        clusterStatus: null
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        encryptedColumnName: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
```

### Definitions

|Key|Required|Description|
| --- | --- | --- | 
dataset|Yes|Array. A list of tables within the dataset to be cataloged
dataset.table|Yes|Name of the table being cataloged; the value should only contain the table name. Do not include the project or dataset name in the value.
dataset.physicalName|No|Physical name of the table, default value is table name + version separated by underscores, as `table_1_2_0`.|
dataset.priorTableName|Yes|Name of the previous version of the dataset.|
dataset.dataGranularity|No|Granular level of the data in the table. Example would be `pmt_txn_id`.|
dataset.columns||Yes|Array. A list of columns in the table.|
dataset.columns.column|Yes|the name of the column.|
dataset.columns.isPrimaryKey|No|Boolean value specifying whether the column is primary or not. Default is false.|
dataset.columns.businessName|Yes|A more conversational name for the column. Think about it as changing from  'Data Speak' to 'English'.|
dataset.columns.logicalType|Yes|The logical data type of the column For example, 'varchar' would fit under the type of 'string'.|
dataset.columns.physicalType|Yes|The actual physical column data type. |
dataset.columns.isNullable|Yes|indicates if the column may contain Null values; possible values are true and false.|
dataset.columns.partitionStatus|Yes|indicates if the column is partitioned; possible values are true and false.|
dataset.columns.clusterStatus|Yes|indicates of the column is clustered; possible values are true and false.|
dataset.columns.classification|Yes|the PayPal data classification indicating the class of data in the column; expected values are 1, 2, 3, 4, or 5.|
|dataset.columns.authoritativeDefinitions|No|list of links to sources that provide more detail on column logic or values; examples would be URL to a GitHub repo, Collibra, on another tool.|
dataset.columns.encryptedColumnName|Yes|The column name within the table that contains the encrypted column value. For example, unencrypted column `email_address` might have an encryptedColumnName of `email_address_encrypt`.
dataset.columns.criticalDataElementStatus|No|True or false indicator; If element is considered a critical data element (CDE) then true else false.|
dataset.columns.tags|No|A list of tags that may be assigned to the dataset, table or column; the tags keyword may appear at any level.|

## Stakeholders
This section lists stakeholders and the history of their relation with this data contract.

```YAML
contractStakeholders: 
  - username: David Austin
    role: Data Innovation Manager
    dateIn: 2022-08-02
    dateOut: null
    replacedByUsername: null
```

### Definitions
The UX label is the label used in the UI and other user experiences. It is not limited to BlueRacket.

|Key|UX label|Required|Description|
| --- | --- | --- | --- |
stakeholders||No|Array
stakeholders.username||No|The stakeholder's username or email.|
stakeholders.role||No|The stakeholder's job role; Examples might be owner, data steward. There is no limit on the role.|
stakeholders.dateIn||No|The date when the user became a stakeholder.|
stakeholders.dateOut||No|The date when the user ceased to be a stakeholder|
stakeholders.replacedByUsername||No|The username of the user who replaced the stakeholder|

## Roles 

This section lists the roles that a consumer may need to access the dataset depending on the type of access they require.

```YAML
- role: datagov_r
    access: read
    firstLevelApprovers: IT
    secondLevelApprovers: null
- role: datagov_rw
    access: read and write
    firstLevelApprovers: Senthil and Parker
    secondLevelApprovers: null
```

### Definitions

|Key|Required|Description|
| --- | --- | --- |
roles|Yes|Array. A list of roles that will provide user access to the dataset.|
roles.role|Yes|name of the IAM role that provides access to the dataset; the value will generally come directly from the "BQ dataset to IAM roles mapping" document.|
roles.access|Yes|the type of access provided by the IAM role; the value will generally come directly from the "BQ dataset to IAM roles mapping" document.|
roles.firstLevelApprovers|No|the name(s) of the first level approver(s) of the role; the value will generally come directly from the "BQ dataset to IAM roles mapping" document.|
roles.secondLevelApprovers|No|the name(s) of the second level approver(s) of the role; the value will generally come directly from the "BQ dataset to IAM roles mapping" document.|


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
