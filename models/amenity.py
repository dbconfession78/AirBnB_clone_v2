#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from os import environ
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""
    if 'HBNB_TYPE_STORAGE' in environ and environ["HBNB_TYPE_STORAGE"] == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "PlaceAmenity", cascade="all,delete-orphan", backref="amenities")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
