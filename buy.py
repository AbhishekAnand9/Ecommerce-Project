import connection
from purchase import purchase_product ,check_stock_availability , update_product_stock
import purchase
def buy_product(product_id, quantity):
    print(product_id,quantity)
    
    if product_id is None or quantity is None:
        return ({'error':'Both feilds are mandatory'})
    mydb = connection.db_connection()
    mycursor = mydb.cursor()
   
    if purchase.check_stock_availability(mycursor, product_id, quantity,False):
        purchase.update_product_stock(mycursor, [(product_id, quantity)], mydb)
        mydb.close()
        return ({'messege' :'Successful Purchase'})
    
    else:
        return ({'error':'out of stock'})
       



