#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Creates a .tgz archive from web_static folder."""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        local("tar -cvzf {} web_static".format(archive_path))

        if os.path.exists(archive_path):
            return archive_path
        else:
            return None
    except Exception as e:
        return None
