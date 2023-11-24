import openpyxl
def good_out(sheet:openpyxl.worksheet.worksheet.Worksheet,ton):
    print(type(sheet))
    print(sheet.title)
    print(ton)
    