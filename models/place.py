#!/usr/bin/python3
""" Place Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from models.review import Review
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True)
)

class Place(BaseModel, Base):
    """class place"""

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'),
                    nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),
                    nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                                  viewonly=False)
    else:
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances
              with place_id equals to the current Place.id"""
            from models import storage
            return [review for review in storage.all(Review).values()
                if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter attribute that returns the list of amenities instances
              with place_id equals to the current Place.id"""
            from models import storage
            from models.amenity import Amenity
            return [amenity for amenity in storage.all(Amenity).values()
                if amenity.place_id == self.id]

        @amenities.setter
        def amenities(self, obj):
            """setter for amenity"""
            from models.amenity import Amenity
            if obj and isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

