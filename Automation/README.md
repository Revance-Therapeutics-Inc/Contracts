# Automation

## Overview

## createmeta.py
This python program was made to create the Dataset and Schema portion of the Data Contracts. It is now completely contained within createcontract.py, so there is really no need to use this program anymore. It is mostly kept for documentation purposes. Instructions on how to use this file to create that section of the Data contracts is found within the file itself in comments.

## createmarkdowncontract.py
This program is where the magic happens. It is an interactive program that walks you through the process of creating a data contract and asks you questions about certain fields as you go. Certain fields, like "transformation logic" and "description" in the DataSet and Schema section are still not able to be filled out though, since these are not documented anywhere else and must be filled out manually for the time being. However, this program will build you most of what you need for your Data contract. Instructions on how to use it are once again found in the file itself via comments.

## createcontract.py

This program is very similar to createmarkdowncontract.py, however this one only creates the imbedded yaml files for the data contract.

## findmaxlen.py

This program takes a table from the informational schema in snowflake and creates a query to find the maximum lengths for all columns of a specific table. To get the table from the informational schema, you need to run *SELECT* * *FROM* *[DATABASE].INFORMATIONAL_SCHEMA.COLUMNS* *WHERE* *TABLE_NAME* = *'[TABLE NAME]'* and download results into the same folder as the automation program.
