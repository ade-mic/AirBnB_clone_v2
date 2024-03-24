#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

if models.storage_t == 'db':
    Base = declarative_base()
else:
    Base = object

time_fmt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A base class for all hbnb models"""
    if models.storage_t == "db":
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        # check if kwargs
        if kwargs:
            for key, item in kwargs.items():
                if key != '__class__':
                    setattr(self, key, item)

            if kwargs.get('created_at', None) and type('created_at') is str:
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    time_fmt)
            else:
                self.updated_at = datetime.utcnow
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            # Randomly generate id and then convert to string
            self.id = str(uuid.uuid4())
            # Assign the time when an instance was
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time_fmt)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time_fmt)
        new_dict["__class__"] = self.__class__.__name__
        if '_sa_instance_state' in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """Delete the current instance fronm storage"""
        models.storage.delete(self)
