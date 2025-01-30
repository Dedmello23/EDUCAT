class Attendance:
    def _init_(self, db):
        self.attendance = db["attendance"]

    def add_attendance(self, username, subject, hours, total_hours):
        self.attendance.insert_one({
            "username": username,
            "subject": subject,
            "hours": hours,
            "totalHours": total_hours
        })

    def get_attendance(self, username):
        return list(self.attendance.find({"username": username}, {"_id": 0}))