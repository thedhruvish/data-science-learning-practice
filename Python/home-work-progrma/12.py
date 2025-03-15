# Q12. Can you write a Python code to read a Comma-Separated Values (CSV) file, apply a specific 
# condition to each row, and create a new CSV file that contains only the rows that satisfy the 
# condition? For example, if the CSV file contains information about products and their prices, you 
# may want to create a new CSV file that only includes the products that are within a certain price 
# range. The program should be able to read the CSV file, compare the values in each row to the 
# specified condition, and write the rows that meet the criteria to a new CSV file.

import csv

inputF = 'products.csv' 
price_range = (10.00, 50.00)
with open(inputF, 'r') as inF:
    reader = csv.reader(inF)

    with open("ans_13.csv",'w') as outF:
        writer = csv.writer(outF)
        for row in reader:
            try:
                price = float(row[1])      
                if price_range[0] <= price <= price_range[1]:
                    writer.writerow(row)  
            except:
                pass

