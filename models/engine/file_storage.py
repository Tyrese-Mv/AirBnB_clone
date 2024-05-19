#!/usr/bin/python3
"""File storage class"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all objects save in class variable"""
        return self.__objects

    def new(self, obj):
        """formats and stores dictionary to a json file"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key not in self.__objects:
            self.__objects[key] = obj

    def deserialise(self):
        """imports and returns a class based on a list
        of classes"""
        from models.base_model import BaseModel
        otherClassImports = {
            "BaseModel": BaseModel,
        }
        return otherClassImports

    def save(self):
        """saves the dictionary to the json file"""
        with open(self.__file_path, "w", encoding="utf-8") as file:
            empty_dict = {k: v.to_dict() for k, v, in self.__objects.items()}
            json.dump(empty_dict, file, indent=4)

    def reload(self):
        """loads information from the file to the class variable
        when the application starts"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                myDict = json.load(file)
                emptyDict = {
                        key: self.deserialise()[val["__class__"]](**val)
                        for key, val in myDict.items()
                    }
                self.__objects = emptyDict
        except FileNotFoundError:
            pass
