#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static

# update the apt install
apt-get update

# Install nginx
if [ "$(command -v nginx)" ]; then
    echo "Nginx is installed."
else
    sudo apt-get install -y nginx
fi

mkdir -p /data/;
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
# Create a fake HTML file /data/web_static/releases/test/index.html
tee /data/web_static/releases/test/index.html <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# a symbolic link to  /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration
tee /etc/nginx/sites-available/default <<EOF
server {
       location /hbnb_static/ {
                alias /data/web_static/current/;
        }
}
EOF
nginx -s reload
