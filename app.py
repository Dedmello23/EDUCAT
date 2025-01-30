from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from routes.auth_routes import auth_bp # type: ignore
from routes.attendance_routes import attendance_bp # type: ignore
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["attendanceDB"]

# Register Blueprints (API Routes)
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(attendance_bp, url_prefix="/attendance")


if __name__ == "_main_":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)

@app.route('/calculate_attendance', methods=['POST'])
def calculate_attendance():
    data = request.json  
    hours_conducted = data.get('hours_conducted')  
    total_hours = data.get('total_hours') 
    
    if total_hours == 0: 
        return jsonify({'error': 'Total hours cannot be zero.'}), 400
    
    
    attendance = (hours_conducted / total_hours) * 100
    

    return jsonify({'attendance': round(attendance, 2)})


if _name_ == '_main_':
    app.run(debug=True)