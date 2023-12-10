#!/usr/bin/python3
"""Base Class"""
import datetime
import uuid
from models import storage


class BaseModel:
    """Base Model class instatiating public instances"""

    def __init__(self, *arg, **kwargs):
        """Instantiate using keyword-arguments, or
        the generic way"""
        if len(kwargs) > 0:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """overrides string representation of the the class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__
            )

    def save(self):
        """saves the object to a json file"""
        storage.save()
        # self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """converts class to a dictionary"""
        mydict = self.__dict__.copy()
        mydict["__class__"] = str(self.__class__.__name__)
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return mydict
