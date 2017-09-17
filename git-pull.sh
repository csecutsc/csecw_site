#!/bin/bash
echo "Pulling from git development branch"
git pull origin development
echo "going into virtual env"
source flask/bin/activate
echo "making database migrations"
python db_migrate.py
echo "stopping nginx"
sudo systemctl stop nginx
echo "restarting csec uWSGI worker"
sudo systemctl restart csec
echo "starting nginx"
sudo systemctl start nginx
  
