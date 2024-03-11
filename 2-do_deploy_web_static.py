#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers,
using the function do_deploy
"""

def do_deploy(archive_path):
    """
    Prototype: def do_deploy(archive_path):
    Returns False if the file at the path archive_path doesn’t exist
    The script should take the following steps:
    Upload the archive to the /tmp/ directory of the web server
    Uncompress the archive to the folder
    /data/web_static/releases/<archive filename without extension>
    on the web server
    Delete the archive from the web server
    Delete the symbolic link /data/web_static/current
    from the web server
    Create a new the symbolic link /data/web_static/current
    on the web server, linked to the new version of your code
    (/data/web_static/releases/<archive filename without extension>)
    All remote commands must be executed on your both web servers
    (using env.hosts = ['<IP web-01>', 'IP web-02']
    variable in your script)
    Returns True if all operations have been done correctly,
    otherwise returns False
    You must use this script to deploy it on your servers:
    xx-web-01 and xx-web-02
    """
    
    from fabric.api import *
    import os
    import sys

    env.hosts = ["54.85.90.192", "54.237.14.81"]
    env.username = sys.argv[-1]
    env.key_filename = sys.argv[-3]

    if  not os.path.exists(archive_path):
        return False
    try:
        # upload the archive to /tmp/ directory of the web servers
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/<filename>
        filename = os.path.basename(archive_path)
        filename_no_ext = os.path.splitext(filename)[0]
        release_folder = "/data/web_static/releases/{}".format(filename_no_ext)
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
