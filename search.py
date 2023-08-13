import connection
from purchase import purchase_product

def search_product(product_name):
    if not product_name:
        raise Exception("Product Name cannot be empty.")
    else:
         mydb = connection.db_connection()
         cursor=mydb.cursor()
         sql = "SELECT id, product_name  FROM products WHERE product_name LIKE %s AND quantity > 0"
         cursor.execute(sql, ('%' + product_name + '%',))
         products = cursor.fetchall()
        #  print(cursor.fetchall)
         print(product_name, 14, products)
         if not products:
            
            return ({'error':'No products found matching the search criteria.'})
         else:
             print("ID\tProduct Name")
             product_list=[]
             for product in products:
                 product_list.append({
                     'name': product[1],
                     'id': product[0]
                 })
             return ({'product_list':product_list})
         