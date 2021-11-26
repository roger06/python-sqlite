#  this is just a test file - it does not create an SQL file

import csv
import sys
 

 
inputFile = 'data/postcodes-short.csv'
   

rowCount = 1

with open(inputFile, newline='') as csvfile:
    reader = csv.DictReader(csvfile)                # by default uses top row as column headings

    print(reader)

    totalrows = len(open(inputFile).readlines())
    print( totalrows)

   
    
    for row in reader:
        lsoa_name = row["lsoa_name"].replace("'", "''")
        lsoa_name = lsoa_name.replace(",", "::")

        print(lsoa_name)

      
     
     
       

 
