#!/usr/bin/env python3
""" fabric script to generates a tgz archive """
import os.path
import time
from fabric.api import local


def do_pack():
    """ the function to create the tgz """
    t = time.localtime()
    current_time = time.strftime("%Y%m%d%H%M%S", t)
    name = "versions/web_static_{}.tgz".format(current_time)
    local("mkdir -p versions")
    local("tar -cvcf {} web_static".format(name))
    return name
