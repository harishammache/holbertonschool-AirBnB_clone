#!/usr/bin/python3
"""Unittest for class FileStorage"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up method for FileStorage tests."""
        self.storage = FileStorage()
        self.model = BaseModel()
    
    def tearDown(self):
        """Tear down method for FileStorage tests."""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)
    
    def test_all(self):
        """Test that all returns the __objects dictionary."""
        self.assertEqual(self.storage.all(), self.storage._FileStorage__objects)
    
    def test_new(self):
        """Test that new adds an object to __objects."""
        self.storage.new(self.model)
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())
    
    def test_save(self):
        """Test that save properly saves objects to file."""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        with open(self.storage._FileStorage__file_path, 'r') as f:
            objdict = json.load(f)
            key = f"{self.model.__class__.__name__}.{self.model.id}"
            self.assertIn(key, objdict)
    
    def test_reload(self):
        """Test that reload properly loads objects from file."""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())
    

    if __name__ == "__main__":
        unittest.main()
