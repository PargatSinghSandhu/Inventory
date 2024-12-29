import openpyxl
def load_file(input_file):   
    inv_file = openpyxl.load_workbook(input_file) #this will give us whole file content
    product_info = inv_file["Sheet1"] # information of sheet 1 is in variabnle whole_inoformtio
    return inv_file, product_info