#!/bin/bash
echo "Pulling from git development branch"
git pull origin development
echo "stopping nginx"
sudo systemctl stop nginx
echo "stopping gunicorn"
sudo systemctl stop gunicorn
echo "starting gunicorn"
sudo systemctl start gunicorn
echo "starting nginx"
sudo systemctl start nginx
  
