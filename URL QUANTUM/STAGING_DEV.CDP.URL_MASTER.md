# URL Data Contract
### Last Edited By: [Jordan Hasulube](https://www.linkedin.com/in/jordan-hasulube-426814236) - Data Decisioning Intern

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
uniqueContractId: 7e47d4aa-2023-11ee-be56-0242ac120002
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
dataset.columns.isPrimary|No|Boolean value specifying whether the column is primary or not. Default is false.|
dataset.columns.businessName|Yes|A more conversational name for the column. Think about it as changing from  'Data Speak' to 'English'.|
dataset.columns.logicalType|Yes|The logical data type of the column For example, 'varchar' would fit under the type of 'string'.|
dataset.columns.physicalType|Yes|The actual physical column data type. |
dataset.columns.maxLen | No | The max length occuring in the column at the time the field was filled out. A "(fixed)" next to the value means that the length of the string in this column never drops below or exeeds the maxLen value.
dataset.columns.isNullable|Yes|indicates if the column may contain Null values; possible values are true and false.|
dataset.columns.description| Yes| description of the column. Null if the column name is self-explanatory |
dataset.columns.criticalDataElementStatus|No|True or false indicator; If element is considered a critical data element (CDE) then true else false.|
dataset.columns.tags|No|A list of tags that may be assigned to the dataset, table or column; the tags keyword may appear at any level.|
dataset|Yes|Array. A list of tables within the dataset to be cataloged
dataset.columns.transformSourceTables| No | Source table(s) for the data in this column. Common sources would be OCE and OPUL |
dataset.columns.transformLogic| No | Exact SQL statements performed to get the data in its current state |
dataset.columns.transformDescription| No | Informal Description of Transformation Logic in a more understandable way |
dataset.columns.sampleValues| No | Sample values for the column to help the viewer understand exaclty what it is |
dataset.table|Yes|Name of the table being cataloged; the value should only contain the table name. Do not include the project or dataset name in the value.
dataset.physicalName|No|Physical name of the table, default value is table name + version separated by underscores, as `table_1_2_0`.|
dataset.columns||Yes|Array. A list of columns in the table.|
dataset.columns.column|Yes|the name of the column.|

## Dataset and Schema
This section describes the dataset and the schema of the data contract.

```YAML
dataset:
  - table:          1.  STAGING_DEV.CDP.URL_MASTER

                    Built based of the below listed tables:
                    2.  STITCH_DEV.CDPSTAGE.URL_MASTER_STG
                    3.  STITCH_DEV.CDPRAW.URL_MASTER_RAW
                    4.  STAGING_DEV.SALES.VW_ACCOUNT
                    5.  STAGING_DEV.OPUL_CRM.ACCOUNT
                    6.  STITCH_DEV.CDPRAW.PAI_GOOGLEMAPS_RAW
                    7.  STITCH_DEV.CDPRAW.PAI_YELP_RAW
                    8.  STITCH_DEV.CDPRAW.PAI_CARECREDIT_RAW
                    9.  STITCH_DEV.CDPRAW.PAI_REALSELF_RAW
                   10. STITCH_DEV.CDPRAW.FINDURL_CARECREDIT
                   11. STITCH_DEV.CDPRAW.PAI_NO_URLS_FACEBOOK
                   12. STITCH_DEV.CDPRAW.FINDURL_NPI_APRIL
                   13. STITCH_DEV.CDPRAW.FINDURL_YELP
                   14. STITCH_DEV.CDPRAW.PAI_LINKEDIN_CO_SEARCH_RAW
                   15. STITCH_DEV.CDPRAW.PAI_LINKEDIN_CO_WEB_RAW
                   16. STITCH_DEV.CDPRAW.PAI_LINKEDIN_CO_WKEXP_RAW
                   17. STITCH_DEV.CDPRAW.PAI_INSTAGRAM_RAW
                   18. STITCH_DEV.CDPRAW.PAI_WEBPAGE_RAW
                   19. STITCH_DEV.CDPRAW.PAI_WEBSCRAPING_RAW
                   20. STITCH_DEV.CDPRAW.PAI_AESTHETICSOCIETY_RAW

    physicalName:  STAGING_DEV.CDP.URL_MASTER 
 
    priorTableName: null
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
        transformSourceTables: STITCH_DEV.CDPSTAGE.URL_MASTER_STG and STAGING_DEV.CDP.URL_MASTER
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
        transformLogic: 1. unique urls are sorted and populated into STITCH_DEV.CDPRAW.URL_MASTER_RAW
                        2. deduped per url granularity is populated into STITCH_DEV.CDPSTAGE.URL_MASTER_STG
                        3. post url_key value generation populated into the final table STAGING_DEV.CDP.URL_MASTER
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
        transformSourceTables: sourced from all of the raw tables mentioned in the table list
        transformLogic: 1. domains derived from unique urls populated into STITCH_DEV.CDPSTAGE.URL_MASTER_STG
                        2. post url_key value generation populated into the final table STAGING_DEV.CDP.URL_MASTER
        transformDescription: Hygiene applied to the derived domain values
        sampleValues: fantybeautywellness, aibypolly, vivereaesthetics
      - column: hp_score
        isPrimary: false
        businessName: business score to identify how reliable the website to refer to as a practice
        logicalType: string
        physicalType: VARCHAR(16777216)
        maxLen: 5
        isNullable: false
        description: using pre-defined algorithm, the business score is assigned with respect to each of the urls
        criticalDataElementStatus: based of the score the url is identified if it is a practice or not
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
        transformLogic: derived value that defines the segment a url will be placed
                        2 -> HP_SCORE is >= 20 then 2
                        1 -> if Practice Source is from OCE or OPUL then 1
                        0 -> if HP_SCORE is between 0 AND 19.99 THEN 0
                       -1 -> if HP_SCORE = -1 then -1; it represents connection error
                       -2 -> for all other exceptions like Invalid Domain etc.. the value is assigned as -2
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
```

### Definitions

|Key|Required|Description|
| --- | --- | --- | 
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
dataset.table|Yes|Name of the table being cataloged; the value should only contain the table name. Do not include the project or dataset name in the value.
dataset.physicalName|No|Physical name of the table, default value is table name + version separated by underscores, as `table_1_2_0`.|
dataset.columns||Yes|Array. A list of columns in the table.|
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
