"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
Base = declarative_base()


class DBStorage:
    """This class manages storage of hbnb models in MySQL database
    using sqlalchemy orm as abstraction
    """
    __engine = None
    __session = None


    def __init__(self):
        """Instantiate the DBStorage class."""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"\
                                      .format(user, password, host, db),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects by class name.
        If cls=None, query all types.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
        objects = []
        if cls:
            objects.extend(self.__session.query(cls).all())
        else:
            clss = [State, City]  # Assuming these are your mapped classes
            for cls in clss:
                objects.extend(self.__session.query(cls).all())
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objects}


    def new(self, obj):
        """
        add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and the current
        database session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
