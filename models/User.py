from pymongo import MongoClient
import bcrypt

class User:
    def _init_(self, db):
        self.users = db["users"]

    def create_user(self, username, password):
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.users.insert_one({"username": username, "password": hashed_pw})

    def find_user(self, username):
        return self.users.find_one({"username": username})

    def verify_password(self, username, password):
        user = self.find_user(username)
        if user:
            return bcrypt.checkpw(password.encode('utf-8'), user["password"])
        return False