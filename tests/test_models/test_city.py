#!/usr/bin/python3
"""Test case for the City class."""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test case for the City class."""

    def test_attributes(self):
        """Test if the default attributes of City are set correctly."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_inheritance(self):
        """Test if City inherits from BaseModel."""
        city = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_instance(self):
        """Test if the instance is an instance of City and BaseModel."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)


if __name__ == "__main__":
    unittest.main()
