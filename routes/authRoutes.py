from flask import Blueprint, request, jsonify
import jwt
import os
from models.user import User # type: ignore
from app import db

auth_bp = Blueprint("auth", __name__)
user_model = User(db)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    if user_model.find_user(data["username"]):
        return jsonify({"message": "User already exists"}), 400
    user_model.create_user(data["username"], data["password"])
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    if user_model.verify_password(data["username"], data["password"]):
        token = jwt.encode({"username": data["username"]}, os.getenv("JWT_SECRET"), algorithm="HS256")
        return jsonify({"token": token, "username": data["username"]})
    return jsonify({"message": "Invalid credentials"}), 400