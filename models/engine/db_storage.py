#!/usr/bin/python3
""""""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """com"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')  # Default to 'localhost' if not set
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user, passwd, host, db),
                           pool_pre_ping=True)

        if env == 'test':
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                      expire_on_commit=False))

    def all(self, cls=None):
        """com"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

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
        from models.base_model import Base
        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
