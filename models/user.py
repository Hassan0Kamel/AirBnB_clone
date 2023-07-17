#!/usr/bin/python3
"""
Class User BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Blueprintobject
    Public Attributes engine
    folder to manage User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
