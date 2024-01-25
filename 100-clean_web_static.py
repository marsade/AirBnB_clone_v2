#!/usr/bin/python3
# This script deletes unneccessary archives
import os.path
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['52.3.245.134', '52.87.154.222']


def do_clean(number=0):
    """Deletes all unnecessary archives"""
    path_remote = "/data/web_static/releases/"
    path_local = "versions"
    number = int(number)
    foldersr = []

    # locate files locally and remotely
    files_local = [os.path.join(path_local, file) for file in os.listdir(
        path_local) if os.path.isfile(os.path.join(path_local, file))]
    res = run("ls -lt {}".format(path_remote))

    # Create deletion list for remote files
    folders_remote = [line.split()[-1] for line in res.stdout.splitlines()[1:]]
    foldersr = [folders for folders in folders_remote if folders.startswith(
        "web_static")]
    sorted_foldesr = sorted(foldersr, reverse=True)

    # Create deletion list for local files
    sorted_filesl = sorted(files_local, key=os.path.getmtime, reverse=True)

    if number <= 0:
        delete_filesl = sorted_filesl[number + 1:]
        delete_filesr = sorted_foldesr[number+ 1:]
    else:
        delete_filesr = sorted_foldesr[number:]
        delete_filesl = sorted_filesl[number:]

    # Delete files
    for file in delete_filesl:
        local("rm -rf {}".format(file))
    for folder in delete_filesr:
        run("rm -rf {}{}".format(path_remote, folder))
