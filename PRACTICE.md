# Data Contract Pracice
## Executive summary

## Table of content
## Notes
## Demographics
### Example
# What's this data  identification?
datasetDomain: practice
quantumName: practice quantum
userConsumptionMode: Analytical
version: 1.0.0
status: current
uuid: 53581432-6c55-4ba2-a65f-72344a91553a #

# Lots of information
description:
  purpose: Tables and attributes related to Practices.
  limitations: null
  usage: null
tenant: revance

# Getting support
productDl: null
productSlackChannel: null
productFeedbackUrl: null

# Physical parts Snowflake specific
sourcePlatform: snowflake
sourceSystem: snowflake
datasetProject: staging_test # snowflake database
datasetName: cdp # snowflake schema

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

# Data Quality
quality: null # See more information below

# Tags
tags: null

dataset:
  - table: practice master
    physicalName: practicemasterdim # default value is table name + version separated by underscores, as table_1_2_0
    priorTableName: null # if needed
    description: Master dimension of all practices 
    tags: null
    dataGranularity: One row per practice
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

stakeholders:
  - username: ceastwood
    role: Data Scientist
    dateIn: 2022-08-02
    dateOut: 2022-10-01
    replacedByUsername: mhopper

roles:
  - role: datagov_r
    access: read
    firstLevelApprovers: IT
    secondLevelApprovers: null
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

