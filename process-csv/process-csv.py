import csv
import sys
import math

table = 'postcodes'
inputFile = '/home/roger/Downloads/postcodes.csv'

createTable = True   # true creates the table
breakAt = 10
linesPerFile = 200000   # max lines per file
lineCounter = 0
fileName = 'postcodes_'  # base file name
fileExt = '.sql'  # file extention
fileCount = 1
insertCode = "INSERT INTO `"+ table+"` (`postcode`, `postcode2`,`lsoa_name`, `LSOA`) VALUES \n"


# lsoa_name,LSOA

if createTable is True:
    sql = "CREATE TABLE `"+ table +"` \n (`postcode` varchar(12) DEFAULT NULL,\n  `postcode2` varchar(12) DEFAULT NULL,\n `lsoa_name` varchar(255) DEFAULT NULL, \n`LSOA` varchar(12) DEFAULT NULL )\n ENGINE=InnoDB \nDEFAULT CHARSET=utf8;\n\n"
else:
    sql = ''

rowCount = 1

with open(inputFile, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    totalrows = len(open(inputFile).readlines())
    print( totalrows)

    numFiles = totalrows / linesPerFile

    print('number of files = ' + str(math.ceil( numFiles)))   # round up as we want whole files to use

    fileToWrite = "postcodes"+ str(fileCount) + ".sql"

    sql += insertCode     
    # sys.exit()
    
    for row in reader:
        lsoa_name = row["lsoa_name"].replace("'", "''")
        lsoa_name = lsoa_name.replace(",", "::")

        sql += " ('" + row["postcode"] + "' , '"+ row["postcode2"]+ "',   '"+  lsoa_name+ "', '"+ row["LSOA"]+ "')"
        rowCount +=1

        lineCounter += 1
     
        # if rowCount != totalrows:
        #     sql += ","


        # print(sql)
 
        # if rowCount == breakAt:
        #     break
        # print("row " + str(lineCounter) + " File = " + str(fileCount) )
        if lineCounter == linesPerFile:

            fileToWrite = "postcodes"+ str(fileCount) + ".sql"
            
            lineCounter = 1  # reset line count
            fileCount += 1   
        

            f = open("output/"+  fileToWrite , "w")
            f.write(sql)
            sql = insertCode     # reset the sql with the insert statement.
            #  todo - still need to remove the last comma from each file.
        else:
            sql += ","

        sql += "\n"

        # print("File to write = " + fileToWrite)     # this print command really slows down script execution.

f.close()
