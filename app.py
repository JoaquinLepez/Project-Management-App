from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# App
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://joaquin:123456789@localhost:5432/base_prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

    # Database models
class Role(db.Model):
    __tablename__= "roles"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship("User", backref="role")

    def __repr__(self):
        return "<Role %r>" % self.name

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return "<User %r>" % self.username

# Routes
@app.route("/")
def index():
    return "Hola mundo"

# Run configuration
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)






