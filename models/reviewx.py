#!/usr/bin/python3
"""
Defines model
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Blueprint objects
    """
    user_id = ""
    place_id = ""
    text = ""
