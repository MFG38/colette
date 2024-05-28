#!/bin/env bash

ROOTDIR=$(pwd)

read -p "Deleting todo.clt. Are you sure? [y/n] " CHOICE

if [ $CHOICE == 'y' ]; then
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
elif [ $CHOICE == 'n' ]; then
	echo "Deletion aborted."
fi