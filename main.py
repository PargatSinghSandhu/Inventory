import openpyxl 
from product_supplier import product_supplier
from total_inventory import total_inventory
from load_inventory import load_file
from products_less_ten import product_less_ten
from new_column import new_column 


def main():
    input_file = "inventory.xlsx"
    output_file = "inv_updated.xlsx"
      
    inv_file, product_info=load_file(input_file)
#product per supplier
    product_supplier_count = product_supplier(product_info)

#total inventory 
    totalinventory_count= total_inventory(product_info)
   
#products with inventory less 10 

    product_less_ten_count = product_less_ten(product_info)
  
#new column , 5th column with the price*inventory 
    new_column(product_info)
    
    inv_file.save(output_file)


    print("This is the total product supplier information", product_supplier_count)
    print("This is the total inventory", totalinventory_count)
    print("This is the information less than the ten", product_less_ten_count)


if __name__ == "__main__":
    main()