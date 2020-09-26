from app import db
from sqlalchemy.sql import func

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(12), unique=True, nullable=False)
    passwd = db.Column(db.String(16), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, name, surname, username, passwd):
        self.name = name
        self.surname = surname
        self.username = username
        self.passwd = passwd

    def __repr__(self):
        return "<Users %r>" % self.username

class Tasks(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(30), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status_tasks.id'))
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime)

    users = db.relationship('Users', foreign_keys=users_id)
    status = db.relationship('Status_Tasks', foreign_keys=status_id)

    def __init__(self, users_id, title, description, status_id):
        self.users_id = users_id
        self.title = title
        self.description = description
        self.status_id = status_id

    def __repr__(self):
        return "<Tasks %r>" % self.id

class Status_Tasks(db.Model):
    __tablename__ = "status_tasks"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(30), nullable=False)

    def __init__(self, status):
        self.status = status

    def __repr__(self):
        return "<Status_Tasks %r>" % self.id