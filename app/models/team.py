from app import db
from app.models.relations import user_team

class Team(db.Model):
    __tablename__ = "teams"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Relaciones con otras tablas

    # Project 1:1
    project = db.relationship("Project", uselist=False, back_populates="team")

    # Users N:M
    users = db.relationship("User", secondary = user_team, back_populates="teams")

