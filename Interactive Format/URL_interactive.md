# URL Data Contract
### Last Edited (dd/mm/yyyy):  06/30/2023
### By: [Jordan Hasulube](https://www.linkedin.com/in/jordan-hasulube-426814236) - Data Decisioning Intern

## Table of Contents
* [Summary](#Summary)
* [Metadata](#Metadata)
* [Dataset and Schema](#Dataset-and-Schema)
* [Stakeholders](#Stakeholders)
* [Roles](#Roles)
* [Service Level Agreements](#Service-Level-Agreements)

## Summary


### What is _a data contract_?
* A data contract is a formal agreement between two parties (data product provider and data product consumer).
It specifies the guarantees about a provided data set and expectations concerning data product access.

### This Contract
* This contract describes the keys and values expected in the URL data contract. It is divided in multiple sections: Metadata, Dataset & Schema, Stakeholders, Roles, Concequences, and Automation. Each section contains a [YAML](https://www.redhat.com/en/topics/automation/what-is-yaml) file followed by definitions for its keys.

## Metadata
This section contains general information about this Data Contract.
<details>
  <summary>Keys and Values</summary>

```YAML
# URL MASTER
domain: url
domainOwner: Senthil Selvaraj
partionedOn: URL
quantumName: url quantum
usagePurpose: Inventory; Analytical
version: 0.0.2
status: current
uniqueContractId: (fka uuid) For lineage/traceability purposes of this contract
activeDate: null
nextReassessmentDate: null

# Contract Description
description:
  purpose: Tables and attributes related to URLs. Talk to Senthil about expanding on this
  limitations: Financial Reporting
tenant: revance

# Getting support (Should probably use an email DL instead of this system)
teamSupportDl: dl.dd@revance.com
teamSupportSlackChannel: null
pointOfContact:
  - name: Senthil Selvaraj
    email: senthil.selvaraj@revance.com
  - name: Parker Hanna
    email: parker.hanna@revance.com

# Physical parts
sourcePlatform: snowflake
sourceSystem: snowflake

kind: virtualDataset
type: tables

# Physical access
#DRIVER INFORMATION REMOVED. NOT APPLICABLE FOR REVANCE
database: staging_test
schema: cdp
schedulerAppName: null #IE Data Bricks, Airflow, Data ALM, etc.

# Tags
tags: null
```
</details>

<details>
  <summary>Definitions</summary>

|Key|Required|Description|
| --- | --- | --- |
|domain| Yes | The domain that the current contract is responsible for describing.|
|domainOwner| Yes | The owner of the current domain. Person responsible for the accuracy and continuity of the contract.|
| partitionedOn | No | The column of the master table that its rows were partitioned on.|
| quantumName | No | Name given to the quantum by George Earl. |
| usagePurpose | No | Description of what kind of tasks this domain may be used for. |
| version|Yes|Current version of the data contract.|
status|Yes|Current status of the dataset. Example value would be current. |
| uniqueContractId |Yes| A unique identifier used to reduce the risk of dataset name collisions; currently we do not have a way to generate the unique ID.|
|activeDate| Yes | The date that this contract becomes active.|
| nextReassessmentDate | No | The next date that the contract will be reassessed.|
description.purpose|No|Purpose of the dataset, table or column (depending on the level); the key may appear at the dataset, table, or column level.|
description.limitations|No|Limitations of the dataset, table or column (depending on the level); the key may appear at the dataset, table, or column level.|
description|No|Object.|
tenant|No|Indicates the property the data is primarily associated with. Value is case insensitive.|
|teamSypportDl | No | Email Distribution List where you can request for support. |
|teamSupportSlackChannel | No | Slack channel where you can reach out to for support. Not set up as of July 2023. |
pointOfContact| Yes | an array containing points of contact using name and email. |
pointOfContact.name|No|Name of employee to reach in order to inquire about the contract.
pointOfContact.email| Yes | Email related to the employee whos name occupies the pointOfContactName field.
sourcePlatform|Yes|The platform where the dataset resides.
sourceSystem|Yes|The system where the dataset resides.  Example values are Snowflake and BigQuery|
kind|Yes|The kind of Rosewall dataset being cataloged; Expected values are `virtualDataset` or `managedDataset`.
|type|Yes|Identifies the types of objects in the dataset.  For Snowflake the expected value would be tables.
database|Yes|Database in which the target table resides.|
schema|Yes|The schema in Snowflake where the dataSet takes place.|
schedulerAppName| No | scheduler application used for this database |
tags|No|a list of tags that may be assigned to the dataset, table or column; the `tags` keyword may appear at any level.

</details>

## Dataset and Schema
This section describes the dataset and the schema of the data contract.
<details>
  <summary>Keys and Values</summary>

```YAML
dataset:
  - table: url master
    physicalName: URL_MASTER
    priorTableName: null
    description: Master dimension of all practices
    tags: null
    dataGranularity: One row per practice
    columns:
      - column: url_key
        isPrimary: true
        businessName: url primary identifier
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: null
        criticalDataElementStatus: null
        tags: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: url
        isPrimary: false
        businessName: url
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: null
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        transformSourceTables: '-OCE -OPUL -Provider AI'
        transformLogic: null
        transformDescription: Hygiene applied to the sourced websites
        sampleValues: null
      - column: domain
        isPrimary: false
        businessName: url domain name
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: null
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        transformSourceTables: '-OCE -OPUL -Provider AI'
        transformLogic: null
        transformDescription: Hygiene applied to the sourced websites
        sampleValues: null
      - column: hp_score
        isPrimary: false
        businessName: url business score
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: null
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        transformSourceTables: STITCH_DEV.CDPRAW.PAI_WEBPAGE_RAW
        transformLogic: null
        transformDescription: Direct pull from source for the respective URL
        sampleValues: null
      - column: source
        isPrimary: false
        businessName: url source
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: 'method used to attain the url ex webscrape, linkedin, etc.'
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        transformSourceTables: '-OCE -OPUL -Provider AI'
        transformLogic: null
        transformDescription: Source with reference to URL
        sampleValues: null
      - column: url_status
        isPrimary: false
        businessName: '???'
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: '???'
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: load_date
        isPrimary: false
        businessName: date added
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: false
        description: null
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: modified_date
        isPrimary: false
        businessName: modified date
        logicalType: string
        physicalType: VARCHAR(16777216)
        isNullable: true
        description: 'date the url was modified(if not modified, set to null)'
        criticalDataElementStatus: null
        tags: null
        classification: null
        authoritativeDefinitions: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
```
</details>

<details>
  <summary>Definitions</summary>
  
|Key|Required|Description|
| --- | --- | --- | 
dataset.columns.isPrimary|No|Boolean value specifying whether the column is primary or not. Default is false.|
dataset.columns.businessName|Yes|A more conversational name for the column. Think about it as changing from  'Data Speak' to 'English'.|
dataset.columns.logicalType|Yes|The logical data type of the column For example, 'varchar' would fit under the type of 'string'.|
dataset.columns.physicalType|Yes|The actual physical column data type. |
dataset.columns.isNullable|Yes|indicates if the column may contain Null values; possible values are true and false.|
dataset.columns.description| Yes| description of the column. Null if the column name is self-explanatory |
dataset.columns.criticalDataElementStatus|No|True or false indicator; If element is considered a critical data element (CDE) then true else false.|
dataset.columns.tags|No|A list of tags that may be assigned to the dataset, table or column; the tags keyword may appear at any level.|
dataset.columns.classification|Yes|the PayPal data classification indicating the class of data in the column; expected values are 1, 2, 3, 4, or 5.|
|dataset.columns.authoritativeDefinitions|No|list of links to sources that provide more detail on column logic or values; examples would be URL to a GitHub repo, Collibra, on another tool.|
dataset|Yes|Array. A list of tables within the dataset to be cataloged
dataset.columns.transformSourceTables| No | Source table(s) for the data in this column. Common sources would be OCE and OPUL |
dataset.columns.transformLogic| No | Exact SQL statements performed to get the data in its current state |
dataset.columns.transformDescription| No | Informal Description of Transformation Logic in a more understandable way |
dataset.columns.sampleValues| No | Sample values for the column to help the viewer understand exaclty what it is |
dataset.table|Yes|Name of the table being cataloged; the value should only contain the table name. Do not include the project or dataset name in the value.
dataset.physicalName|No|Physical name of the table, default value is table name + version separated by underscores, as `table_1_2_0`.|
dataset.columns||Yes|Array. A list of columns in the table.|
dataset.columns.column|Yes|the name of the column.|
</details>

## Stakeholders
This section lists stakeholders and the history of their relation with this data contract.

<details>
  <summary>Keys and Values</summary>
  
```YAML
contractStakeholders: 
  - name: David Austin
    email: david.austin@revance.com
    role: Data Innovation Manager
    dateIn: 2023-04-10
    dateOut: null
    replacedByUsername: null
```
</details>

<details>
  <summary>Definitions</summary>
  
|Key|Required|Description|
| --- | --- | --- |
contractStakeholders|No|Array
contractStakeholders.name|Yes|The stakeholder's first and last name|
contractStakeholders.email|No| The stakeholder's work email|
contractStakeholders.role|No|The stakeholder's job role; Examples might be owner, data steward. There is no limit on the role.|
contractStakeholders.dateIn|No|The date when the user became a stakeholder.|
contractStakeholders.dateOut|No|The date when the user ceased to be a stakeholder|
contractStakeholders.replacedByUsername|No|The username of the user who replaced the stakeholder|
</details>

## Roles 

This section lists the roles that a consumer may need to access the dataset depending on the type of access they require.

<details>
  <summary>Keys and Values</summary>
  
```YAML
- role: datagov_r
  access: read only
  approvers:
    - name: IT
      approvalLevel: 1
- role: datagov_rw
  access: read and write
  approvers:
    - name: Senthil Salvaraj
      approvalLevel: 1
    - name: Parker Hanna
      approvalLevel: 1
```
</details>

<details>
  <summary>Definitions</summary>
  
|Key|Required|Description|
| --- | --- | --- |
roles|Yes|Array. A list of roles that will provide user access to the dataset.|
roles.role|Yes|name of the IAM role that provides access to the dataset.|
roles.access|Yes|the type of access provided by the IAM role; the value will generally come directly from the "BQ dataset to IAM roles mapping" document.|
roles.firstLevelApprovers|No|the name(s) of the first level approver(s) of the role.|
roles.secondLevelApprovers|No|the name(s) of the second level approver(s) of the role.|
</details>


