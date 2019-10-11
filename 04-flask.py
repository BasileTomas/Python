from flask import Flask, jsonify
from products import products

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message":"pong!"})

#Endpoint que retorna todos los productos
@app.route('/products')
def getProducts():
        return jsonify({"products": products})   

#Endpoint que retorna el producto indicado por id
@app.route('/product/<int:id_product>')
def getProduct(id_product):
    productFound = [product for product in products if product['id'] == id_product]
    if(len(productFound) > 0):
        return jsonify({"product": productFound[0]})
    else:
        return jsonify({"message": "Product not found"})


if __name__== '__main__':
    app.run(debug= True, port= 4000)
