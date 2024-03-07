#!/usr/bin/python3
"""Test case for the Place class."""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test case for the Place class."""

    def test_attributes(self):
        """Test if the default attributes of Place are set correctly."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_inheritance(self):
        """Test if Place inherits from BaseModel."""
        place = Place()
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance(self):
        """Test if the instance is an instance of Place and BaseModel."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)


if __name__ == "__main__":
    unittest.main()
