import os
from flask import Flask
from .extensions import db, login_manager


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    app.config['SECRET_KEY'] = 'dev-secret-key-change-this-in-prod'
    # Load config
    cfg = os.path.join(os.path.dirname(__file__), '..', 'config.py')
    if os.path.exists(cfg):
        app.config.from_pyfile(cfg)
    else:
        app.config.from_object('config')

    # ensure instance folder exists
    try:
        os.makedirs(os.path.join(app.root_path, '..', 'instance'), exist_ok=True)
    except Exception:
        pass

    db.init_app(app)
    login_manager.init_app(app)
    # user loader
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from .public.routes import public_bp
    from .auth.routes import auth_bp
    from .admin.routes import admin_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app
