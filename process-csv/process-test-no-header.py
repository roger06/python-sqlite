#  reads a csv with no header row
#  this is just a test file - it does not create an SQL file

import csv
from csv import reader

 
inputFile = 'data/postcodes-short.csv'
  

with open(inputFile, 'r') as f:
    d_reader = csv.DictReader(f)

    #get fieldnames from DictReader object and store in list
    headers = d_reader.fieldnames

    numOfFields = len(headers)

    print(numOfFields)

    print(headers)
    print(headers[0])

 
