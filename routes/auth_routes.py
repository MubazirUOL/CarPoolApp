from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from models.user_model import User
from database.db import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')


        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash('Email already exists!', 'danger')
            return redirect(url_for('auth.register'))


        hashed_password = generate_password_hash(password)


        new_user = User(
            full_name=full_name,
            email=email,
            password=hashed_password,
            role=role
        )

        db.session.add(new_user)
        db.session.commit()


        flash('Registration successful!', 'success')

        return redirect(url_for('auth.login'))


    return render_template('auth/register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')


        user = User.query.filter_by(email=email).first()


        if user and check_password_hash(user.password, password):

            session['user_id'] = user.id
            session['user_name'] = user.full_name
            session['user_role'] = user.role

            flash('Login successful!', 'success')

            return redirect(url_for('dashboard'))

        else:
            flash('Invalid email or password!', 'danger')


    return render_template('auth/login.html')

@auth.route('/logout')
def logout():

    session.clear()

    flash('Logged out successfully!', 'success')

    return redirect(url_for('auth.login'))