#!/usr/bin/python3
"""This file instantiate
a “switch” will allow you to change storage
type directly by using an environment variable
"""
import os
storage_t = getenv("HBNB_TYPE_STORAGE")


if storage_t = "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_Storage import FileStorage
    storage = FileStorage()

storage.reload()
