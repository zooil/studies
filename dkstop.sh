#!/bin/sh

docker stop nodejs
docker container rm nodejs
docker rmi $(docker images -f "dangling=true" -q)
