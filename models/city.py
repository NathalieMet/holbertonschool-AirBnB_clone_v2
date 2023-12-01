#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ La classe City, contient l'ID de l'état et le nom """

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id', ondelete="CASCADE"),
                      nullable=False)

    places = relationship(
        "Place", backref="city", cascade="all, delete-orphan")
