def total_inventory(product_info):
    '''param: product info is the whole information
       this function is calucating the total inventory
        '''
    total_inventory = {}
    for cursor in range(2, product_info.max_row+1):
        supplier_name = product_info.cell(cursor, 4).value
        
        if supplier_name in total_inventory:
            
            previous_value= total_inventory[supplier_name]           
            total_inventory[supplier_name] = previous_value+(product_info.cell(cursor, 2).value*product_info.cell(cursor,3).value) 

        else:
            print("New value added")
            total_inventory[supplier_name] = product_info.cell(cursor, 2).value*product_info.cell(cursor,3).value 
    return total_inventory