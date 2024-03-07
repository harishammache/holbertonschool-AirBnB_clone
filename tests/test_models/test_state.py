#!/usr/bin/python3
"""Test case for the State class."""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test case for the State class."""

    def test_attributes(self):
        """Test if the default attributes of State are set correctly."""
        state = State()
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        """Test if State inherits from BaseModel."""
        state = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance(self):
        """Test if the instance is an instance of State and BaseModel."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)


if __name__ == "__main__":
    unittest.main()
