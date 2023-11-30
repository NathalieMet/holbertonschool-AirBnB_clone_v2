#!/usr/bin/python3
""""""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """com"""
        hbnb_dev = os.environ.get('HBNB_MYSQL_USER')
        hbnb_dev_pwd = os.environ.get('HBNB_MYSQL_PWD')
        localhost = os.environ.get('HBNB_MYSQL_HOST', 'localhost')  # Default to 'localhost' if not set
        hbnb_dev_db = os.environ.get('HBNB_MYSQL_DB')
        hbnb_env = os.environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(hbnb_dev, hbnb_dev_pwd, hbnb_dev_db),
                           pool_pre_ping=True)

        if hbnb_env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                      expire_on_commit=False))

        def all(self, cls=None):
            """com"""
            objects = {}
            if cls:
                query_result = self.__session.query(cls).all()
            else:
                query_result = []
                for model_cls in [User, State, City, Amenity, Place, Review]:
                    query_result.extend(self.__session.query(model_cls).all())

            for obj in query_result:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
            return objects

        def new(self, obj):
            """Add the object to the current database session"""
            self.__session.add(obj)

        def save(self):
            """Commit all changes of the current database session"""
            self.__session.commit()

        def delete(self, obj=None):
            """Delete obj from the current database session if not None"""
            if obj:
                self.__session.delete(obj)

        def reload(self):
            """Create all tables and the current database session"""
            Base.metadata.create_all(bind=self.__engine)
            Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
            self.__session = Session()
