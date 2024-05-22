import unittest
from app import create_app, db
from app.models import Project, Task

class ProjectTasteCase(unittest.TestCase):

    def setUp(self):
        
        # Project
        self.NAME_PRUEBA = "mi proyecto"
        self.DESCRIPTION_PRUEBA = "esta es la descripcion de mi proyecto"
        self.START_DATE_PRUEBA = "1/1/2024"
        self.DEADLINE_PRUEBA = "28/2/2024"
        self.STATE_PRUEBA = "en proceso"

        # Task 1
        self.TASK1_NAME_PRUEBA = "prueba número 1"
        self.TASK1_DESCRIPTION_PRUEBA = "esta es la descripcion de mi prueba número 1"
        self.TASK1_START_DATE_PRUEBA = "1/1/2024"
        self.TASK1_DEADLINE_PRUEBA = "28/2/2024"
        self.TASK1_PRIORITY_PRUEBA = "alta prioridad"
        self.TASK1_DIFFICULTY_PRUEBA = "elevada"
        self.TASK1_STATE_PRUEBA = "en proceso"

        # Task 2
        self.TASK2_NAME_PRUEBA = "prueba número 2"
        self.TASK2_DESCRIPTION_PRUEBA = "esta es la descripcion de mi prueba número 2"
        self.TASK2_START_DATE_PRUEBA = "1/1/2028"
        self.TASK2_DEADLINE_PRUEBA = "28/2/2028"
        self.TASK2_PRIORITY_PRUEBA = "baja prioridad"
        self.TASK2_DIFFICULTY_PRUEBA = "baja"
        self.TASK2_STATE_PRUEBA = "to do"

        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_project(self):
        
        project = self.__get_project()

        db.session.add(project)
        db.session.commit()

        self.assertTrue(project.name, self.NAME_PRUEBA)
        self.assertTrue(project.description, self.DESCRIPTION_PRUEBA)
        self.assertTrue(project.start_date, self.START_DATE_PRUEBA)
        self.assertTrue(project.deadline, self.DEADLINE_PRUEBA)
        self.assertTrue(project.state, self.STATE_PRUEBA)
        self.assertIsNotNone(project.tasks[0])
        self.assertIsNotNone(project.tasks[1])

    def __get_project(self):

        task1 = Task()
        task1.name = self.TASK1_NAME_PRUEBA
        task1.description = self.TASK1_DESCRIPTION_PRUEBA
        task1.start_date = self.TASK1_START_DATE_PRUEBA
        task1.deadline = self.TASK1_DEADLINE_PRUEBA
        task1.priority = self.TASK1_PRIORITY_PRUEBA
        task1.difficulty = self.TASK1_DIFFICULTY_PRUEBA
        task1.state = self.TASK1_STATE_PRUEBA

        task2 = Task()
        task2.name = self.TASK2_NAME_PRUEBA
        task2.description = self.TASK2_DESCRIPTION_PRUEBA
        task2.start_date = self.TASK2_START_DATE_PRUEBA
        task2.deadline = self.TASK2_DEADLINE_PRUEBA
        task2.priority = self.TASK2_PRIORITY_PRUEBA
        task2.difficulty = self.TASK2_DIFFICULTY_PRUEBA
        task2.state = self.TASK2_STATE_PRUEBA

        project = Project()
        project.name = self.NAME_PRUEBA
        project.description = self.DESCRIPTION_PRUEBA
        project.start_date = self.START_DATE_PRUEBA
        project.deadline = self.DEADLINE_PRUEBA
        project.state = self.STATE_PRUEBA

        project.tasks.append(task1)
        project.tasks.append(task2)

        return project
    

if __name__ == '__main__':
    unittest.main()
