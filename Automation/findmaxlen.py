import csv

outputfile = open('dc.txt', 'w')

inputfile = open('location.csv', 'r')
csvReader = csv.reader(inputfile)
next(csvReader)

queryMap = {}
i = 0

for line in csvReader:
    string = "select '" 
    string += str(line[3]).lower()
    string += "', max(length(" 
    string += str(line[3]).lower()
    string+= ")) as max_len, "
    string += str(line[4])
    string += " as cardinality from staging_dev.cdp.location_master\n"
    queryMap[int(line[4])] = string
    i += 1
outputfile.write("select * from (\n")
for j in range(i):
    outputfile.write(queryMap[j+1])
    if (j+1) != i:
        outputfile.write("union\n")
    else:
        outputfile.write(") order by cardinality")
    

