from app.models import Task
from app import db

class TaskRepository:

    def save(self, task):
        db.session.add(task)
        db.session.commit()
        return task
    
    def update(self, task, id):
        entity = self.find(id)
        entity.name = task.name
        entity.description = task.description
        entity.start_date = task.start_date
        entity.deadline = task.deadline
        entity.priority = task.priority
        entity.difficulty = task.difficulty
        entity.state = task.state
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, task):
        db.session.delete(task)
        db.session.commit()

    def all(self):
        tasks = db.session.query(Task).all()
        return tasks
    
    # Método que muestre todas las task de un project, o todas las task que tiene asignado un user

    def find(self, id):
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Task).filter(Task.id == id).one()
        except:
            return None
        
    def find_by_name(self, name):
        return db.session.query(Task).filter(Task.name == name).one_or_none()
    
