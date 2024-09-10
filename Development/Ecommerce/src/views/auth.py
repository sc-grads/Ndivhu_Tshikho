from flask import Blueprint, redirect, render_template, request, url_for
from controllers.auth_controller import register_user, login_user

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic
        return redirect(url_for('auth_bp.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        return redirect(url_for('auth_bp.dashboard'))  # Or wherever you want to redirect after login
    return render_template('login.html')