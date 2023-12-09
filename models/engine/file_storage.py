#!/usr/bin/python3
"""File storage class"""
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key not in self.__objects:
            self.__objects[key] = obj

    def deseriaReload(self):
        from models.base_model import BaseModel
        otherClassImports = {
            "BaseModel": BaseModel
        }
        return otherClassImports

    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as file:
            empty_dict = {k: v.to_dict() for k, v, in self.__objects.items()}
            # for key, value in empty_dict.items():
            #     # print(f"key: {key}")
            #     class_name, obj_id = key.split('.')
            #     obj = self.all(self)[key]
            #     empty_dict[key] = obj
            # # print("Before Dumping")
            # # print(empty_dict)
            json.dump(empty_dict, file, indent=4)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                # for key, value in data.items():
                #     class_name, obj_id = key.split('.')
                #     obj = BaseModel(**value)
                #     self.__objects[key] = obj
                myDict = json.load(file)
                # print("******before overwriting __object*****")
                # print(myDict)
                # print()
                emptyDict = {
                        key: self.deseriaReload()[val["__class__"]](**val)
                        for key, val in myDict.items()
                    }  # To Note!!!!!!!!!!!!!!
                self.__objects = emptyDict
                # print("******after overwriting __object*****")
                # print(self.__objects)
        except FileNotFoundError:
            pass
