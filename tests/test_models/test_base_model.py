#!/usr/bin/python3
"""Unittest for the task 3"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """unittest for the class base model"""

    def test_init(self):
        """Test the initialization of BaseModel."""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertEqual(type(model.id), str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertLessEqual(model.created_at, model.updated_at)

    def test_unique_id(self):
        """Test that each instance has a unique ID."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_string_representation_content(self):
        """Test that the string representation has the correct content."""
        model = BaseModel()
        string_repr = str(model)
        expected_repr = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(string_repr, expected_repr)

    def test_save(self):
        """Test the save method of BaseModel."""
        model = BaseModel()
        model.created_at = model.updated_at
        model.save()
        self.assertNotEqual(model.created_at, model.updated_at)
        self.assertGreater(model.updated_at, model.created_at)

    def test_to_dict(self):
        """Test that the values in the dictionary"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())

    def test_init_with_kwargs(self):
        """ Test initialization with kwargs """
        kwargs = {
            'id': '123456',
            'name': 'Test',
            'created_at': '2023-03-01T12:00:00.000',
            'updated_at': '2023-03-01T13:00:00.000'
        }
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, '123456')
        self.assertEqual(obj.name, 'Test')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.created_at, datetime(2023, 3, 1, 12, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 3, 1, 13, 0, 0))


class TestFileStorage(unittest.TestCase):
    """Unittest for class FileStorage"""

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


if __name__ == '__main__':
    unittest.main()
