import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
