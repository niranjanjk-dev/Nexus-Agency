# CoralZo — coralzo_ecosystem0.01

Starter Flask project scaffold for the CoralZo agency website.

Quick start (development):

1. Create a virtualenv and install dependencies:

```sh
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

2. Seed the database (creates an admin user and sample data):

```sh
python seed.py
```

3. Run the app:

```sh
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

Admin credentials (seeded):
- email: `admin@coralzo.com`
- password: `@#jhfs6&%d`  (CHANGE THIS IMMEDIATELY)

Configuration: copy `config.py.example` to `config.py` and update email/SMTP settings.

This scaffold includes:
- Flask app factory
- Blueprints: `public`, `auth`, `admin`
- SQLite DB + SQLAlchemy models
- Seed script for services, portfolio, admin user, and leads
- A single consolidated CSS file at `app/static/css/main.css`
