#!/usr/bin/python3
"""
Create a unique Fition
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
