#!/bin/sh

apt update
apt install -y vim
cd app
pip install -r requirements.txt

while true; do echo "still live"; sleep 1800; done
