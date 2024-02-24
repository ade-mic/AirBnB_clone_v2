#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
Base = declarative_base()



class BaseModel(Base):
    """A base class for all hbnb models"""
    __abstract__ = True
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        # check if kwargs
        if kwargs:
            for key, item in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        self.__dict__[key] = datetime.datetime.strptime(
                            item, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = item
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
        dictionary = {}
        dictionary.update(self.__dict__)
        if '_sa_instance_state' in dictionary:
            dictionary.pop('_sa_instance_state', None)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
    
    def delete(self):
        """Delete the current instance fronm storage"""
        from models import storage
        storage.delete(self)
