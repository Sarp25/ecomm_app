import hashlib
from storage import load_json, save_json

USERS_FILE= "users.json"

class UserManager:
    def __init__(self):
        self.users= load_json(USERS_FILE, [])

    def _hash_password(self, password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def get_user(self, username):
        for user in self.users:
            if user["username"] ==username:
                return user
        return None

    def register(self, username, password):
        username=username.strip()

        if self.get_user(username):
            return False, "Username already exists."

        if len(password)< 6:
            return False, "Password must be at least 6 characters."

        self.users.append({
            "username": username,
            "password_hash": self._hash_password(password),
            "role": "user"
        })

        save_json(USERS_FILE, self.users)
        return True, "User registered successfully."

    def login(self, username, password):
        user=self.get_user(username)
        if not user:
            return False, "Invalid login."

        if user["password_hash"] !=self._hash_password(password):
            return False, "Invalid login."

        return True, user