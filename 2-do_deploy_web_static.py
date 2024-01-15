#!/usr/bin/python3
# Distributes archives to the web servers
from fabric.api import *
import os.path

env.user = 'ubuntu'
env.hosts = ['54.209.112.112', '52.87.154.222']


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
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(file_name_ne))
        print('New version deployed!')
        return True
    except Exception as e:
        return False
