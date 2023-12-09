#!/usr/bin/python3
"""Unit tests for base_model.py"""

import unittest
import os
import time
from datetime import datetime, timedelta
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        storage.reload()

    def test_instantiation(self):
        result_model = BaseModel()
        self.assertIsInstance(result_model, BaseModel)
        self.assertTrue(hasattr(result_model, 'id'))
        self.assertTrue(hasattr(result_model, 'created_at'))
        self.assertTrue(hasattr(result_model, 'updated_at'))
        self.assertIsInstance(result_model.created_at, datetime)
        self.assertIsInstance(result_model.updated_at, datetime)

    def test_to_dict(self):
        result_model = BaseModel().to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertCountEqual(result_model.keys(), expected_keys)
        self.assertEqual(result_model['__class__'], 'BaseModel')
        self.assertIn('__class__', result_model)
        self.assertIn('id', result_model)
        self.assertIn('created_at', result_model)
        self.assertIn('updated_at', result_model)

    def test_datatype(self):
        result_model = BaseModel().to_dict()

        self.assertEqual(str, type(result_model["id"]))
        self.assertEqual(str, type(result_model["created_at"]))
        self.assertEqual(str, type(result_model["updated_at"]))
        self.assertEqual(str, type(result_model["__class__"]))

    def test_str_representation(self):
        result_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            result_model.id,
            result_model.__dict__
            )
        self.assertEqual(str(result_model), expected_str)

    def test_initialization_with_keyword_arguments(self):
        data = {
            'id': '123',
            'created_at': '2022-01-01T12:00:00',
            'updated_at': '2023-01-01T16:00:00'
        }
        result_model = BaseModel(**data)
        self.assertEqual(result_model.id, '123')
        self.assertEqual(
            result_model.created_at,
            datetime(2022, 1, 1, 12, 0, 0)
            )
        self.assertEqual(
            result_model.updated_at,
            datetime(2023, 1, 1, 16, 00, 0)
            )

    # def test_attribute_modification(self):
    #     model = BaseModel()
    #     original_updated_at = model.updated_at
    #     model.created_at -= timedelta(days=1)
    #     time.sleep(5)
    #     model.save()
    #     self.assertNotEqual(model.updated_at, original_updated_at)
