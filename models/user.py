#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
Base = declarative_base()


class User(BaseModel, Base):
    __tablename__ = 'users'
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
