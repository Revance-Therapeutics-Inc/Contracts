import csv
import string

incomplete = []

#PUT YOUR OUTTPUT FILE HERE
outputFile = open('dc.txt', 'w')

try:
    master = input('REQUIRED: What is the filename for the master table of this domain? Make sure you are using a .csv file. ')
    if master[master.index('.'):] != '.csv':
        #Throw error
        x = 7
    else:
        inputFile = open(master, 'r')
except:
    print("Try again!")
    master = input('REQUIRED: What is the filename for the master table of this domain? Make sure you are using a .csv file. ')
    inputFile = open(master, 'r')
#REMEMBER TO MAKE THIS TABLE ADD AUTOMATICALLY

csvReader = csv.reader(inputFile)
next(csvReader)


domain = input('REQUIRED: What Domain is this? ')
outputFile.write('# ' + domain.capitalize() + ' Data Contract\n')
outputFile.write('### By: [Jordan Hasulube](https://www.linkedin.com/in/jordan-hasulube-426814236) - Data Decisioning Intern\n\n## Table of Contents\n* [Summary](#Summary)\n* [Metadata](#Metadata)\n* [Dataset and Schema](#Dataset-and-Schema)\n* [Stakeholders](#Stakeholders)\n* [Roles](#Roles)\n\n## Summary\n\n### What is _a data contract_?\n* A data contract is a formal agreement between two parties (data product provider and data product consumer).\nIt specifies the guarantees about a provided data set and expectations concerning data product access.\n\n### This Contract\n* This contract describes the keys and values expected in the ' + domain.upper() + ' data contract. It is divided in multiple sections: Metadata, Dataset & Schema, Stakeholders, Roles, Concequences, and Automation. Each section contains a [YAML](https://www.redhat.com/en/topics/automation/what-is-yaml) file followed by definitions for its keys.\n\n## Metadata\nThis section contains general information about this Data Contract.\n\n```YAML\n# ' + domain.upper() + ' MASTER\n')
outputFile.write("domain: " + domain.upper() + '\n')
domainOwner = input('REQUIRED: Who owns this domain(First Name Last Name)? ')
domainOwner = string.capwords(domainOwner)
outputFile.write('domainOwner: ' + domainOwner + '\n')
outputFile.write('domainOwnerEmail: ' + domainOwner[:domainOwner.index(' ')].lower() + '.' + domainOwner[domainOwner.index(' ') + 1:].lower() + '@revance.com\n')
partitionedOn = input('What field is this domain partitioned on? If you do not know, hit the Enter key. ')
outputFile.write('partitionedOn: ')
if partitionedOn == '':
    outputFile.write('null\n')
    incomplete.append('partitionedOn')
else:
    outputFile.write(partitionedOn.upper() + '\n')
outputFile.write('quantumName: ' + domain.lower() + ' quantum\n')
outputFile.write('usagePurpose: null\n') ##update this later!!
description = input('Define the primary data in this domain as it relates to Revance and our uses for it. To skip, hit the Enter key. ')
if description == '':
    outputFile.write('description: null\n')
    incomplete.append('contractDescription')
else:
    outputFile.write('description: ' + description + '\n')
limitations = input('What are the limitations on the use of the data in this domain? To skip, hit the Enter key. ')
if limitations == '':
    outputFile.write('limitations: null\n')
else: 
    outputFile.write('limitations: ' + limitations + '\n')
outputFile.write('version: 0.0.1\n')
outputFile.write('status: current\n')
uniqueContractID = input('REQUIRED: What is the unique contract ID? Generate a version 4 UUID from https://www.uuidgenerator.net/version4 ')
outputFile.write('uniqueContractID: ' + uniqueContractID + '\n')
outputFile.write('activeDate: null\nnextReassessmentDate: null\n')
outputFile.write('tenant: Revance\n\n# Getting support\nteamSupportDl: dl.dd@revance.com\nteamSupportSlackChannel: null\n\n# Physical parts\nsourcePlatform: snowflake\nsourceSystem: snowflake\n\nkind: virtualDataset\ntype: tables\n\n# Physical access\n')
for line in csvReader:
    database = line[0]
    schema = line[1]
    break
outputFile.write('database: ' + database + '\nschema: ' + schema + '\n')
outputFile.write('\n# Tags\ntags: null\n```\n\n|Key|Required|Description|\n| --- | --- | --- |\n|domain| Yes | The domain that the current contract is responsible for describing.|\n|domainOwner| Yes | The owner of the current domain. Person responsible for the accuracy and continuity of the contract.|\n| domainOwnerEmail | Yes | The email of the person who owns the domain |\n| partitionedOn | No | The column of the master table that its rows were partitioned on.|\n| quantumName | No | Name given to the quantum by George Earl. |\n| usagePurpose | No | Description of what kind of tasks this domain may be used for. |\n| description | Yes | Description of the domain and the nature of the data it holds|\n| limitations | Yes| Description of areas that the data from this quantum cannot be used in |\n| version|Yes|Current version of the data contract. Uses semantic versioning.|\nstatus|Yes|Current status of the dataset. Example value would be current. |\n| uniqueContractId |Yes| A unique identifier used to reduce the risk of dataset name collisions; version 4 uuid generated from [this URL](https://www.uuidgenerator.net/version1)|\n|activeDate| Yes | The date that this contract becomes active.|\n| nextReassessmentDate | No | The next date that the contract will be reassessed.|\ntenant|No|Indicates the property the data is primarily associated with. Value is case insensitive.|\n|teamSypportDl | No | Email Distribution List where you can request for support.|\n|teamSupportSlackChannel | No | Slack channel where you can reach out to for support. Not set up as of July 2023. |\npointOfContact| Yes | an array containing points of contact using name and email. |\npointOfContact.name|No|Name of employee to reach in order to inquire about the contract.\npointOfContact.email| Yes | Email related to the employee whos name occupies the pointOfContactName field.\nsourcePlatform|Yes|The platform where the dataset resides.\nsourceSystem|Yes|The system where the dataset resides. Example values are Snowflake and BigQuery|\nkind|Yes|The kind of Rosewall dataset being cataloged; Expected values are`virtualDataset`or`managedDataset`.\n|type|Yes|Identifies the types of objects in the dataset. For Snowflake the expected value would betables.\ndatabase|Yes|Database in which the target table resides.|\nschema|Yes|The schema in Snowflake where the dataSet takes place.|\nschedulerAppName| No | scheduler application used for this database |\ntags|No|a list of tags that may be assigned to the dataset, table or column; the `tags` keyword may appear at any level.\n\n## Dataset and Schema\nThis section describes the dataset and the schema of the data contract.\n\n```YAML\n')
inputFile.close()

print('We are now on the DataSet and Schema section of the Data Contract.\n')
k = 0
addTable = 'Y'
while True:
  if addTable.upper() == 'N':
      break
  elif addTable.upper() == 'Y':
      if k == 0:
        tableName = master
      elif k > 0:
        tableName = input("What table would you like to add(enter file name with .csv extention)? hit the Enter key to cancel. ")
      if tableName == '':
          break
      try:
        with open(tableName, 'r') as csvFile:
            csvReader = csv.reader(csvFile)

            next(csvReader) #skip past the column names
            i = 0
            stringList = []
            stringMap = {} #used to order the rows based on ORIGINAL_POSTITION in snowflake.
            for line in csvReader:
                if i == 0:
                    tableName = line[2].lower().split('_')
                    tableString = ''
                    for t in tableName:
                        tableString += t
                        tableString += ' '
                    outputFile.write('  - table: ' + tableString + '\n')
                    outputFile.write('    sourceTables: null\n')
                    outputFile.write('    physicalName: ' + line[0] + '.' + line[1] + '.' + line[2] + '\n')
                    outputFile.write('    priorTableName: null\n')
                    if tableName[0] == 'vw':
                        outputFile.write('    description: master dimension of all ' + tableName[1] + 's\n')
                    else:
                        outputFile.write('    description: master dimension of all ' + tableName[0] + 's\n')
                    outputFile.write('    tags: null\n')
                    if tableName[0] == 'vw':
                        outputFile.write('    dataGranularity: One row per ' + tableName[1] + '\n')
                    else:
                        outputFile.write('    dataGranularity: One row per ' + tableName[0] + '\n')
                    outputFile.write('    columns:\n')
                stringList.append('') 
                stringList[i] += '      - column: ' + line[3].lower() + '\n'
                if str(line[4]) == '1':
                    stringList[i] += '        isPrimary: true\n'
                else:
                    stringList[i] += '        isPrimary: false\n'
                businessName = str(line[3]).lower().split('_')
                stringList[i] += '        businessName: '
                for s in businessName:
                    stringList[i] += s + ' '
                stringList[i] += '\n'
                stringList[i] += '        logicalType: ' + str(line[7]).lower() + '\n'
                stringList[i] += '        physicalType: '
                if str(line[7]) == 'TEXT':
                    stringList[i] += 'VARCHAR(' + str(line[8]) + ')\n'
                elif str(line[7] == 'NUMBER'):
                    stringList[i] += 'NUMBER('
                    if str(line[8]) == '':
                        stringList[i] += '1'
                    else:
                        stringList[i] += str(line[8])
                    stringList[i] += ',0)\n'
                elif str(line[7] == 'BOOLEAN\n'):
                    stringList += str(line[7])
                else:
                    stringList += 'UNKNOWN\n'
                stringList[i] += '        maxLen: null\n'
                stringList[i] += '        isNullable: '
                if str(line[6]) == 'NO' or str(line[4]) == '1':
                    stringList[i] += 'false'
                else:
                    stringList[i] += 'true'
                stringList[i] += '\n'
                stringList[i] += '        description: null\n'
                stringList[i] += '        criticalDataElementStatus: null\n'
                stringList[i] += '        transformSourceTables: null\n'
                stringList[i] += '        transformLogic: null\n'
                stringList[i] += '        transformDescription: null\n'
                stringList[i] += '        sampleValues: null\n'
                stringMap[int(line[4])] = stringList[i]
                i += 1
        csvFile.close()
        stringList.sort()
        for j in range(i):
            outputFile.write(stringMap[j+1])
        k += 1
        addTable = input('REQUIRED: Would you like to add another table(Y/N)? ' + str(k) + ' added so far.')
      except:
          print('Invalid file name!\n')
  else:
      addTable = input('Invalid input. Enter Y or N. Would you like to add a table? ' + str(k) + ' added so far.')
outputFile.write('```\n\n### Definitions\n\n|Key|Required|Description|\n| --- | --- | --- | \n|dataset.table|Yes|Name of the table being cataloged; the value should only contain the table name. Do not include the project or dataset name in the value.|\n|dataset.sourceTables| Yes | A list of all source tables for the current table.|\n|dataset.physicalName|No|Physical name of the table, default value is table name + version separated by underscores, as `table_1_2_0`.|\n|dataset.description | Yes | Description of the current table.|\n|dataset.tags| No | Words related to the current table and it\'s main applications.|\n|dataset.dataGranularity| Yes | Whether the row has one or many rows per primarily identified object. |\ndataset.columns|Yes|Array. A list of columns in the table.|\ndataset.columns.isPrimary|No|Boolean value specifying whether the column is primary or not. Default is false.|\ndataset.columns.businessName|Yes|A more conversational name for the column. Think about it as changing from  \'Data Speak\' to \'English\'.|\ndataset.columns.logicalType|Yes|The logical data type of the column For example, \'varchar\' would fit under the type of \'string\'.|\ndataset.columns.physicalType|Yes|The actual physical column data type. |\ndataset.columns.maxLen | No | The max length occuring in the column, or that would be expected to occur in the column under normal conditions. If a value has (fixed) after it, that means the length of that column never deviates from the stated length.\ndataset.columns.isNullable|Yes|indicates if the column may contain Null values; possible values are true and false.|\ndataset.columns.description| Yes| description of the column. Null if the column name is self-explanatory |\ndataset.columns.criticalDataElementStatus|No|True or false indicator; If element is considered a critical data element (CDE) then true else false.|\ndataset.columns.tags|No|A list of tags that may be assigned to the dataset, table or column; the tags keyword may appear at any level.|\ndataset|Yes|Array. A list of tables within the dataset to be cataloged\ndataset.columns.transformSourceTables| No | Source table(s) for the data in this column. Common sources would be OCE and OPUL |\ndataset.columns.transformLogic| No | Exact SQL statements performed to get the data in its current state |\ndataset.columns.transformDescription| No | Informal Description of Transformation Logic in a more understandable way |\ndataset.columns.sampleValues| No | Sample values for the column to help the viewer understand exaclty what it is |\ndataset.columns.column|Yes|the name of the column.|\n\n## Stakeholders\nThis section lists stakeholders and the history of their relation with this data contract.\n\n```YAML\ncontractStakeholders: \n')
while True:
  addStakeholder = input('Add a contract stakeholder(Y/N)? ')
  if addStakeholder.upper() == 'N':
      break
  elif addStakeholder.upper() == 'Y':
      name = input("What is their name(First Name Last Name)? ")
      name = string.capwords(name)
      role = input("What is their role? To skip, hit the Enter key. ")
      if role == '':
          role = 'null'
      dateIn = input('What date were they assigned this role(YYYY-MM-DD)? To skip, hit the Enter key. ')
      if dateIn == '':
          dateIn = 'null'
      outputFile.write('  - name: ' + name + '\n    email: ' + name[:name.index(' ')].lower() + '.' + name[name.index(' ') + 1:].lower() + '@revance.com\n    role: ' + role + '\n    dateIn: ' + dateIn + '\n    dateOut: null\n')
  else:
      print('Invalid Input!\n')
outputFile.write('```\n\n### Definitions\n\n|Key|Required|Description|\n| --- | --- | --- |\ncontractStakeholders|No|Array\ncontractStakeholders.name|Yes|The stakeholder\'s first and last name|\ncontractStakeholders.email|No| The stakeholder\'s work email|\ncontractStakeholders.role|No|The stakeholder\'s job role; Examples might be owner, data steward. There is no limit on the role.|\ncontractStakeholders.dateIn|No|The date when the user became a stakeholder.|\ncontractStakeholders.dateOut|No|The date when the user ceased to be a stakeholder|\ncontractStakeholders.replacedByUsername|No|The username of the user who replaced the stakeholder|\n\n## Roles\n\nThis section lists the roles that a consumer may need to access the dataset depending on the type of access they require.\n\n```YAML\n- role: datagov_r\n  access: read only\n  approvers:\n    - name: IT\n      approvalLevel: 1\n- role: datagov_rw\n  access: read and write\n  approvers:\n    - name: Senthil Salvaraj\n      approvalLevel: 1\n    - name: Parker Hanna\n      approvalLevel: 1\n```\n\n### Definitions\n\n|Key|Required|Description|\n| --- | --- | --- |\nroles|Yes|Array. A list of roles that will provide user access to the dataset.|\nroles.role|Yes|name of the IAM role that provides access to the dataset.|\nroles.access|Yes|the type of access provided by the IAM role; the value will generally come directly from the "BQ dataset to IAM roles mapping" document.|\nroles.firstLevelApprovers|No|the name(s) of the first level approver(s) of the role.|\nroles.secondLevelApprovers|No|the name(s) of the second level approver(s) of the role.|\n')
outputFile.close()
