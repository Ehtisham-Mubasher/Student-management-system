class User:
    def __init__(self, user_id=None, username=None, password_hash=None, role='admin'):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.role = role

    def __repr__(self):
        return f"<User(username={self.username}, role={self.role})>"
