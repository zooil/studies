#!/bin/sh

docker run -d -v $PWD/pyStudies/fastapi:/app -p 5000:8000 --name fastapi fastapitest 
