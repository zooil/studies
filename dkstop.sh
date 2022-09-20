#!/bin/sh

# ./dkstop.sh <containerName>
# ./dkstop.sh nodejs

docker stop $1
docker container rm $1

isNoneImg=$(docker images -f "dangling=true" -q)
echo $isNoneImg
if [ $isNoneImg ]
then
        docker rmi $isNoneImg
fi
