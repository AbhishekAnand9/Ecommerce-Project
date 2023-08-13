import connection

def delete_item(product_id):
    mydb = connection.db_connection()
    mycursor = mydb.cursor()

    sql_select = "SELECT product_name FROM products WHERE id = %s"
    mycursor.execute(sql_select, (product_id,))
    product_name = mycursor.fetchone()

    if not product_name:
        mydb.close()
        raise Exception("Product not found.")
    else:
        sql_delete = "DELETE FROM products WHERE id = %s"
        mycursor.execute(sql_delete, (product_id,))
        mydb.commit()
        mydb.close()


