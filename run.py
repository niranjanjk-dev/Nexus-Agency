from app import create_app, db
# IMPORTANT: You must import your models here so SQLAlchemy knows what tables to create
from app import models 

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # This line creates the tables if they don't exist
        db.create_all()
        print("Database tables created (if they didn't exist).")
        
    app.run(debug=True, port=8000)
