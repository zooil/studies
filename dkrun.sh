#!/bin/sh

docker run -d -v $PWD/nodejs/app:/app -p 3000:3000/tcp --name nodetest nodeexpress
