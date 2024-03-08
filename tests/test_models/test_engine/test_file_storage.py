#!/usr/bin/python3
"""Unittest for FileStorage"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
import os
import json
import models


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
        self.assertEqual(self.storage.all(),
                         self.storage._FileStorage__objects)

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
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_save_with_multiple_models(self):
        """Test that save and reload works with different model types."""
        user = User(email="user@example.com", password="password", first_name="John", last_name="Doe")
        self.storage.new(user)
        city = City(name="San Francisco")
        self.storage.new(city)

        self.storage.save()
        self.storage.reload()

        user_key = f"{User.__name__}.{user.id}"
        city_key = f"{City.__name__}.{city.id}"

        self.assertIn(user_key, self.storage.all())
        self.assertIn(city_key, self.storage.all())

        reloaded_user = self.storage.all()[user_key]
        self.assertEqual(reloaded_user.email, user.email)
        self.assertEqual(reloaded_user.first_name, user.first_name)
        self.assertEqual(reloaded_user.last_name, user.last_name)

        reloaded_city = self.storage.all()[city_key]
        self.assertEqual(reloaded_city.name, city.name)


if __name__ == '__main__':
    unittest.main()
