#!/usr/bin/python3
# Archives and deploys archives to the web servers
import os.path
from datetime import datetime
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['52.3.245.134', '52.87.154.222']


def do_pack():
    """Archive function

    Returns:
        path to archive
    """
    try:
        if not os.path.isdir("versions"):
            os.mkdir("versions")
        now = datetime.now()
        file_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day,
            now.hour, now.minute, now.second
        )
        print("Packing web_static to versions/web_static_{}".format(file_name))
        local("tar -cvzf versions/{} web_static".format(file_name))
        dir = "versions/{}".format(file_name)
        size = os.stat(dir).st_size
        print("web_static packed: {} -> {} Bytes".format(dir, size))
        return "versions/{}".format(file_name)
    except Exception as e:
        print("Error: {}".format(e))
        return None


def do_deploy(archive_path):
    """Deploys to the web servers"""
    try:
        if not os.path.isfile(archive_path):
            return False
        file_name = os.path.basename(archive_path)
        file_name_ne = file_name.strip('.tgz')
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(file_name_ne))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            file_name, file_name_ne))
        run('rm /tmp/{}'.format(file_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}'.format(
            file_name_ne, file_name_ne
        ))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            file_name_ne))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(file_name_ne))
        print('New version deployed!')
        return True
    except Exception as e:
        return False


def deploy():
    try:
        new_archive = do_pack()
        stat = do_deploy(new_archive)
        return stat
    except Exception as e:
        return False
