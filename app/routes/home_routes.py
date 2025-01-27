from flask import Blueprint, jsonify

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    print("Home route accessed")  # Check if this gets printed
    return jsonify({"message": "Welcome to the API"})