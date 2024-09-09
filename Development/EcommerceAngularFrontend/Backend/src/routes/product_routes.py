from flask import Blueprint, request, jsonify
from model.product_model import Product
from src import db
import logging

product_bp = Blueprint('product', __name__)
logger = logging.getLogger(__name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    logger.info('Fetching all products')
    products = Product.query.all()
    product_list = [product.to_dict() for product in products]
    logger.info('Products fetched successfully')
    return jsonify(product_list), 200

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    logger.info(f'Fetching product with ID: {product_id}')
    product = Product.query.get_or_404(product_id)
    logger.info(f'Product with ID: {product_id} fetched successfully')
    return jsonify(product.to_dict()), 200
