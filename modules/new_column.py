def new_column(product_info):
    
    for cursor in range (2, product_info.max_row+1):
        product_info.cell(cursor, 5).value = product_info.cell(cursor, 2).value * product_info.cell(cursor,3).value
