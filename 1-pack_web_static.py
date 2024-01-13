#!/usr/bin/python3
# Generate a tgz archive containing the content from web_static
from fabric.api import *
from datetime import datetime


def do_pack():
    """Archive function"""
    try:
        now = datetime.now()
        file_name = "webstatic{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day,
            now.hour, now.minute
        )
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(file_name))
        return "versions/{}".format(file_name)
    except Exception as e:
        return None
