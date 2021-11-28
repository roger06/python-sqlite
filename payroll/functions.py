# def printSalary(salary):
#     return(salary)

def calNetSalary(salary, taxData):
    netSalary = 0
    band = 0

    # loop through tax

    for row in taxData:
        # print(row['id'] , row['minsalary'] , row['maxsalary'], row['rate'])
        if salary > row['minsalary'] and salary < row['maxsalary']:
            band = row['id']
    # print("Band is ", band)

    #  under £10k - no tax
    if band == 1:
        netSalary = salary

    #  20% of £10k - £40K
    if band == 2:

        taxable = (salary - 10000)
        taxdue = (taxable / 100) * taxData[1]['rate']                    # 20%
        netSalary = salary - taxdue

    if band == 3:

        taxable1 = (taxData[2]['minsalary'] - taxData[0]['maxsalary'])   # £30k

        taxdue1 = (taxable1 / 100) * taxData[1]['rate']                    # 20%

        taxable2 = (salary - taxData[1]['maxsalary'])
        taxdue2 = (taxable2 / 100) * taxData[2]['rate']                    # 40%

        totalTax = taxdue1 + taxdue2
        netSalary = salary - totalTax

    if band == 4:

        taxable1 = (taxData[2]['minsalary'] - taxData[0]['maxsalary'])   # £30k

        taxdue1 = (taxable1 / 100) * taxData[1]['rate']                    # 20%

        taxable2 = (taxData[2]['maxsalary'] - taxData[2]['minsalary'])
        taxdue2 = (taxable2 / 100) * taxData[2]['rate']                    # 40%
        
        taxable3 = (salary - taxData[2]['maxsalary']  )  
        taxdue3 =  (taxable2 / 100) * taxData[3]['rate']                    # 50%
        

        totalTax = taxdue1 + taxdue2 + taxdue3
        netSalary = (salary - totalTax) 
         

    return(netSalary)
