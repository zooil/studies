#!/bin/sh

#docker run -d -v $PWD/nodejs:/app --name nodejs nodetest
docker run -p 5000:3000 --name nodejs nodetest
