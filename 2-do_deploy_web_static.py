#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ["54.85.90.192", "54.237.14.81"]
env.username = "ubuntu"

def do_deploy(archive_path):
    """Distributes an archive to a web servers."""
    if  not os.path.exists(archive_path):
        return False
    try:
        # upload the archive to /tmp/ directory of the web servers
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/<filename>
        filename = os.path.basename(archive_path)
        filename_no_ext = os.path.splitext(filename)[0]
        release_folder = = "/data/web_static/releases/{}".format(filename_no_ext)
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(filename, release_folder))

        # Delete the archive from the web servers
        run("rm /tmp/{}".format(filename))

        # Delete the symbolic link /data/web_static/current
        run('rm -f /data/web_static/current')

        # Create a new symbolic link /data/web_static/current linked
        run('ln -s {} /data/web_static/current'
            .format(release_folder))

        return True
    except Exception as e:
        return False
