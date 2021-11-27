import pandas as pd
import sys
import functions

empFile = 'data/employees.json'
taxFile = 'data/tax-tables.json'

# Load the JSON file into a DataFrame: 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html


empData = pd.read_json(empFile)
taxData = pd.read_json(taxFile)

print(taxData)

# for index, row in taxData.iterrows():
#     print(index, row[3])
 

sys.exit()

# for index, row in empData.iterrows():
#     print(row['id'] , row['firstname'] , row['lastname'] + " £" + str(functions.printSalary(row['salary']))  + " take-home = " + str(functions.printSalary(586) ))

for index, row in empData.iterrows():
    salary = row['salary']
    # print( str(functions.calNetSalary(row['salary'], taxData) ))

# str(functions.calNetSalary(row['salary']) )
    # for index, row in taxData.iterrows():
    #         print(row['id'] , row['minsalary'] , row['maxsalary'], row['rate'])

            # if salary > row['minsalary'] and salary <  row['maxsalary']:
            #     band = row['id']
            #     print("Band is ",band  )

    print( "For salary ", salary , " " ,  functions.calNetSalary(salary, taxData))
              
    # sys.exit()