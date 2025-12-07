import os
from app import create_app
from app.extensions import db
from app.models import User, Service, PortfolioItem


def seed():
    app = create_app()
    with app.app_context():
        db.create_all()

        # Seed admin user
        email = app.config.get('SEED_ADMIN_EMAIL', 'admin@coralzo.com')
        pwd = app.config.get('SEED_ADMIN_PASSWORD', '@#jhfs6&%d')
        if not User.query.filter_by(email=email).first():
            u = User(email=email, is_admin=True)
            u.set_password(pwd)
            db.session.add(u)

        # Seed services
        if not Service.query.first():
            services = [
                Service(title='Full-Stack Launch', slug='full-stack-launch', price='$4,500', description='Landing + 3 pages + CMS'),
                Service(title='Growth Content Pack', slug='growth-content', price='$1,200', description='8 social posts + 2 graphics'),
                Service(title='Notion Starter Template', slug='notion-starter', price='$49', description='Downloadable Notion template')
            ]
            db.session.bulk_save_objects(services)

        # Seed portfolio
        if not PortfolioItem.query.first():
            pf = [
                PortfolioItem(title='Notion CRM Template', category='Notion', description='Template for small teams'),
                PortfolioItem(title='LinkedIn Makeover', category='LinkedIn', description='Profile & page design'),
                PortfolioItem(title='Social Launch Campaign', category='Social', description='Content and assets')
            ]
            db.session.bulk_save_objects(pf)

        db.session.commit()
        print('Seed complete. Admin:', email)


if __name__ == '__main__':
    seed()
