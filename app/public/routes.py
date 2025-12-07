from flask import render_template, request, redirect, url_for, current_app, flash
from . import public_bp
from ..models import Service, PortfolioItem, Lead
from ..extensions import db


@public_bp.route('/')
def home():
    services = Service.query.limit(6).all()
    portfolio = PortfolioItem.query.limit(6).all()
    return render_template('home.html', services=services, portfolio=portfolio)


@public_bp.route('/lead', methods=['POST'])
def lead_capture():
    data = request.form
    lead = Lead(
        name=data.get('name'),
        email=data.get('email'),
        company=data.get('company'),
        service_interest=data.get('service_interest'),
        budget=data.get('budget'),
        message=data.get('message') 
    )
    db.session.add(lead)
    db.session.commit()
    # send email notification (simple console fallback)
    try:
        import smtplib
        # for production, use Flask-Mail or external provider
    except Exception:
        pass
    flash('Thanks — we received your request.', 'success')
    return redirect(url_for('public.home'))
