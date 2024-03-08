#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static

# update the apt install
sudo apt-get update

# Install nginx
if [ "$(command -v nginx)" ]; then
    echo "Nginx is installed."
else
    sudo apt-get install -y nginx
fi

sudo mkdir -p /data/;sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
# Create a fake HTML file /data/web_static/releases/test/index.html
sudo tee /data/web_static/releases/test/index.html <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# a symbolic link to  /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration
sudo tee /etc/nginx/sites-available/default <<EOF
server {
       location /hbnb_static/ {
                alias /data/web_static/current/;
        }
}
EOF
service nginx restart
