import connection
def delete_item(product_id):
    mydb = connection.db_connection()
    mycursor = mydb.cursor()

    sql_select = "SELECT product_name FROM products WHERE id = %s"
    mycursor.execute(sql_select, (product_id,))
    product_name = mycursor.fetchone()

    if not product_name:
        print("Product not found.")
        mydb.close()
        return

    sql_delete = "DELETE FROM products WHERE id = %s"
    mycursor.execute(sql_delete, (product_id,))
    mydb.commit()
    print(f"Product '{product_name[0]}' with ID {product_id} deleted successfully.")
    mydb.close()


def purchase_product():
    mydb = connection.db_connection()
    mycursor = mydb.cursor()
    purchase_list = get_purchase_list(mycursor)

    if not purchase_list:
        print("No items selected for purchase.")
        mydb.close()
        return

    if not check_stock_availability(mycursor,False, False, purchase_list):
        print("One or more products are not available in the required quantity.")
        mydb.close()
        return

    
    update_product_stock(mycursor, purchase_list, mydb) 
    mydb.commit()
    print("Purchase successful! Thank you for shopping with us.")
    mydb.close()


def get_purchase_list(cursor):
    purchase_list = []
    while True:
        search_input = input("Enter at least 3 characters to search for a product (0 to finish): ")
        if search_input == '0':
            break

        if len(search_input) < 3:
            print("Please enter at least 3 characters to search for a product.")
            continue
        sql = "SELECT id, product_name  FROM products WHERE product_name LIKE %s AND quantity > 0"
        cursor.execute(sql, ('%' + search_input + '%',))
        products = cursor.fetchall()

        if not products:
            print("No products found matching the search criteria.")
        else:
            print("ID\tProduct Name")
            for product in products:
                print(f"{product[0]}\t{product[1]}")

            while True:
                product_id = int(input("Enter the ID of the product you want to purchase (0 to finish search): "))
                if product_id == 0:
                    break
                quantity = int(input("Enter the quantity you want to purchase: "))
                if check_stock_availability(cursor,product_id,quantity,False):
                    purchase_list.append((product_id, quantity))
                else:
                    print("Entered quantity is not available in stock .")
    return purchase_list


def check_stock_availability(ram, shyam,sita,gita):
    if gita:
        for product_id, quantity in gita:
            sql = "SELECT quantity FROM products WHERE id = %s"
            ram.execute(sql, (product_id,))
            available_quantity = ram.fetchone()[0]
            if quantity > available_quantity:
                return False
        return True
    else:
        sql = "SELECT quantity FROM products WHERE id = %s"
        ram.execute(sql, (shyam,))
        available_quantity = ram.fetchone()[0]
        if sita > available_quantity:
            return False
        return True
        

def update_product_stock(cursor, purchase_list, mydb):
    for product_id, quantity in purchase_list:
        sql_select = "SELECT quantity FROM products WHERE id = %s"
        cursor.execute(sql_select, (product_id,))
        available_quantity = cursor.fetchone()[0]

        if available_quantity < quantity:
            print(f"Product with ID {product_id} does not have sufficient stock. Available: {available_quantity}")
            continue

        new_quantity = available_quantity - quantity  
        sql_update = "UPDATE products SET quantity = %s WHERE id = %s"
        cursor.execute(sql_update, (new_quantity, product_id))
        print(f"Purchase successful for product with ID {product_id}! Thank you for shopping with us.")
        mydb.commit()  


if __name__ == "__main__":
    user_choice = input("Enter '1' to purchase products, '2' to delete a product: ")
    
    if user_choice == '1':
        purchase_product()
    elif user_choice == '2':
        product_id_to_delete = int(input("Enter the ID of the product you want to delete: "))
        delete_item(product_id_to_delete)
    else:
        print("Invalid choice.")
        
