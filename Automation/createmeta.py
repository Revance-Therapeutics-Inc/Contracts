"""
This program uses metadata from snowflake about a table in order to create the
corresponding tables' section in the Dataset and Schema section in the corresponding data domain.
The metada comes from a csv, which is downloaded from the results of the following
query in Snowflake:

select * from staging_dev.information_schema.columns where table_name = 'LOCATION_MASTER'

Where, of course, you may substitute out the specific databse where you are
getting the information schema, and you can substitute out the table_name for
the table in which you want to use.

The program uses local files, and does not interact with Snowflake directly at all.
In order to use it, you must download the results of that query and place it in 
the same folder as this program, and then you must create an output file in this folder
as well. After doing so, make sure that you specify the correct input and output
file in the code below.

Certain attributes for each column are set to null by default, so that the user may
edit them after pasting the results into the Data Contract. other attributes are set 
to different values. Those are listed below.
isPrimary - set to true for the column which has a original_position of 1 in the information_schema
physicalType - set to UNKNOWN if its data type has not been yet accounted for below
isNullable - set to true unless otherwise it has an original_position of 1 or it has 'NO' in the
             IS_NULLABLE column inside snowflake. However, most of the tables dont actually have
             'NO'in the IS_NULLABLE column yet, so you may have to set this value manually
dataGranularity - set to One row per url, location, practice, etc. which may not always be the case
"""

import csv

with open('practice.csv', 'r') as csvFile:
    output = open('dataset.txt', 'w')
    csvReader = csv.reader(csvFile)

    next(csvReader) #skip past the column names
    i = 0
    stringList = []
    stringMap = {} #used to order the rows based on ORIGINAL_POSTITION in snowflake. See line 104
    for line in csvReader:
        if i == 0:
            tableName = line[2].lower().split('_')
            tableString = ''
            for t in tableName:
                tableString += t
                tableString += ' '
            output.write('  - table: ' + tableString + '\n')
            output.write('    physicalName: ' + line[2] + '\n')
            output.write('    priorTableName: null\n')
            if tableName[0] == 'vw':
                output.write('    description: master dimension of all ' + tableName[1] + 's\n')
            else:
                output.write('    description: master dimension of all ' + tableName[0] + 's\n')
            output.write('    tags: null\n')
            if tableName[0] == 'vw':
                output.write('    dataGranularity: One row per ' + tableName[1] + '\n')
            else:
                output.write('    dataGranularity: One row per ' + tableName[0] + '\n')
            output.write('    columns:\n')
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
stringList.sort()
for j in range(i):
    output.write(stringMap[j+1])
csvFile.close()
output.close()
