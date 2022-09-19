#!/bin/sh
# dkbuild <dir> <DockerImageName>
# ex) dkbuild nodejs/app nodetest

echo $PWD
echo "change " $1
cd $1
echo $PWD

docker build -t $2 .
