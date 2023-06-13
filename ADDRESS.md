# ADDRESS Contract Template

## Executive summary
This document describes the keys and values expected in the ADDRESS data contract. It is divided in multiple sections: [demographics](#Demographics), [dataset & schema](#Dataset-&-schema), [pricing](#Pricing), [stakeholders](#Stakeholders), [roles](#Roles), [service-level agreement](#Service-level-agreement), and [other properties](#Other-properties). Each section starts with at least an example followed by definition of each field/key.

## Table of content
* [Demographics](#Demographics)
* [Dataset & schema](#Dataset-&-schema)
* [Stakeholders](#Stakeholders)
* [Roles](#Roles)

## Notes
* This contract is containing example values, we reviewed very carefully the consistency of those values, but we cannot guarantee that there are no errors. If you spot one, please raise an issue(link for raising issue yet to be added)
* Some fields have `null` value: even if it is equivalent to not having the field in the contract, we wanted to have the field for illustration purpose.
* This contract leverages Snowflake but should be **platform agnostic**. If you think it is not the case, please raise an issue.

## Demographics
This section contains general information about the contract.

### Example

```YAML
# What's this data  identification?
datasetDomain: Address # Domain
quantumName: Address quantum # Data product name
userConsumptionMode: Analytical
version: 1.1.0 # Version follows semantic versioning (Are we still using this?)
status: current
uuid: 53581432-6c55-4ba2-a65f-72344a91553a # Yet to be determined

# Lots of information
description:
  purpose: ---
  limitations: null
  usage: null
tenant: paypal

# Getting support
productDl: product-dl@paypal.com
productSlackChannel: '#product-help'
productFeedbackUrl: null

# Physical parts / GCP / BigQuery specific
sourcePlatform: googleCloudPlatform
sourceSystem: bigQuery
datasetProject: edw # BQ dataset
datasetName: access_views # BQ dataset

kind: virtualDataset
type: tables

# Physical access
driver: null
driverVersion: null
server: null
database: pypl-edw.pp_access_views
username: '${env.username}'
password: '${env.password}'
schedulerAppName: name_coming_from_scheduler # NEW 2.1.0 Required if you want to schedule stuff, comes from DataALM.

# Tags
tags: null
```

|Key|UX label|Required|Description|
| --- | --- | --- | --- |
| version|Version|Yes|Current version of the data contract.|
| uuid|Identifier|Yes| A unique identifier used to reduce the risk of dataset name collisions; initially the UUID will be created using a UUID generator tool ([example](https://www.uuidgenerator.net/)). However, we may want to develop a method that accepts a seed value using a combination of fields–such as name, kind and source–to create a repeatable value.|
|username|Username|Yes|User credentials for connecting to the dataset; how the credentials will be stored/passed is outside of the scope of the contract.|
|userConsumptionMode|Consumption mode|No|List of data modes for which the dataset may be used.  Expected sample values might be Analytical or Operational. <br/>Note: in the future, this will probably be replaced by ports.|
|type|Type|Yes|Identifies the types of objects in the dataset.  For BigQuery the expected value would be tables.
tenant|Tenant|No|Indicates the property the data is primarily associated with. Value is case insensitive. For PayPal, the expected sample values might be PayPal, Venmo, PPWC, etc.|
tags|Tags|No|a list of tags that may be assigned to the dataset, table or column; the `tags` keyword may appear at any level.
status|Status|Yes|Current status of the dataset.
sourceSystem|Source system|Yes|The system where the dataset resides.  Expected value is bigQuery
sourcePlatform|Source platform|Yes|The platform where the dataset resides. Expected value is googleCloudPlatform
server|Server|Yes|The server where the dataset resides.|
quantumName|Quantum name|Yes|The name of the data quantum or data product.
productSlackChannel|Support Slack channel|No|Slack channel of the team responsible for maintaining the dataset.
productFeedbackUrl|Feedback URL|No|The URL for submitting feedback to the team responsible for maintaining the dataset.|
productDl|E-mail distribution list|No|The email distribution list (DL) of the persons or team responsible for maintaining the dataset.
password|Password|Yes|User credentials for connecting to the dataset; how the credentials will be stored/passed is out of the scope of this contract.
kind|Kind|Yes|The kind of Rosewall dataset being cataloged; Expected values are `virtualDataset` or `managedDataset`.
driverVersion|Driver version|Yes|The version of the connection driver to be used to connect to the dataset.|
driver|Driver|Yes|The connection driver required to connect to the dataset.|
description.usage|Usage|No|intended usage of the dataset, table, or column (depending on the level); the key may appear at the dataset, table, or column level.|
description.purpose|Purpose|No|Purpose of the dataset, table or column (depending on the level); the key may appear at the dataset, table, or column level.|
description.limitations|Limitations|No|Limitations of the dataset, table or column (depending on the level); the key may appear at the dataset, table, or column level.|
description|N/A|No|Object.|
datasetProject|GCP project|Yes|GCP BigQuery dataset project name.|
datasetName|BigQuery dataset name|Yes|GCP BigQuery dataset name.|
|datasetDomain|Domain dataset|No|Name of the logical domain dataset the contract describes. This field is only required for output data contracts. Examples: `imdb_ds_aggregate`, `receiver_profile_out`,  `transaction_profile_out`.|
database|Database|Yes|The database where the dataset resides.|

## Dataset & schema
This section describes the dataset and the schema of the data contract. It is the support for data quality, which is detailed in the next section.

### Example

```YAML
dataset:
  - table: tbl
    physicalName: tbl_1 # NEW in v2.1.0, Optional, default value is table name + version separated by underscores, as table_1_2_0
    priorTableName: null # if needed
    description: Provides core payment metrics 
    tags: null
    dataGranularity: Aggregation on columns txn_ref_dt, pmt_txn_id
    columns:
      - column: txn_ref_dt
        isPrimary: false # NEW in v2.1.0, Optional, default value is false, indicates whether the column is primary key in the table.
        businessName: transaction reference date
        logicalType: date
        physicalType: date
        isNullable: false
        description: null
        partitionStatus: true
        clusterStatus: false
        criticalDataElementStatus: false
        tags: null
        classification: null
        encryptedColumnName: null
        transformSourceTables:
          - table_name_1
          - table_name_2
          - table_name_3
        transformLogic: sel t1.txn_dt as txn_ref_dt from table_name_1 as t1, table_name_2 as t2, table_name_3 as t3 where t1.txn_dt=date-3
        transformDescription: defines the logic in business terms; logic for dummies
        sampleValues:
          - 2022-10-03
          - 2020-01-28
      - column: rcvr_id
        isPrimary: true # NEW in v2.1.0, Optional, default value is false, indicates whether the column is primary key in the table.
        businessName: receiver id
        logicalType: string
        physicalType: varchar(18)
        isNullable: false
        description: A description for column rcvr_id.
        partitionStatus: false
        clusterStatus: true
        criticalDataElementStatus: false
        tags: null
        classification: null
        encryptedColumnName: null
      - column: rcvr_cntry_code
        isPrimary: false # NEW in v2.1.0, Optional, default value is false, indicates whether the column is primary key in the table.
        businessName: receiver country code
        logicalType: string
        physicalType: varchar(2)
        isNullable: false
        description: null
        partitionStatus: false
        clusterStatus: false
        criticalDataElementStatus: false
        tags: null
        classification: null
        authoritativeDefinitions:
          - url: https://collibra.com/asset/742b358f-71a5-4ab1-bda4-dcdba9418c25
            type: Business definition
          - url: https://github.com/myorg/myrepo
            type: Reference implementation
        encryptedColumnName: rcvr_cntry_code_encrypted
```

### Definitions

|Key|UX label|Required|Description|
| --- | --- | --- | --- | 
dataset||Yes|Array. A list of tables within the dataset to be cataloged
dataset.table||Yes|Name of the table being cataloged; the value should only contain the table name. Do not include the project or dataset name in the value.
dataset.physicalName||No|Physical name of the table, default value is table name + version separated by underscores, as `table_1_2_0`.|
dataset.priorTableName||Yes|Name of the previous version of the dataset.|
dataset.dataGranularity||No|Granular level of the data in the table. Example would be `pmt_txn_id`.|
dataset.columns||Yes|Array. A list of columns in the table.|
dataset.columns.column||Yes|the name of the column.|
dataset.columns.isPrimaryKey||No|Boolean value specifying whether the column is primary or not. Default is false.|
dataset.columns.businessName||Yes|the business name of the column.|
dataset.columns.logicalType||Yes|the logical column datatype.|
dataset.columns.physicalType||Yes|the physical column datatype.|
dataset.columns.isNullable||Yes|indicates if the column may contain Null values; possible values are true and false.|
dataset.columns.partitionStatus||Yes|indicates if the column is partitioned; possible values are true and false.|
dataset.columns.clusterStatus||Yes|indicates of the column is clustered; possible values are true and false.|
dataset.columns.classification||Yes|the PayPal data classification indicating the class of data in the column; expected values are 1, 2, 3, 4, or 5.|
|dataset.columns.authoritativeDefinitions||No|list of links to sources that provide more detail on column logic or values; examples would be URL to a GitHub repo, Collibra, on another tool.|
dataset.columns.encryptedColumnName||Yes|The column name within the table that contains the encrypted column value. For example, unencrypted column `email_address` might have an encryptedColumnName of `email_address_encrypt`.
dataset.columns.transformSourceTables||No|List of sources used in column transformation.|
dataset.columns.transformLogic||No|Logic used in the column transformation.|
dataset.columns.transformDescription||No|Describes the transform logic in very simple terms.|
dataset.columns.sampleValues||No|List of sample column values.|
dataset.columns.criticalDataElementStatus||No|True or false indicator; If element is considered a critical data element (CDE) then true else false.|
dataset.columns.tags||No|A list of tags that may be assigned to the dataset, table or column; the tags keyword may appear at any level.|

## Stakeholders
This section lists stakeholders and the history of their relation with this data contract.

### Example
```YAML
stakeholders:
  - username: ceastwood
    role: Data Scientist
    dateIn: 2022-08-02
    dateOut: 2022-10-01
    replacedByUsername: mhopper
  - username: mhopper
    role: Data Scientist
    dateIn: 2022-10-01
    dateOut: null
    replacedByUsername: null
  - username: daustin
    role: Owner
    comment: Keeper of the grail
    dateIn: 2022-10-01
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

### Example

```YAML
roles:
  - role: microstrategy_user_opr
    access: read
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: 'mandolorian'
  - role: bq_queryman_user_opr
    access: read
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: na
  - role: risk_data_access_opr
    access: read
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: 'dathvador'
  - role: bq_unica_user_opr
    access: write
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: 'mickey'
```

### Definitions

|Key|UX label|Required|Description|
| --- | --- | --- | --- |
roles||Yes|Array. A list of roles that will provide user access to the dataset.|
roles.role||Yes|name of the IAM role that provides access to the dataset; the value will generally come directly from the "BQ dataset to IAM roles mapping" document.|
roles.access||Yes|the type of access provided by the IAM role; the value will generally come directly from the "BQ dataset to IAM roles mapping" document.|
roles.firstLevelApprovers||No|the name(s) of the first level approver(s) of the role; the value will generally come directly from the "BQ dataset to IAM roles mapping" document.|
roles.secondLevelApprovers||No|the name(s) of the second level approver(s) of the role; the value will generally come directly from the "BQ dataset to IAM roles mapping" document.|
