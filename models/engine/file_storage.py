#!/usr/bin/python3
"""File storage class"""
import json
import os
 
class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        if key not in self.__objects:
            self.__objects[key] = obj.to_dict()
        print("New method on file storage")
        i = 0
        for keys in self.__objects:
            i+=1
            print("{}. {}".format(i, self.__objects[keys]))
            print()
            print()
        print("______________________objects")
        
    
    
    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as file:
            empty_dict = {k: v for k, v in FileStorage.__objects.items()}
            for key, value in empty_dict.items():
                print(f"key: {key}")
                class_name, obj_id = key.split('.')
                obj = FileStorage.all(self)[key]
                empty_dict[key] = obj
            json.dump(empty_dict, file, indent=4)
    
    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                # for key, value in data.items():
                #     class_name, obj_id = key.split('.')
                #     obj = BaseModel(**value)
                #     self.__objects[key] = obj
                myDict = json.load(file)
                emptyDict = {k: val for k, val in myDict.items()}
                FileStorage.__objects = emptyDict
        except FileNotFoundError:
            pass
        