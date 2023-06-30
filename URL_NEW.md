# URL Data Contract
### Last Edited (dd/mm/yyyy):  06/30/2023
### By: Jordan Hasulube - Data Decisioning Intern

## Table of Contents
* Summary
* Metadata
* Dataset-&-Schema

## Summary

### What is _a data contract_?
* A data contract is a formal agreement between two parties (data product provider and data product consumer).
It specifies the guarantees about a provided data set and expectations concerning data product access.

### This Contract
* This contract describes the keys and values expected in the URL data contract. It is divided in multiple sections. Each section contains a [YAML](https://www.redhat.com/en/topics/automation/what-is-yaml) file followed by definitions for its keys.

## Metadata

* Domain name
* Domain owner
* Data product consumer
  * Responsible consumer contact details
* Purpose
* Output port
  * Technology (files, tables, topics)
  * Format (Parquet, Delta, JSON, ...)
  * Global address
* Schema
  * Field names and types
  * Primary and foreign keys
  * Partitions
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
* Security
  * The IAM role definition to grant
* Costs and Billing
* Contract duration
  * Start date
  * Notice period and end date
  * Next reassessment date
 
  ```YAML
field: value
  ```

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
