def product_less_ten(product_info):
    '''param: product info is the whole information this function 
    is calucating the product'''
    info_less_ten = {}
    for cursor in range (2, product_info.max_row+1):        
        supplier_name = product_info.cell(cursor, 4).value
        if product_info.cell(cursor, 2).value < 10:
            info_less_ten[int(product_info.cell(cursor,1).value)] = int(product_info.cell(cursor, 2).value) #bty defualt the values are interpreted as float numbers 
    return info_less_ten