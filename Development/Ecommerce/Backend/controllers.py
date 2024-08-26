from flask import Blueprint, jsonify, request
from models import Product, db

# Define a blueprint for routes
main = Blueprint('main', __name__)

# Route to get all products
@main.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

# Route to get a single product by its ID
@main.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product:
        return jsonify(product.to_dict())
    return jsonify({'message': 'Product not found'}), 404

# Route to add a product to the cart (example)
@main.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    product_id = data.get('product_id')
    product = Product.query.get(product_id)
    if product:
        # Logic to add the product to the cart could be expanded here
        return jsonify({'message': f'{product.name} added to cart successfully!'})
    return jsonify({'message': 'Product not found'}), 404
