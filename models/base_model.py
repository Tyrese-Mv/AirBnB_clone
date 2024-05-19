#!/usr/bin/python3
"""Base model module"""
import uuid
import datetime
from models import storage

class BaseModel:
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0 :
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
        """returns a string representation of the class

        Returns:
            string: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__
            )

    def save(self):
        """sets new value for the updated time
        """
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance:

        Returns:
            dict: dictionary with value of the instances
        """
        myDict = self.__dict__.copy()
        myDict['__class__'] = self.__class__.__name__
        myDict['updated_at'] = self.updated_at.isoformat()
        myDict['created_at'] = self.created_at.isoformat()
        return myDict
    