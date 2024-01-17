#!/bin/python3
from uuid import uuid4
from datetime import datetime
import models
"""BaseModel that defines all common attributes/methods for other classes"""

class BaseModel:
    """ Base Model """
    def __init__(self, *args, **kwargs):
        """instance initialization"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            format_data ='%Y-%m-%dT%H:%M:%S.%f'
            for key, val in kwargs.items():
                print("> {}\n".format(kwargs[key]))
                #  if key != '__class__':
                #     setattr(self, key, val)
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val,format_data)
                else:
                    self.__dict__[key] = val
        else:
        
            models.storage.new(self)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()


    def to_dict(self):
        """Return a dictionary representation of the object."""
        to_dic = self.__dict__.copy()
        to_dic["created_at"] = self.created_at.isoformat()
        to_dic["updated_at"] = self.updated_at.isoformat()
        to_dic["__class__"] = self.__class__.__name__
        return to_dic

        """
        return {
            
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
        """
    def __str__(self):
        """Return the string representation of the object."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
