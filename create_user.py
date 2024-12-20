from app import app, db, User  # Import the app, db, and User model

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()  # Create all tables based on models
    # Add a new admin user
    user = User(username='admin', password='admin123')
    db.session.add(user)
    db.session.commit()

print("Admin user created successfully!")