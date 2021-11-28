import pandas as pd
import sys
import functions
import json
from tkinter import *

win = Tk()
Label(win, text="Payroll").pack()

text = Text(win)

win.minsize(400,600)

empFile = 'data/employees.json'
taxFile = 'data/tax-tables.json'

# Load the JSON file into a DataFrame: 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html


empData = pd.read_json(empFile)
# taxData = pd.read_json(taxFile)
 

with open(taxFile) as json_file:
    taxData = json.load(json_file)
  
  

# sys.exit()

# 
theText = ''
for index, row in empData.iterrows():
    salary = row['salary']


    netSalary = functions.calNetSalary(salary, taxData) /12
    netSalary = "{:.2f}".format(netSalary)
   
    theText +=  row['firstname'] + " " + row['lastname'] +  " £" + netSalary  + "\n"
    # print( row['firstname'], row['lastname'] , "£",netSalary  )
   
    # sys.exit()

   
text.insert(INSERT, theText)
text.pack()
win.mainloop()