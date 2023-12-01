#!/usr/bin/python3
""" Place Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from models.review import Review
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id')),
    Column('amenity_id', String(60), ForeignKey('amenities.id'))
)

class Place(BaseModel, Base):


    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'),
                    nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),
                    nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    """amenities = relationship("amenities", secondary=place_amenity,
                             viewonly=False)"""


    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref='place', cascade="all")
        """amenities = relationship("amenities", secondary=place_amenity,
                             viewonly=False)"""
    else:
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances
              with place_id equals to the current Place.id"""
            from models import storage
            return [review for review in storage.all(Review).values()
                if review.place_id == self.id]

        """@property
        def amenities(self):"""
        """Getter attribute that returns the list of amenities instances
              with place_id equals to the current Place.id"""
        """from models import storage
            return [amenity for amenity in storage.all(Review).values()
                if amenity.place_id == self.id]"""

        """@amenities.setter
        def amenities(self, amenity):
        # Setter attribute that handles appending Amenity IDs
        # Accepts only Amenity objects, appends their IDs to amenity_ids
            if isinstance(amenity, amenity):
                self.amenity_ids.append(amenity.id)"""

