import connection 

def add_item():
    mydb = connection.db_connection()
    print(mydb)
    mycursor = mydb.cursor()
    num_products = int(input("Enter the number of products you want to add: "))
    
    for i in range(num_products):
        print(f"\n Adding product {i + 1}:")
        product_name = input("Product Name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
        manufacture_date = input("Manufacture Date (YYYY-MM-DD): ")
        expiry_date = input("Expiry Date (YYYY-MM-DD): ")

        sql = "INSERT INTO products (product_name, quantity, price, manufacture_date, expiry_date) VALUES (%s, %s, %s, %s, %s)"
        values = (product_name, quantity, price, manufacture_date, expiry_date)
        mycursor.execute(sql, values)
        print("Product added successfully!")
    mydb.commit()
    mydb.close()
    
if __name__ == "__main__":
    add_item()

