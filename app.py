from flask import Flask, request, jsonify, render_template
import purchase 
import connection
import additem
from search import search_product
from buy import buy_product
from deleteitem import delete_item
from insertitem import add_item
app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_data():
     product_name = request.args.get('product-name')
     print(request)
     print(product_name)
     
     product_list=search_product(product_name)
     return (jsonify(product_list) ,404 if  "error" in  product_list else 200)
    


@app.route('/purchase', methods=['POST'])
def purchase_item():
    data = request.get_json()
    if 'id' not in data or 'quantity' not in data:
        return jsonify({'error':'Both feilds are mandatory'})
    
    item_id = data['id']
    quantity = data['quantity']
    print(data,item_id,quantity)
    
    data1=buy_product(item_id,quantity)
    return (jsonify(data1) ,404 if  "error" in  data1 else 200)
    
    
    
@app.route('/delete', methods=['POST'])
def delete_product():
    try:
        data = request.get_json()
        product_id = data['product_id']
        
        delete_item(product_id)
        
        return jsonify({'message': f'Product with ID {product_id} deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400




@app.route('/add', methods=['POST'])
def add_product():
    try:
        data = request.get_json()
        
        product_name = data['product_name']
        quantity = data['quantity']
        price = data['price']
        manufacture_date = data['manufacture_date']
        expiry_date = data['expiry_date']

        add_item(product_name, quantity, price, manufacture_date, expiry_date)

        return jsonify({'message': 'Product added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


