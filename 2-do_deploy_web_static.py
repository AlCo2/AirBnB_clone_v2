#!/usr/bin/python3
""" deploy a web app to servers """
import os.path
from fabric.api import env, run, put

env.hosts = ["100.25.143.95", "54.175.165.203"]


def do_deploy(archive_path):
    """ function to deployt the app """

    if os.path.isfile(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/{}".format(name))
        run('mkdir -p {}'.format(path))
        run("tar -xzf /tmp/{} -C {}/{}".format(archive_path, path, name))
        run('rm -rf /data/web_static/current/*')
        run("mv {}{}/web_static/* {}{}".format(path, name, path, name))
        run('ln -s {}{} /data/web_static/current'.format(path, name))
        return True
    except Exception:
        return False
