#!/usr/bin/python3
"""Defines the FileStorage class."""

import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary containing all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize all objects to the JSON file."""
        objects_dict = {}

        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file to the storage dictionary."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                objects_dict = json.load(file)

            from models.base_model import BaseModel

            for key, obj_dict in objects_dict.items():
                self.__objects[key] = BaseModel(**obj_dict)

        except FileNotFoundError:
            pass
