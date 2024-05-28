import unittest
from app import create_app, db
from app.models import Team

class TeamTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_team(self):
        team = self.__get_team()

        self.assertIsNotNone(team)
    
    def __get_team(self):
        team = Team()

        return team