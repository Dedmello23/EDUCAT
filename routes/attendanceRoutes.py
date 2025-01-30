from flask import Blueprint, request, jsonify
from models.attendance import Attendance # type: ignore
from app import db

attendance_bp = Blueprint("attendance", __name__)
attendance_model = Attendance(db)

@attendance_bp.route("/add", methods=["POST"])
def add_attendance():
    data = request.json
    attendance_model.add_attendance(data["username"], data["subject"], data["hours"], data["totalHours"])
    return jsonify({"message": "Attendance added successfully"}), 201

@attendance_bp.route("/<username>", methods=["GET"])
def get_attendance(username):
    records = attendance_model.get_attendance(username)
    return jsonify(records)