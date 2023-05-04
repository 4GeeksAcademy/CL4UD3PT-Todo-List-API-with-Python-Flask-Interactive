from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    todos = db.relationship('Todo', backref='user')

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(120), unique=False, nullable=False)
    done = db.Column(db.Boolean(), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False, nullable=False)

    def serialize(self):
        return {
            "done": self.done,
            "label": self.label
        }

