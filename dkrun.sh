#!/bin/sh

docker run -d -v $PWD/nodejs:/app --name nodejs nodetest
