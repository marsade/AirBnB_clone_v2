#!/usr/bin/python3
# Generate a tgz archive containing the content from web_static
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Archive function"""
    try:
        if not os.path.isdir("versions"):
            os.mkdir("versions")
        now = datetime.now()
        file_name = "webstatic{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day,
            now.hour, now.minute
        )
        local("tar -cvzf versions/{} web_static".format(file_name))
        return "versions/{}".format(file_name)
    except Exception as e:
        return None
