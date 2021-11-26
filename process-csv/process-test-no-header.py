#  reads a csv with no header row
#  this is just a test file - it does not create an SQL file

import csv
from csv import reader

 
inputFile = 'data/postcodes-short-no-header.csv'
  

# skip first line i.e. read header first and then iterate over each row od csv as a list
with open(inputFile, 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            print(row[0])


       

 
