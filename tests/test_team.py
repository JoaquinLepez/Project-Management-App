import unittest
from app import create_app, db
from app.models import Team
from app.services import TeamService

team_service = TeamService()

class TeamTestCase(unittest.TestCase):

    def setUp(self):

        self.NAME_PRUEBA = "nombre de equipo"

        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_team(self):
        team = Team(name= self.NAME_PRUEBA)

        self.assertIsNotNone(team)
        self.assertEqual(team.name, self.NAME_PRUEBA)
    
    def test_team_save(self):
        team = Team(name= self.NAME_PRUEBA)
        team_service.save(team)

        self.assertGreaterEqual(team.id,1)
        self.assertEqual(team.name, self.NAME_PRUEBA)
    
    def test_team_delete(self):
        team = Team(name= self.NAME_PRUEBA)
        team_service.save(team)

        team_service.delete(team)
        self.assertIsNone(team_service.find(team.id))
    
    def test_team_all(self):
        team = Team(name= self.NAME_PRUEBA)
        team_service.save(team)

        teams = team_service.all()
        self.assertGreaterEqual(len(teams), 1)
    
    def test_team_find(self):
        team = Team(name= self.NAME_PRUEBA)
        team_service.save(team)

        team_find = team_service.find(1)
        self.assertIsNotNone(team_find)
        self.assertEqual(team_find.id, team.id)
    
    def test_team_find_by_name(self):
        team = Team(name= self.NAME_PRUEBA)
        team_service.save(team)

        team_find = team_service.find_by_name(team.name)
        self.assertIsNotNone(team_find)
        self.assertEqual(team_find.id, team.id)