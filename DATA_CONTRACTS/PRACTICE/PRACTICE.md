# Practice Data Contract
### By: [Jordan Hasulube](https://www.linkedin.com/in/jordan-hasulube-426814236) - Data Decisioning Intern

## Table of Contents
* [Summary](#Summary)
* [Metadata](#Metadata)
* [Dataset and Schema](#Dataset-and-Schema)
* [Stakeholders](#Stakeholders)
* [Roles](#Roles)

## Summary

### What is _a data contract_?
* A data contract is a formal agreement between two parties (data product provider and data product consumer).
It specifies the guarantees about a provided data set and expectations concerning data product access.

### This Contract
* This contract describes the keys and values expected in the PRACTICE data contract. It is divided in multiple sections: Metadata, Dataset & Schema, Stakeholders, Roles, Concequences, and Automation. Each section contains a [YAML](https://www.redhat.com/en/topics/automation/what-is-yaml) file followed by definitions for its keys.

## Metadata
This section contains general information about this Data Contract.

```YAML
# PRACTICE MASTER
domain: PRACTICE
domainOwner: Senthil Selvaraj
domainOwnerEmail: senthil.selvaraj@revance.com
partitionedOn: null
quantumName: practice quantum
usagePurpose: null
description: null
limitations: null
version: 0.0.1
status: current
uniqueContractID: 99d2dd92-947c-439d-ae34-85bf032c139d
activeDate: null
nextReassessmentDate: null
tenant: Revance

# Getting support
teamSupportDl: dl.dd@revance.com
teamSupportSlackChannel: null

# Physical parts
sourcePlatform: snowflake
sourceSystem: snowflake

kind: virtualDataset
type: tables

# Physical access
database: STAGING_DEV
schema: CDP

# Tags
tags: null
```

|Key|Required|Description|
| --- | --- | --- |
|domain| Yes | The domain that the current contract is responsible for describing.|
|domainOwner| Yes | The owner of the current domain. Person responsible for the accuracy and continuity of the contract.|
| domainOwnerEmail | Yes | The email of the person who owns the domain |
| partitionedOn | No | The column of the master table that its rows were partitioned on.|
| quantumName | No | Name given to the quantum by George Earl. |
| usagePurpose | No | Description of what kind of tasks this domain may be used for. |
| description | Yes | Description of the domain and the nature of the data it holds|
| limitations | Yes| Description of areas that the data from this quantum cannot be used in |
| version|Yes|Current version of the data contract. Uses semantic versioning.|
status|Yes|Current status of the dataset. Example value would be current. |
| uniqueContractId |Yes| A unique identifier used to reduce the risk of dataset name collisions; version 4 uuid generated from [this URL](https://www.uuidgenerator.net/version1)|
|activeDate| Yes | The date that this contract becomes active.|
| nextReassessmentDate | No | The next date that the contract will be reassessed.|
tenant|No|Indicates the property the data is primarily associated with. Value is case insensitive.|
|teamSypportDl | No | Email Distribution List where you can request for support.|
|teamSupportSlackChannel | No | Slack channel where you can reach out to for support. Not set up as of July 2023. |
pointOfContact| Yes | an array containing points of contact using name and email. |
pointOfContact.name|No|Name of employee to reach in order to inquire about the contract.
pointOfContact.email| Yes | Email related to the employee whos name occupies the pointOfContactName field.
sourcePlatform|Yes|The platform where the dataset resides.
sourceSystem|Yes|The system where the dataset resides. Example values are Snowflake and BigQuery|
kind|Yes|The kind of Rosewall dataset being cataloged; Expected values are`virtualDataset`or`managedDataset`.
|type|Yes|Identifies the types of objects in the dataset. For Snowflake the expected value would betables.
database|Yes|Database in which the target table resides.|
schema|Yes|The schema in Snowflake where the dataSet takes place.|
schedulerAppName| No | scheduler application used for this database |
tags|No|a list of tags that may be assigned to the dataset, table or column; the `tags` keyword may appear at any level.

## Dataset and Schema
This section describes the dataset and the schema of the data contract.

```YAML
  - table: practice master 
    sourceTables: null
    physicalName: STAGING_DEV.CDP.PRACTICE_MASTER
    priorTableName: null
    description: master dimension of all practices
    tags: null
    dataGranularity: One row per practice
    columns:
      - column: practice_key
        isPrimary: true
        businessName: practice key 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: false
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: url_key
        isPrimary: false
        businessName: url key 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: location_key
        isPrimary: false
        businessName: location key 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: practice_name
        isPrimary: false
        businessName: practice name 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: derived_practice_name
        isPrimary: false
        businessName: derived practice name 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: customer_number
        isPrimary: false
        businessName: customer number 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: derived_customer_number
        isPrimary: false
        businessName: derived customer number 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: oce_salesforce_id
        isPrimary: false
        businessName: oce salesforce id 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: oce_account_type
        isPrimary: false
        businessName: oce account type 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: oce_account_status
        isPrimary: false
        businessName: oce account status 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: opul_platform_number
        isPrimary: false
        businessName: opul platform number 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: opul_salesforce_id
        isPrimary: false
        businessName: opul salesforce id 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: opul_organization_id
        isPrimary: false
        businessName: opul organization id 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: opul_gx_provider_id
        isPrimary: false
        businessName: opul gx provider id 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: opul_merchant_id
        isPrimary: false
        businessName: opul merchant id 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: opul_account_type
        isPrimary: false
        businessName: opul account type 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: categories
        isPrimary: false
        businessName: categories 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: specialty
        isPrimary: false
        businessName: specialty 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: street
        isPrimary: false
        businessName: street 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: city
        isPrimary: false
        businessName: city 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: state
        isPrimary: false
        businessName: state 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: postal_code
        isPrimary: false
        businessName: postal code 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: fulladdress
        isPrimary: false
        businessName: fulladdress 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: territory
        isPrimary: false
        businessName: territory 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: region
        isPrimary: false
        businessName: region 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: zone
        isPrimary: false
        businessName: zone 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: rha_customer
        isPrimary: false
        businessName: rha customer 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: daxi_customer
        isPrimary: false
        businessName: daxi customer 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: multi_locations
        isPrimary: false
        businessName: multi locations 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: phone
        isPrimary: false
        businessName: phone 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: email
        isPrimary: false
        businessName: email 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: url
        isPrimary: false
        businessName: url 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: domain
        isPrimary: false
        businessName: domain 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: is_national_account
        isPrimary: false
        businessName: is national account 
        logicalType: boolean
        physicalType: NUMBER(1,0)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: parent_salesforce_id
        isPrimary: false
        businessName: parent salesforce id 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: oce_parent_account_number
        isPrimary: false
        businessName: oce parent account number 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: oce_parent_account_name
        isPrimary: false
        businessName: oce parent account name 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: keyword
        isPrimary: false
        businessName: keyword 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: new_hpscore
        isPrimary: false
        businessName: new hpscore 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: pai_practice_status
        isPrimary: false
        businessName: pai practice status 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: in_oce
        isPrimary: false
        businessName: in oce 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: in_sfdc
        isPrimary: false
        businessName: in sfdc 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: cdp_status
        isPrimary: false
        businessName: cdp status 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: account_name
        isPrimary: false
        businessName: account name 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: dent_suspects
        isPrimary: false
        businessName: dent suspects 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: vet_suspects
        isPrimary: false
        businessName: vet suspects 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: foot_suspects
        isPrimary: false
        businessName: foot suspects 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: practice_source
        isPrimary: false
        businessName: practice source 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: addresstoken
        isPrimary: false
        businessName: addresstoken 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: addresstoken2
        isPrimary: false
        businessName: addresstoken2 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: practicetoken
        isPrimary: false
        businessName: practicetoken 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: urltoken
        isPrimary: false
        businessName: urltoken 
        logicalType: text
        physicalType: VARCHAR(16777216)
        maxLen: null
        isNullable: true
        description: null
        criticalDataElementStatus: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
```

### Definitions

|Key|Required|Description|
| --- | --- | --- | 
|dataset.table|Yes|Name of the table being cataloged; the value should only contain the table name. Do not include the project or dataset name in the value.|
|dataset.sourceTables| Yes | A list of all source tables for the current table.|
|dataset.physicalName|No|Physical name of the table, default value is table name + version separated by underscores, as `table_1_2_0`.|
|dataset.description | Yes | Description of the current table.|
|dataset.tags| No | Words related to the current table and it's main applications.|
|dataset.dataGranularity| Yes | Whether the row has one or many rows per primarily identified object. |
dataset.columns|Yes|Array. A list of columns in the table.|
dataset.columns.isPrimary|No|Boolean value specifying whether the column is primary or not. Default is false.|
dataset.columns.businessName|Yes|A more conversational name for the column. Think about it as changing from  'Data Speak' to 'English'.|
dataset.columns.logicalType|Yes|The logical data type of the column For example, 'varchar' would fit under the type of 'string'.|
dataset.columns.physicalType|Yes|The actual physical column data type. |
dataset.columns.maxLen | No | The max length occuring in the column, or that would be expected to occur in the column under normal conditions. If a value has (fixed) after it, that means the length of that column never deviates from the stated length.
dataset.columns.isNullable|Yes|indicates if the column may contain Null values; possible values are true and false.|
dataset.columns.description| Yes| description of the column. Null if the column name is self-explanatory |
dataset.columns.criticalDataElementStatus|No|True or false indicator; If element is considered a critical data element (CDE) then true else false.|
dataset.columns.tags|No|A list of tags that may be assigned to the dataset, table or column; the tags keyword may appear at any level.|
dataset|Yes|Array. A list of tables within the dataset to be cataloged
dataset.columns.transformSourceTables| No | Source table(s) for the data in this column. Common sources would be OCE and OPUL |
dataset.columns.transformLogic| No | Exact SQL statements performed to get the data in its current state |
dataset.columns.transformDescription| No | Informal Description of Transformation Logic in a more understandable way |
dataset.columns.sampleValues| No | Sample values for the column to help the viewer understand exaclty what it is |
dataset.columns.column|Yes|the name of the column.|

## Stakeholders
This section lists stakeholders and the history of their relation with this data contract.

```YAML
contractStakeholders: 
  - name: David Austin
    email: david.austin@revance.com
    role: Data Innovation Manager
    dateIn: 2023-04-01
    dateOut: null
```

### Definitions

|Key|Required|Description|
| --- | --- | --- |
contractStakeholders|No|Array
contractStakeholders.name|Yes|The stakeholder's first and last name|
contractStakeholders.email|No| The stakeholder's work email|
contractStakeholders.role|No|The stakeholder's job role; Examples might be owner, data steward. There is no limit on the role.|
contractStakeholders.dateIn|No|The date when the user became a stakeholder.|
contractStakeholders.dateOut|No|The date when the user ceased to be a stakeholder|
contractStakeholders.replacedByUsername|No|The username of the user who replaced the stakeholder|

## Roles

This section lists the roles that a consumer may need to access the dataset depending on the type of access they require.

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

### Definitions

|Key|Required|Description|
| --- | --- | --- |
roles|Yes|Array. A list of roles that will provide user access to the dataset.|
roles.role|Yes|name of the IAM role that provides access to the dataset.|
roles.access|Yes|the type of access provided by the IAM role; the value will generally come directly from the "BQ dataset to IAM roles mapping" document.|
roles.firstLevelApprovers|No|the name(s) of the first level approver(s) of the role.|
roles.secondLevelApprovers|No|the name(s) of the second level approver(s) of the role.|
