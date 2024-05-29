import unittest
from app import create_app, db
from app.models import Task
from app.services import TaskService

task_service = TaskService()

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

        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_task(self):
        
        task = self.__get_task()

        self.assertEqual(task.name, self.NAME_PRUEBA)
        self.assertEqual(task.description, self.DESCRIPTION_PRUEBA)
        self.assertEqual(task.start_date, self.START_DATE_PRUEBA)
        self.assertEqual(task.deadline, self.DEADLINE_PRUEBA)
        self.assertEqual(task.priority, self.PRIORITY_PRUEBA)
        self.assertEqual(task.difficulty, self.DIFFICULTY_PRUEBA)
        self.assertEqual(task.state, self.STATE_PRUEBA)
    
    def test_task_save(self):
        task = self.__get_task()

        task_service.save(task)

        self.assertGreaterEqual(task.id,1)
        self.assertEqual(task.name, self.NAME_PRUEBA)
        self.assertEqual(task.description, self.DESCRIPTION_PRUEBA)
        self.assertEqual(task.start_date, self.START_DATE_PRUEBA)
        self.assertEqual(task.deadline, self.DEADLINE_PRUEBA)
        self.assertEqual(task.priority, self.PRIORITY_PRUEBA)
        self.assertEqual(task.difficulty, self.DIFFICULTY_PRUEBA)
        self.assertEqual(task.state, self.STATE_PRUEBA)

    def test_task_delete(self):
        task = self.__get_task()
        task_service.save(task)

        task_service.delete(task)
        self.assertIsNone(task_service.find(task.id))
    
    def test_task_all(self):
        task = self.__get_task()
        task_service.save(task)

        tasks = task_service.all()
        self.assertGreaterEqual(len(tasks), 1)

    def test_task_find(self):
        task = self.__get_task()
        task_service.save(task)

        task_find = task_service.find(1)
        self.assertIsNotNone(task_find)
        self.assertEqual(task_find.id, task.id)
    
    def test_task_find_by_name(self):
        task = self.__get_task()
        task_service.save(task)

        task_find = task_service.find_by_name(task.name)
        self.assertIsNotNone(task_find)
        self.assertEqual(task_find.id, task.id)

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
