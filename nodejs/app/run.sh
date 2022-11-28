#!/bin/sh

apk add vim
apk add grep
cd app
npm install
#node app.js
while true; do echo "still live"; sleep 1800; done
