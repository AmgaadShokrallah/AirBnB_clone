#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bmode = BaseModel()
        bmode.id = "123456"
        bmode.created_at = bmode.updated_at = dt
        bmodestr = bmode.__str__()
        self.assertIn("[BaseModel] (123456)", bmodestr)
        self.assertIn("'id': '123456'", bmodestr)
        self.assertIn("'created_at': " + dt_repr, bmodestr)
        self.assertIn("'updated_at': " + dt_repr, bmodestr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bmode = BaseModel()
        sleep(0.05)
        first_updated_at = bmode.updated_at
        bmode.save()
        self.assertLess(first_updated_at, bmode.updated_at)

    def test_two_saves(self):
        bmode = BaseModel()
        sleep(0.05)
        first_updated_at = bmode.updated_at
        bmode.save()
        second_updated_at = bmode.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bmode.save()
        self.assertLess(second_updated_at, bmode.updated_at)

    def test_save_with_arg(self):
        bmode = BaseModel()
        with self.assertRaises(TypeError):
            bmode.save(None)

    def test_save_updates_file(self):
        bmode = BaseModel()
        bmode.save()
        bmodeid = "BaseModel." + bmode.id
        with open("file.json", "r") as f:
            self.assertIn(bmodeid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of BaseModel class."""

    def test_to_dict_type(self):
        bmode = BaseModel()
        self.assertTrue(dict, type(bmode.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bmode = BaseModel()
        self.assertIn("id", bmode.to_dict())
        self.assertIn("created_at", bmode.to_dict())
        self.assertIn("updated_at", bmode.to_dict())
        self.assertIn("__class__", bmode.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bmode = BaseModel()
        bmode.name = "Holberton"
        bmode.my_number = 98
        self.assertIn("name", bmode.to_dict())
        self.assertIn("my_number", bmode.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bmode = BaseModel()
        bmode_dict = bmode.to_dict()
        self.assertEqual(str, type(bmode_dict["created_at"]))
        self.assertEqual(str, type(bmode_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.utcnow()
        bmode = BaseModel()
        bmode.id = "123456"
        bmode.created_at = bmode.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bmode.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bmode = BaseModel()
        self.assertNotEqual(bmode.to_dict(), bmode.__dict__)

    def test_to_dict_with_arg(self):
        bmode = BaseModel()
        with self.assertRaises(TypeError):
            bmode.to_dict(None)


if __name__ == "__main__":
    unittest.main()
