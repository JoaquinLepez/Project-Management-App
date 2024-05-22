from app import db

user_task = db.Table("user_task",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("task_id", db.Integer, db.ForeignKey("tasks.id")))

user_team = db.Table("user_team",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("team_id", db.Integer, db.ForeignKey("teams.id")))