from app import db
from . import UserData
from app.models.relations import user_task, user_team

class User(db.Model):
    __tablename__ = 'users'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    password: str = db.Column(db.String(255), nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)

    # Relaciones con otras tablas

    # Userdata 1:1
    data = db.relationship('UserData', uselist=False, back_populates='user')

    # Tasks N:M
    tasks = db.relationship("Task", secondary = user_task, back_populates="users")

    # Teams N:M
    teams = db.relationship("Team", secondary = user_team, back_populates="users")

    def __init__(self, user_data: UserData = None):
        self.data = user_data





