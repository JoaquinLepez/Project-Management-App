from app import db
from app.models.relations import user_team

class Team(db.Model):
    __tablename__ = "teams"

    # Atributos propios
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), nullable=False)

    # Relaciones con otras tablas
    # Project 1:1
    project = db.relationship("Project", uselist=False, back_populates="team")

    # Users N:M
    users = db.relationship("User", secondary = user_team, back_populates="teams")

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
    
    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)