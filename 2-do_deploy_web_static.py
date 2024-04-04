#!/usr/bin/python3
""" deploy a web app to servers """
import os.path
import time
from fabric.api import local
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["100.25.143.95", "54.175.165.203"]

def do_pack():
    """ the function to create the tgz """
    t = time.localtime()
    current_time = time.strftime("%Y%m%d%H%M%S", t)
    name = "versions/web_static_{}.tgz".format(current_time)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(name)).failed is True:
        return None
    return name

def do_deploy(archive_path):
    """ function to deployt the app """

    if os.path.isfile(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    path = "/data/web_static/releases/"

    put(archive_path, "/tmp/{}".format(name))
    run('mkdir -p {}'.format(path))
    run("tar -xzf /tmp/{} -C {}/{}".format(archive_path, path, name))
    run ('rm -rf /data/web_static/current/*')
    run("mv {}{}/web_static/* {}{}".format(path, name, path ,name))
    run('ln -s {}{} /data/web_static/current'.format(path, name))
    return True
