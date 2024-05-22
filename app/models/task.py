from app import db
from app.models.relations import user_task

class Task(db.Model):
    __tablename__ = "tasks"

    # Atributos propios
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), nullable=False)
    description: str = db.Column(db.String(80), nullable=False)
    start_date: str = db.Column(db.String(80), nullable=False)
    deadline: str = db.Column(db.String(80), nullable=False)
    priority: str   = db.Column(db.String(80), nullable=False)
    difficulty: str = db.Column(db.String(80), nullable=False)
    state: str = db.Column(db.String(80), nullable=False)
    # ForeignKey de la tabla Users
    project_id: int = db.Column(db.Integer, db.ForeignKey("projects.id"))

    # Relaciones con otras tablas

    # Projects 1:N
    project = db.relationship("Project", back_populates="tasks")

    # Users N:M
    users = db.relationship("User", secondary = user_task, back_populates="tasks")

    