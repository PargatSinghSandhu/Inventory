

def product_supplier(product_info):
    ''' param : product_info will take the information of the .xlsx file
    This function will give the count of the productsw of each supplier in the dictoonary format
    and return the dict 
    '''
    product_per_supplier= {}
    for cursor in range(2, product_info.max_row+1): #by default the max_row starts with 0, and so it will be 0 to 74, so we are adding +1
        supplier_name = product_info.cell(cursor, 4).value #row second, column 4 (2,4)    
        if supplier_name in product_per_supplier:
            count_supplier_name = product_per_supplier[supplier_name]
            product_per_supplier[supplier_name] = count_supplier_name+1  # +1 in total, so i need the count 
        else:
            #print("New Supplie added")
            product_per_supplier[supplier_name]=1
    
    return product_per_supplier