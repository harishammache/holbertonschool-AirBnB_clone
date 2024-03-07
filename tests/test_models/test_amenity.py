#!/usr/bin/python3
"""Test case for the Amenity class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test case for the Amenity class."""

    def test_attributes(self):
        """Test if the default attributes of Amenity are set correctly."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance(self):
        """Test if the instance is an instance of Amenity and BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)


if __name__ == "__main__":
    unittest.main()
