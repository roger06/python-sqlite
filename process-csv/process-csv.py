import csv
import sys
table = 'postcodes'
inputFile = '/home/roger/Downloads/postcodes.csv'

createTable = False
breakAt = 10

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

    sql += "INSERT INTO `"+ table+"` (`postcode`, `postcode2`,`lsoa_name`, `LSOA`) VALUES \n"
     
    # sys.exit()
    
    for row in reader:
        lsoa_name = row["lsoa_name"].replace("'", "''")
        lsoa_name = lsoa_name.replace(",", "::")

        sql += " ('" + row["postcode"] + "' , '"+ row["postcode2"]+ "',   '"+  lsoa_name+ "', '"+ row["LSOA"]+ "')"
        rowCount +=1

        if rowCount != totalrows:
            sql += ","

        sql += "\n"

        print(sql)

        if rowCount == breakAt:
            break


# f = open("postcodes.sql", "w")
# f.write(sql)
# f.close()