# List of modules---------
import openpyxl
import os
import pandas as pd
import json

# List of variables---------
wb_file_path = './PY02_EXCEL_WITH_PYTHON/customer_data.xlsx'
wb = openpyxl.Workbook()
sheet1 = wb['Sheet']

# List of functions---------
def custom_print(label, value):
    print(f"{label}: {value} \n")

def print_title(title):
    print(f"\n\n--------------------- {title}\n")

def save_file():
    return wb.save(wb_file_path)

def print_dimension(sheet):
    custom_print('Sheet Dimension', sheet.calculate_dimension())

#Clear the terminal.
os.system('clear') 

#Insert cell values 
sheet1['A1'] = 'first_name'
sheet1['B1'] = 'last_name'
sheet1['C1'] = 'gender'

#Save the workbook inside PY_02
save_file()

#Update C1 value as M/F
sheet1['C1'] = 'M/F'

#Save the workbook inside PY_02
save_file()

#Get range of cells where cell value is present.
"""
calculate_dimension() gives same result when you 
press CTRL UP and CTRL DOWN to select data.
"""
print_title('#Get range of cells where cell value is present.')
custom_print('Sheet Dimension', sheet1.calculate_dimension())

#Insert data of headers
sheet1.append(['Manish', 'Shivale', 'M'])
save_file()

#Insert 3 rows after A1
print_title('#Insert 3 rows after A1')
sheet1.insert_rows(2,3)
#Insert 1 column before A1
print_title('#Insert 1 row before A1')
sheet1.insert_cols(1)
sheet1['A1'] = 'Roll_No'
sheet1['A5'] = 1
save_file()
print_dimension(sheet1)

#Delete empty rows between A1 and A5
print_title('#Delete empty rows between A1 and A5')
sheet1.delete_rows(2,3)
save_file()
print_dimension(sheet1)

#Rename the active sheet as "Customer".
print_title('#Rename the active sheet as "Customer".')
sheet1.title = "Customer"
save_file()