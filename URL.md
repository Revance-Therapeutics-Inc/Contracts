# URL Data Contract
### Last Edited By: [Jordan Hasulube](https://www.linkedin.com/in/jordan-hasulube-426814236) - Data Decisioning Intern

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
* This contract describes the keys and values expected in the URL data contract. It is divided in multiple sections: Metadata, Dataset & Schema, Stakeholders, Roles, Concequences, and Automation. Each section contains a [YAML](https://www.redhat.com/en/topics/automation/what-is-yaml) file followed by definitions for its keys.

## Metadata
This section contains general information about this Data Contract.

```YAML
# URL MASTER
domain: url
domainOwner: Senthil Selvaraj
domainOwnerEmail: senthil.salvaraj@revance.com
partionedOn: URL
quantumName: url quantum
usagePurpose: Inventory; Analytical
version: 0.0.1
status: current
uniqueContractId: 25da803a-9bad-4caf-bd28-1318d57af812
activeDate: null
nextReassessmentDate: null

# Contract Description
description:
  purpose: Tables and attributes related to URLs. Urls are tools for marketing used by only a subset of practices. Some use multiple urls. #this goes over the purpose of urls, not of this contract
  limitations: Financial Reporting; Any other uses that require  1 on 1 accuracy, since one practice can have many urls.
tenant: Revance

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
tags: link, website, web address, web page, page, hyperlink
```

|Key|Required|Description|
| --- | --- | --- |
|domain| Yes | The domain that the current contract is responsible for describing.|
|domainOwner| Yes | The owner of the current domain. Person responsible for the accuracy and continuity of the contract.|
| domainOwnerEmail | Yes | The email of the person who owns the domain |
| partitionedOn | No | The column of the master table that its rows were partitioned on.|
| quantumName | No | Name given to the quantum by George Earl. |
| usagePurpose | No | Description of what kind of tasks this domain may be used for. |
| version|Yes|Current version of the data contract. Uses semantic versioning.|
status|Yes|Current status of the dataset. Example value would be current. |
| uniqueContractId |Yes| A unique identifier used to reduce the risk of dataset name collisions; version 4 uuid generated from [this URL](https://www.uuidgenerator.net/version1)|
|activeDate| Yes | The date that this contract becomes active.|
| nextReassessmentDate | No | The next date that the contract will be reassessed.|
description.purpose|No|Purpose of the dataset, table or column (depending on the level); the key may appear at the dataset, table, or column level.|
description.limitations|No|Limitations of the dataset, table or column (depending on the level); the key may appear at the dataset, table, or column level.|
description|No|Object. Holds purpose and limitations attributes for this data contract. |
tenant|No|Indicates the property the data is primarily associated with. Value is case insensitive.|
|teamSypportDl | No | Email Distribution List where you can request for support. Not set up as of July 2023.|
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

## Dataset and Schema
This section describes the dataset and the schema of the data contract.

```YAML
dataset:
  - table: url master, tables organized top down
    sourceTables:
      - STITCH_DEV.CDPSTAGE.URL_MASTER_STG
      - STITCH_DEV.CDPRAW.URL_MASTER_RAW
      - STAGING_DEV.SALES.VW_ACCOUNT
      - STAGING_DEV.OPUL_CRM.ACCOUNT
      - STITCH_DEV.CDPRAW.PAI_GOOGLEMAPS_RAW
      - STITCH_DEV.CDPRAW.PAI_YELP_RAW
      - STITCH_DEV.CDPRAW.PAI_CARECREDIT_RAW
      - STITCH_DEV.CDPRAW.PAI_REALSELF_RAW
      - STITCH_DEV.CDPRAW.FINDURL_CARECREDIT
      - STITCH_DEV.CDPRAW.PAI_NO_URLS_FACEBOOK
      - STITCH_DEV.CDPRAW.FINDURL_NPI_APRIL
      - STITCH_DEV.CDPRAW.FINDURL_YELP
      - STITCH_DEV.CDPRAW.PAI_LINKEDIN_CO_SEARCH_RAW
      - STITCH_DEV.CDPRAW.PAI_LINKEDIN_CO_WEB_RAW
      - STITCH_DEV.CDPRAW.PAI_LINKEDIN_CO_WKEXP_RAW
      - STITCH_DEV.CDPRAW.PAI_INSTAGRAM_RAW
      - STITCH_DEV.CDPRAW.PAI_WEBPAGE_RAW
      - STITCH_DEV.CDPRAW.PAI_WEBSCRAPING_RAW
      - STITCH_DEV.CDPRAW.PAI_AESTHETICSOCIETY_RAW
    physicalName: STAGING_DEV.CDP.URL_MASTER 
    description: Master dimension of all urls
    tags: null
    dataGranularity: One row per url
    columns:
      - column: url_key
        isPrimary: true
        businessName: url primary identifier
        logicalType: string
        physicalType: VARCHAR(16777216)
        maxLen: 11 (fixed)
        isNullable: false
        description: identifies a distinct url.  used to join with other dimension and fact tables already having url_key
        criticalDataElementStatus: identifies the unique url
        tags: null
        transformSourceTables:
          - STITCH_DEV.CDPSTAGE.URL_MASTER_STG
          - STAGING_DEV.CDP.URL_MASTER
        transformLogic: autogenerated incremental numbers
        transformDescription: incremental number values autogenerated in STITCH_DEV.CDPSTAGE.URL_MASTER_STG and formatted in STAGING_DEV.CDP.URL_MASTER
        sampleValues: URL10978798, URL10978799
      - column: url
        isPrimary: false
        businessName: url
        logicalType: string
        physicalType: VARCHAR(16777216)
        maxLen: 173
        isNullable: false
        description: cleaned up website to hold only its respective url value
        criticalDataElementStatus: actual url dimension of a website
        tags: null
        transformSourceTables: sourced from all of the raw tables mentioned in the table list
        transformLogic:
          - unique urls are sorted and populated into STITCH_DEV.CDPRAW.URL_MASTER_RAW
          - deduped per url granularity is populated into STITCH_DEV.CDPSTAGE.URL_MASTER_STG
          - post url_key value generation populated into the final table STAGING_DEV.CDP.URL_MASTER
        transformDescription: Hygiene applied to the sourced websites
        sampleValues: fantybeautywellness.com, aibypolly.com, vivereaesthetics.com
      - column: domain
        isPrimary: false
        businessName: url domain name
        logicalType: string
        physicalType: VARCHAR(16777216)
        maxLen: 69
        isNullable: false
        description: for populated url, domain value is derived to populate this column
        criticalDataElementStatus: domain value of the respective website is hygiened which will be used as a lookup to related tables
        tags: null
        transformSourceTables: sourced from all of the raw tables mentioned in the table list   --Does this have to be a list???
        transformLogic:
          - domains derived from unique urls populated into STITCH_DEV.CDPSTAGE.URL_MASTER_STG
          - post url_key value generation populated into the final table STAGING_DEV.CDP.URL_MASTER
        transformDescription: Hygiene applied to the derived domain values
        sampleValues: fantybeautywellness, aibypolly, vivereaesthetics
      - column: hp_score
        isPrimary: false
        businessName: business score 
        logicalType: string
        physicalType: VARCHAR(16777216)
        maxLen: 5
        isNullable: false
        description: business score to identify how reliable the website to refer to as a practice.
        criticalDataElementStatus: true
        tags: null
        transformSourceTables: sourced from all of the raw tables mentioned in the table list
        transformLogic: derived based of score distribution as of current iteration any score greater than equal to 20 is defined as a practice                        
        transformDescription: derived value based of predefined algorithm
        sampleValues: 48.56, 36.56, 37.96
      - column: url_status
        isPrimary: false
        businessName: url status
        logicalType: string
        physicalType: VARCHAR(16777216)
        maxLen: 2
        isNullable: false
        description: segmenting url based of the score
        criticalDataElementStatus: essential to segment urls
        tags: null
        transformSourceTables: STITCH_DEV.CDPSTAGE.URL_MASTER_STG
        transformLogic:
          - if HP_SCORE is >= 20 then 2
          - if Practice Source is from OCE or OPUL then 1
          - if HP_SCORE is between 0 AND 19.99 THEN 0
          - if HP_SCORE = -1 then -1; it represents connection error
          - for all other exceptions like Invalid Domain etc.. the value is assigned as -2
        transformDescription: urls are segmented based of the scores generated by pre-defined algorithm
        sampleValues: 2, 1, 0, -1, -2
      - column: load_date
        isPrimary: false
        businessName: load date when the url is populated into the table
        logicalType: string
        physicalType: VARCHAR(16777216)
        maxLen: 
        isNullable: false
        description: identifies when the url is populated into the final table STAGING_DEV.CDP.URL_MASTER
        criticalDataElementStatus: identifies when the url load process got completed successfully
        tags: null
        transformSourceTables: STAGING_DEV.CDP.URL_MASTER
        transformLogic: autogenerated for every run
        transformDescription: date of successful completion of the url process
        sampleValues: 2023-07-11 08:58:09.627
      - column: modified_date
        isPrimary: false
        businessName: modified date
        logicalType: string
        physicalType: VARCHAR(16777216)
        maxLen: 
        isNullable: true
        description: 'date the url was modified(if not modified, default to null)'
        criticalDataElementStatus: null
        tags: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: when a url value is modified the column gets updated
        sampleValues: 2023-08-11 08:58:09.627
  - table: url master view
    sourceTables: STAGING_DEV.CDP.URL_MASTER
    physicalName: STAGING_DEV.CDP.VW_URL_MASTER
    description: view for url master containing url, domain, and hp_score
    tags: view
    dataGranularity: one row per URL
    columns:
      - column: url
        isPrimary: false
        businessName: business url
        logicalType: string
        physicalType: VARCHAR(16777216)
        maxLen: 
        isNullable: false
        description: null
        criticalDataElementStatus: true
        tags: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: domain
        isPrimary: false
        businessName: url domain name
        logicalType: string
        physicalType: VARCHAR(16777216)
        maxLen: 
        isNullable: false
        description: the url without the web extention on the end
        criticalDataElementStatus: false
        tags: null
        transformSourceTables: null
        transformLogic: null
        transformDescription: null
        sampleValues: null
      - column: hp_score
        isPrimary: false
        businessName: url score
        logicalType: string
        physicalType: VARCHAR(16777216)
        maxLen: 
        isNullable: false
        description: business score to identify how reliable the website to refer to as a practice.
        criticalDataElementStatus: true
        tags: null
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
dataset.columns.maxLen | No | The max length occuring in the column, or that would be expected to occur in the column under normal conditions
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
    dateIn: 2023-04-10
    dateOut: null
    replacedByUsername: null
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
