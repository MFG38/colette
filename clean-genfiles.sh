#!/bin/env bash

ROOTDIR=$(pwd)

if [ -f 'todo.clt' ]; then
	rm todo.clt
fi

for dir in */; do
	cd $dir
	if [ -f 'todo.clt' ]; then
		rm todo.clt
	fi
	cd $ROOTDIR
done