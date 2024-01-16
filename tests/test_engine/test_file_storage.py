#!/usr/bin/python3

"""Module containing tests for the File Storage class"""

import unittest
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """ Test class for the file storage model"""

    @classmethod
    def setUp(self):
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = file.json

    def setUpClass(self):
        self.my_model = BaseModel()

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(sefl):
        bsm = BaseModel()
        models.storage.new(bsm)
        self.assertIn("BaseModel" + bsm.id, models.storage.all().keys())
        self.assertIn(bsm, models.storage.all().values())

    def test_reload(self):
        bsm = BaseModel()
        models.storage.new(bsm)
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel" + bsm.id, objs)

    def test_save(self):
        bsm = BaseModel()
        models.storage.new(bsm)
        save_text = ""
        with open("file.json", "r") as r:
            save_text = r.read()
            self.assertIn("BaseModel", + bsm.id, save_text )


if __name__ == '__main__':
    unittest.main()
