#!/usr/bin/python3

"""Module containing tests for the File Storage class"""


import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test class for the file storage model"""

    def test_file_path(self):
        """Test that the file path exists and has the correct value"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertEqual(FileStorage._FileStorage__file_path, 'file.json')

    def test_reload(self):
        """Test that objects are loaded into the program"""
        storage = FileStorage()
        base_obj = BaseModel()
        base_obj.name = "Elsa"
        base_obj.age = 22
        base_obj.save()
        storage._FileStorage__objects = {}
        storage.reload()
        self.assertIn(base_obj.id, storage.all())

    def test_save(self):
        """Test that objects are saved to a file in JSON"""
        storage = FileStorage()
        base_obj = BaseModel()
        base_obj.name = "Elsa"
        base_obj.age = 22
        base_obj.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))

if __name__ == '__main__':
    unittest.main()
