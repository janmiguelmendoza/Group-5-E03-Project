import hashlib
import os

class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = self.hash_password(password)
    
    def hash_password(self, password):
        salt = os.urandom(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + hashed_password
    
    def check_password(self, stored_password, provided_password):
        salt = stored_password[:16]
        stored_hashed_password = stored_password[16:]
        provided_hashed_password = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
        return stored_hashed_password == provided_hashed_password

    def save(self, db):
        db.execute('INSERT INTO user (id, name, email, password, role) VALUES (?, ?, ?, ?, ?)',
                   (self.user_id, self.name, self.email, self.password, 'admin'))
    
    def delete(self, db):
        db.execute('DELETE FROM user WHERE id = ?', (self.user_id,))
    
    def login(self, db):
        user = db.fetchone('SELECT * FROM user WHERE email = ?', (self.email,))
        if user and self.check_password(user[3], self.password):
            return user
        return None
    
    def logout(self):
        pass
