#!/usr/bin/python3
"""Base Class"""
import datetime
import uuid

class BaseModel:
    """Base Model class instatiating public instances"""
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        mydict = self.__dict__
        
        mydict["__class__"] = str(self.__class__.__name__)
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return mydict
    
    