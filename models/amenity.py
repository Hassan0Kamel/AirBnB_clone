#!/usr/bin/python3
"""
Defines model
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Blueprint for Amenity objects
    """
    name = ""
