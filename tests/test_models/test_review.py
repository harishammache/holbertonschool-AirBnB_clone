#!/usr/bin/python3
"""Test case for the Review class."""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test case for the Review class."""

    def test_attributes(self):
        """Test if the default attributes of Review are set correctly."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.texte, "")

    def test_inheritance(self):
        """Test if Review inherits from BaseModel."""
        review = Review()
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance(self):
        """Test if the instance is an instance of Review and BaseModel."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)


if __name__ == "__main__":
    unittest.main()
