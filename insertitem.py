import connection

def add_item(product_name, quantity, price, manufacture_date, expiry_date):
    mydb = connection.db_connection()
    mycursor = mydb.cursor()

    sql = "INSERT INTO products (product_name, quantity, price, manufacture_date, expiry_date) VALUES (%s, %s, %s, %s, %s)"
    values = (product_name, quantity, price, manufacture_date, expiry_date)
    
    try:
        mycursor.execute(sql, values)
        mydb.commit()
        print("Product added successfully!")
    except Exception as e:
        raise e
    
    mydb.close()
    
