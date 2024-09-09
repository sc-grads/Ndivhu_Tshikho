from flask import Blueprint, request, jsonify
from model.cart_model import Cart
from src import db
import logging

cart_bp = Blueprint('cart', __name__)
logger = logging.getLogger(__name__)

@cart_bp.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    logger.info(f'Fetching cart for user ID: {user_id}')
    cart = Cart.query.filter_by(user_id=user_id).all()
    cart_items = [item.to_dict() for item in cart]
    logger.info(f'Cart for user ID: {user_id} fetched successfully')
    return jsonify(cart_items), 200
