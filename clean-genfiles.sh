#!/bin/env bash

ROOTDIR=$(pwd)

read -p "Deleting todo.clt. Are you sure? [Y/n] " CHOICE

if [ ! $CHOICE == 'n' ]; then
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
else
	echo "Deletion aborted."
fi