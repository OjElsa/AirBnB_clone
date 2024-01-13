#!/usr/bin/python3

"""Module containing tests for the BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""
    @classmethod

    def setUpClass(self):
        """create an instance for the BaseModel class"""
        pass

    def test_id(self):
        """test BaseModel id"""
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.assertIsInstance(self.obj1, BaseModel)
        self.assertTrue(hasattr(self.obj1, "id"))
        self.assertIsInstance(self.obj1.id, str)
        self.assertNotEqual(self.obj1, self.obj2)

    def test_create_at(self):
        """test created_at property"""
        self.bsm_created_at = BaseModel()
        self.assertIsInstance(self.bsm_created_at, BaseModel)
        self.assertTrue(hasattr(self.bsm_created_at, "created_at"))
        self.assertIsInstance(self.bsm_created_at.created_at, datetime)

    def test_updated_at(self):
        """test updated_at property"""
        self.bsm_updated_at = BaseModel()
        self.assertIsInstance(self.bsm_updated_at, BaseModel)
        self.assertTrue(hasattr(self.bsm_updated_at, "updated_at"))
        self.assertIsInstance(self.bsm_updated_at.updated_at, datetime)

    def test_str(self):
        """test __str__ function"""
        self.bsm_str = BaseModel()
        self.assertIsInstance(self.bsm_str, BaseModel)
        self.assertTrue(hasattr(BaseModel.__dict__, "__str__"))
        self.maxDiff = None
        expected_str = "[{}] ({}) {}".format(
                    self.bsm_str.__class__.__name__,
                    self.bsm_str.id,
                    {k: v for k, v in self.bsm_str.__dict__.items() if k != 'updated_at'}
                )
        actual_str = str(self.bsm_str)
        print(expected_str)
        print(actual_str)
        print(self.bsm_str.updated_at)
        print(datetime.strptime(actual_str.split('\'updated_at\': ')[1].split(',')[0], "'%Y-%m-%d %H:%M:%S.%f'"))
        self.assertEqual(expected_str, actual_str)

    def test_to_dict(self):
        """test to_dict method"""
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue("to_dict" in dir(BaseModel))
        self.bsm_dict = BaseModel().to_dict()
        self.assertIsInstance(self.bsm_dict, dict)
        self.assertTrue("id" in self.bsm_dict)
        self.assertTrue("created_at" in self.bsm_dict)
        self.assertTrue("updated_at" in self.bsm_dict)
        self.assertTrue("__class__" in self.bsm_dict)
        self.assertEqual(self.bsm_dict["__class__"], "BaseModel")
        self.assertIsInstance(self.bsm_dict["created_at"], str)
        self.assertIsInstance(self.bsm_dict["updated_at"], str)

    def test_save(self):
        """ test save() method"""
        save_obj = BaseModel()
        updated_time = save_obj.updated_at
        save_obj.save()
        self.assertLess(updated_time, save_obj.updated_at)
