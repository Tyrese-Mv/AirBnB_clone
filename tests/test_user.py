#!/usr/bin/python3
import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Unit test for User Class"""
    
    
    def test_instance_creation(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attributes_assignment(self):
        user_data = {
            'id': '123',
            'created_at': '2023-01-01T12:00:00',
            'updated_at': '2023-01-01T12:30:00',
            'email': 'musa@gmail.com',
            'password': 'abc',
            'first_name': 'Musa',
            'last_name': 'Mvuna'
        }
        user = User(**user_data)
        self.assertEqual(user.id, '123')
        self.assertEqual(user.created_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(user.updated_at, datetime(2023, 1, 1, 12, 30, 0))
        self.assertEqual(user.email, 'musa@gmail.com')
        self.assertEqual(user.password, 'abc')
        self.assertEqual(user.first_name, 'Musa')
        self.assertEqual(user.last_name, 'Mvuna')

    def test_to_dict_method(self):
        user_data = {
            'id': '456',
            'created_at': '2023-02-01T08:00:00',
            'updated_at': '2023-02-01T09:00:00',
            'email': 'WTC@wethinkcode.com',
            'password': 'secret',
            'first_name': 'WTC',
            'last_name': 'LMS'
        }
        user = User(**user_data)
        user_dict = user.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', 'email', 'password', 'first_name', 'last_name', '__class__']
        self.assertCountEqual(user_dict.keys(), expected_keys)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
