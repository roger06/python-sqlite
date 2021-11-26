# script reads a  CSV file 
# we'll work out the headerList and use these as colum names 
import csv
import sys
import math

table = 'postcodes'
inputFile = 'data/postcodes.csv'

createTable = True   # true creates the table
breakAt = 10
linesPerFile = 200000   # max lines (of sql) per file
lineCounter = 1
fileName = 'postcodes_'  # base file name
fileExt = '.sql'  # file extention
fileCount = 1


# get headerList


with open(inputFile, 'r') as f:
    d_reader = csv.DictReader(f)

    #get fieldnames from DictReader object and store in list
    headerList = d_reader.fieldnames

    numOfFields = len(headerList)   # should we need the length (number of headers)

    # print(numOfFields)

    # print(headerList)
    # print(headerList[0])


if createTable is True:
    sql = "CREATE TABLE  `" + table + "` (\n "

    colCount = 0

    for column in headerList:
        print("col = " + column)

        sql += "`"+ column +"` varchar(50)  DEFAULT NULL "
        if colCount != numOfFields-1:
            sql += ", "
        colCount += 1

        sql += "\n"
       

else:
    sql = ''

print(sql)


sql += ")\n ENGINE=InnoDB \nDEFAULT CHARSET=utf8;\n\n"


    

insertSql = "INSERT INTO `"+ table +"` "


# `postcode`, `postcode2`,`lsoa_name`, `LSOA`
# 
insertSql += " VALUES \n ("

rowCount = 1

with open(inputFile, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    totalrows = len(open(inputFile).readlines())
    print( totalrows)

    numFiles = totalrows / linesPerFile

    print('number of files = ' + str(math.ceil( numFiles)))   # round up as we want whole files to use

    fileToWrite = "postcodes"+ str(fileCount) + ".sql"

    # insertSql = insertCode     
    # sys.exit()
    
    for row in reader:
        lsoa_name = row["lsoa_name"].replace("'", "''")
        lsoa_name = lsoa_name.replace(",", "::")
        
        colCount = 0

        for column in headerList:

            insertSql += " '" + row[column] + "'"
            if colCount != numOfFields-1:
                insertSql += ",  \n"
    
            colCount += 1    
            # '"+ row["postcode2"]+ "',   '"+  lsoa_name+ "', '"+ row["LSOA"]+ "')"
        rowCount +=1
        insertSql += ")"
        print(insertSql)


        sys.exit()
        lineCounter += 1
     
     

        if lineCounter == linesPerFile or rowCount == totalrows:

            fileToWrite = "postcodes"+ str(fileCount) + ".sql"
            
            lineCounter = 1  # reset line count
            fileCount += 1   
            print(".", end='')
        

            f = open("output/"+  fileToWrite , "w")
            f.write(insertSql)
            insertSql = insertCode     # reset the sql with the insert statement.
            
        else:
            insertSql += ","

        insertSql += "\n"

        # print("File to write = " + fileToWrite)     # this print command really slows down script execution.

f.close()
# print("final line count = " + str(lineCounter) )
# print("final row count = " + str(rowCount) )