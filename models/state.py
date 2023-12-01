#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ La classe State """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            from models import storage
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]
"""class State(BaseModel, Base):

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
            cities = relationship('City', backref='state',
                                  cascade='all')
    else:
        @property
        def cities(self):
            from models import storage
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]"""
