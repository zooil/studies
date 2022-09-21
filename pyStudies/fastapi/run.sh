#!/bin/sh

apt update
apt install vim
pip install -r requirements.txt

while true; do echo "still live"; sleep 1800; done
