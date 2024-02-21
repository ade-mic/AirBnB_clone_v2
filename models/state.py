#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        super().__init__(self, *args, **kwargs)
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # Relatioship with city
    cities = relationship('City', backref='state', cascade='all,delete-orphan')

    @property
    def cities(self):
        from models import storage
        return [city for city in storage.all('City')
                 if city.state_id == self.id]