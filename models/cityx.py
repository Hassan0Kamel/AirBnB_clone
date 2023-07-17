#!/usr/bin/python3
"""
Defines model
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Blueprint objects
    """
    state_id = ""
    name = ""
