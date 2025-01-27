from app.models import User

def login_user(username, password):
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        return {"message": "Login successful", "isAdmin": True}, 200
    else:
        print("Invalid credentials")
        return {"message": "Invalid credentials"}, 401