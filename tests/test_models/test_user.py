#!/usr/bin/python3
"""Test case for the User class."""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test case for the User class."""

    def test_attributes(self):
        """Test if the default attributes of User are set correctly."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        """Test if User inherits from BaseModel."""
        user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance(self):
        """Test if the instance is an instance of User and BaseModel."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)


if __name__ == "__main__":
    unittest.main()
