class User():
    def __init__(self, id: str, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email
    
    def to_json(self):
        return {
            "username": self.username,
            "email": self.email
        }
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.id
