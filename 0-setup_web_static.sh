#!/usr/bin/env bash
# a scripts that sets up the web server for deployment of web_static

# installs nginx
sudo apt-get update
sudo apt-get -y install nginx

# creates folder /data
sudo mkdir -p /data/

# creates folder /data/web_static
sudo mkdir -p /data/web_static/

# creates folder /data/web_static/releases
sudo mkdir -p /data/web_static/releases/

# creates folder /data/web_static/shared
sudo mkdir -p /data/web_static/shared/

# creates folder /data/web_static/releases/test/
sudo mkdir -p /data/web_static/releases/test/

# creates a fake HTML file with content
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# creates a symbolink link /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# gives ownership of /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Nginx configuration
sudo sed -i '/listen 80 default/a\ \tlocation /hbnb_static { \n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# restarts nginx
sudo service nginx restart

