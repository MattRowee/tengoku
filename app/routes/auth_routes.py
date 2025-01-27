from flask import Blueprint, request, jsonify
from app.services.auth_service import login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    print(f"Received login request for {username}")

    result, status_code = login_user(username, password)
    return jsonify(result), status_code