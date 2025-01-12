from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app) 

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model (for login purposes)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# CORS preflight handling
@app.before_request
def handle_preflight():
    if request.method == 'OPTIONS':
        response = jsonify({"message": "CORS preflight"})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Credentials', 'true')

        return response

# Creating the tables only once
# @app.before_first_request
# def create_tables():
#     db.create_all()

# Admin home route
@app.route('/')
def home():
    print("Home route accessed")  # Check if this gets printed
    return jsonify({"message": "Welcome to the API"})

# Admin login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    print(f"Received login request for {username}")
    
    user = User.query.filter_by(username=username).first()
    
    if user and user.password == password:
        return jsonify({"message": "Login successful", "isAdmin": True}), 200
    print("Invalid credentials")
    return jsonify({"message": "Invalid credentials"}), 401


if __name__ == '__main__':
    app.run(debug=True)
