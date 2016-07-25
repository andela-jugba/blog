import unittest
from flask import current_app
from app import db, create_app


class TestAppCreation(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        pass

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        pass

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_current_config_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])