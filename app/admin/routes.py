from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import admin_bp
from ..models import Service, PortfolioItem, Lead, User
from ..extensions import db


@admin_bp.route('/')
@login_required
def dashboard():
    services = Service.query.all()
    portfolio = PortfolioItem.query.all()
    leads = Lead.query.order_by(Lead.created_at.desc()).limit(20).all()
    return render_template('admin/dashboard.html', services=services, portfolio=portfolio, leads=leads)


@admin_bp.route('/services/new', methods=['GET', 'POST'])
@login_required
def new_service():
    if request.method == 'POST':
        s = Service(
            title=request.form.get('title'),
            slug=request.form.get('slug'),
            price=request.form.get('price'),
            description=request.form.get('description')
        )
        db.session.add(s)
        db.session.commit()
        flash('Service created', 'success')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/new_service.html')
