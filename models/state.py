#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    __table_args__ = {'mysql_engine': 'InnoDB'}
    name = Column(String(128), nullable=False)
    # Relatioship with city
    cities = relationship('City', backref='state',
                          cascade='all,delete-orphan')

    def __init__(self, *args, **kwargs):
        """Initialize state"""
        super().__init__(*args, **kwargs)
    @property
    def cities(self):
        from models import storage
        return [city for city in storage.all(City)
                 if city.state_id == self.id]