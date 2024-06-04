import unittest
from app import create_app, db
from app.models import Task, Team, User
from app.services import TaskService, TeamService, UserService

task_service = TaskService()
team_service = TeamService()
user_service = UserService()

class TaskTeamUserTestCase(unittest.TestCase):

    def setUp(self):
        # Task
        self.NAME_TASK = "prueba número 1"
        self.DESCRIPTION_TASK = "esta es la descripcion de mi prueba número 1"
        self.START_DATE_TASK = "1/1/2024"
        self.DEADLINE_TASK = "28/2/2024"
        self.PRIORITY_TASK = "alta prioridad"
        self.DIFFICULTY_TASK = "elevada"
        self.STATE_TASK = "en proceso"

        # Team
        self.NAME_TEAM = "nombre de equipo"

        # User
        self.USERNAME_USER = 'usuario34'
        self.PASSWORD_USER = '123456'
        self.EMAIL_USER = 'test@test.com'

        # User Data
        self.FIRSTNAME_PRUEBA = 'Joaquin'
        self.LASTNAME_PRUEBA = 'Lepez'
        self.PHONE_PRUEBA = '542604660416'
        self.ADDRESS_PRUEBA = 'Address 1234'
        self.CITY_PRUEBA = 'San Rafael'
        self.COUNTRY_PRUEBA = 'Argentina'

        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_save(self):
        user = self.__get_user()
        user.add_task(self.__get_task())
        user.add_team(Team(name=self.NAME_TEAM))
        user_service.save(user)

        self.assertGreaterEqual(user.id, 1)
        self.assertGreaterEqual(len(user.tasks) , 1)
        self.assertGreaterEqual(len(user.teams) , 1)

    def __get_task(self):
        task = Task()

        task.name = self.NAME_TASK
        task.description = self.DESCRIPTION_TASK
        task.start_date = self.START_DATE_TASK
        task.deadline = self.DEADLINE_TASK
        task.priority = self.PRIORITY_TASK
        task.difficulty = self.DIFFICULTY_TASK
        task.state = self.STATE_TASK

        return task

    def __get_user(self):

        user = User()
        user.username = self.USERNAME_USER
        user.password = self.PASSWORD_USER
        user.email = self.EMAIL_USER

        return user

        