#!/usr/bin/python3
# Generate a tgz archive containing the content from web_static
from fabric.api import local, runs_once
from datetime import datetime
import os

@runs_once
def do_pack():
    """Archive function"""
    try:
        if not os.path.isdir("versions"):
            os.mkdir("versions")
        now = datetime.now()
        file_name = "webstatic{}{}{}{}{}{}.tgz".format(
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
