import pandas as pd
import sys
import functions

empFile = 'data/employees.json'
taxFile = 'data/tax-tables.json'

# Load the JSON file into a DataFrame: 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html


empData = pd.read_json(empFile)
taxData = pd.read_json(taxFile)


for index, row in taxData.iterrows():
        print(row['id'] , row['minsalary'] , row['maxsalary'], row['rate'])

sys.exit()
# functions.calNetSalary(238476)


# for index, row in empData.iterrows():
#     print(row['id'] , row['firstname'] , row['lastname'] + " £" + str(functions.printSalary(row['salary']))  + " take-home = " + str(functions.printSalary(586) ))

for index, row in empData.iterrows():
    print( str(functions.calNetSalary(row['salary'], taxData) ))

# str(functions.calNetSalary(row['salary']) )
   

# print(empData.to_string())  

# print(empData[0])