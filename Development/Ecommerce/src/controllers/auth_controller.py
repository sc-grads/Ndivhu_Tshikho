from flask import request, redirect, url_for, render_template, flash
from ..models.user import User, db

def register_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash('Registration successful. Please login.')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            flash('Login successful.')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials.')
            return redirect(url_for('auth.login'))
    
    return render_template('login.html')
