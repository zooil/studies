#!/bin/sh

apk add vim
cd app
npm install
while true; do echo "still live"; sleep 1800; done
