from flask import Blueprint, jsonify, request
from model.cart_model import Cart, db
from model.product_model import Product

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    user_id = data.get('user_id')
    quantity = data.get('quantity')

    cart_item = Cart(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity
    )

    db.session.add(cart_item)
    db.session.commit()

    return jsonify({'message': 'Product added to cart'}), 201

@cart_bp.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    cart_list = [{
        'product_name': item.product.name,
        'quantity': item.quantity,
        'price': item.product.price
    } for item in cart_items]

    return jsonify(cart_list), 200
