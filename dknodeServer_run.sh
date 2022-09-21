#!/bin/sh

docker run -d -v $PWD/nodejs/app:/app -p 5000:3000 --name nodejs nodetest
