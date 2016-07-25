from app.models import User, Role
from app import db,create_app
from flask import current_app
import unittest

class ModelTests(unittest.TestCase):
    def setUp(self):
        # self.app = create_app('testing')
        # self.app_context = self.app.app_context()
        # self.app_context.push()
        # db.create_all()
        pass

    def tearDown(self):
        # db.session.remove()
        # db.drop_all()
        pass

    def test_password_hash_with_correct_password(self):
        user = User()
        user.password = 'dreamcatcher'
        self.assertTrue(user.verify_password('dreamcatcher'), 'Should be true if the password is correct')

    def test_password_hash_with_wrong_password(self):
        u = User()
        u.password = 'dream'
        self.assertFalse(u.verify_password('dreamed'), 'should be false')

    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)
