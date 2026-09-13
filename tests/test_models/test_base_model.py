#!/usr/bin/python3
"""Unittest module for BaseModel."""

import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel."""

    def test_instance(self):
        """Test that BaseModel creates an instance."""
        model = BaseModel()

        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_unique_ids(self):
        """Test that each instance gets a unique ID."""
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertNotEqual(model1.id, model2.id)

    def test_str(self):
        """Test the string representation."""
        model = BaseModel()

        expected = "[BaseModel] ({}) {}".format(
            model.id, model.__dict__
        )

        self.assertEqual(str(model), expected)

    def test_save(self):
        """Test that save updates updated_at."""
        model = BaseModel()
        old_updated_at = model.updated_at

        model.save()

        self.assertGreater(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test conversion to dictionary."""
        model = BaseModel()

        obj_dict = model.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], model.id)
        self.assertEqual(
            obj_dict["created_at"],
            model.created_at.isoformat()
        )
        self.assertEqual(
            obj_dict["updated_at"],
            model.updated_at.isoformat()
        )

    def test_kwargs(self):
        """Test creating BaseModel from a dictionary."""
        model1 = BaseModel()
        model1.name = "Test"

        data = model1.to_dict()
        model2 = BaseModel(**data)

        self.assertEqual(model2.id, model1.id)
        self.assertEqual(model2.name, "Test")
        self.assertEqual(model2.created_at, model1.created_at)
        self.assertEqual(model2.updated_at, model1.updated_at)


if __name__ == "__main__":
    unittest.main()
