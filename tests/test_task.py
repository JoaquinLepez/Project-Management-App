import unittest
from app import create_app, db
from app.models import Task

class TaskTasteCase(unittest.TestCase):

    def setUp(self):
        
        # Task
        self.NAME_PRUEBA = "prueba número 1"
        self.DESCRIPTION_PRUEBA = "esta es la descripcion de mi prueba número 1"
        self.START_DATE_PRUEBA = "1/1/2024"
        self.DEADLINE_PRUEBA = "28/2/2024"
        self.PRIORITY_PRUEBA = "alta prioridad"
        self.DIFFICULTY_PRUEBA = "elevada"
        self.STATE_PRUEBA = "en proceso"

        # Project
        self.PROJECT_NAME_PRUEBA = "mi proyecto"
        self.PROJECT_DESCRIPTION_PRUEBA = "esta es la descripcion de mi proyecto"
        self.PROJECT_START_DATE_PRUEBA = "1/1/2024"
        self.PROJECT_DEADLINE_PRUEBA = "28/2/2024"
        self.PROJECT_STATE_PRUEBA = "en proceso"

        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_project(self):
        
        task = self.__get_task()

        self.assertTrue(task.name, self.NAME_PRUEBA)
        self.assertTrue(task.description, self.DESCRIPTION_PRUEBA)
        self.assertTrue(task.start_date, self.START_DATE_PRUEBA)
        self.assertTrue(task.deadline, self.DEADLINE_PRUEBA)
        self.assertTrue(task.priority, self.PRIORITY_PRUEBA)
        self.assertTrue(task.difficulty, self.DIFFICULTY_PRUEBA)
        self.assertTrue(task.state, self.STATE_PRUEBA)

    def __get_task(self):

        task = Task()
        task.name = self.NAME_PRUEBA
        task.description = self.DESCRIPTION_PRUEBA
        task.start_date = self.START_DATE_PRUEBA
        task.deadline = self.DEADLINE_PRUEBA
        task.priority = self.PRIORITY_PRUEBA
        task.difficulty = self.DIFFICULTY_PRUEBA
        task.state = self.STATE_PRUEBA

        return task
    

if __name__ == '__main__':
    unittest.main()
