import openpyxl as xl

wb = xl.load_workbook('pycham_xl_1.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
cell1 = sheet.cell(1, 1)
print(sheet.values)
