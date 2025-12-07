from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from . import auth_bp
from ..models import User
from ..extensions import db


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        flash('Invalid credentials', 'danger')
    return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('public.home'))
