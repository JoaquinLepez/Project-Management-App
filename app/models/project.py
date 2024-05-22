from app import db

class Project(db.Model):
    __tablename__ = "projects"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    start_date: str = db.Column(db.String(80), nullable=False)
    deadline: str = db.Column(db.String(80), nullable=False)
    state: str = db.Column(db.String(80), nullable=False)
    # ForeignKey de la tabla Team
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    
    # Relaciones con otras tablas
    # Team 1:1
    team = db.relationship("Team", back_populates="project", uselist=False)
    # Task 1:N
    tasks = db.relationship("Task", back_populates="project")


