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
        put(archive_path, "/tmp/")
        run('mkdir -p {}{}'.format(path, name))
        run("tar -xzf /tmp/{} -C {}{}/".format(file, path, name))
        run("rm /tmp/{}".format(file))
        run("mv {}{}/web_static/* {}{}".format(path, name, path, name))
        run('rm -rf {}{}/web_static'.format(path, name))
        run('rm -rf /data/web_static/current/')
        run('ln -s {}{} /data/web_static/current'.format(path, name))
        return True
    except Exception:
        return False
