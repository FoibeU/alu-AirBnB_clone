#usr/bin/python3
"""Parent class BaseModel"""
from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """
        Parent class 'BaseModel' for AirBnB clone
    """

    def __init__(self, *args, **kwargs):
        """
            Initialize attributes
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
            Save the model instance to the storage engine
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
            Return dictionary with string format
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """
            Return string representation of the model
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
