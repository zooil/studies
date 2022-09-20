#!/bin/sh

isNoneImg=$(docker images -f "dangling=true" -q)
echo $isNoneImg
if [ $isNoneImg ]
then
	docker rmi $isNoneImg
fi
