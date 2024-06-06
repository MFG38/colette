#!/bin/env bash

ROOTDIR=$(pwd)
GENFILES=('todo.clt')

read -p "Deleting Colette-generated files. Are you sure? [y/n] " CHOICE

if [ $CHOICE == 'y' ]; then
	for file in $GENFILES; do
		if [ $(find ./ -iname $file | wc -l) -gt 0 ]; then
			if [ -f $file ]; then
				rm $file
			fi
		fi
	done
elif [ $CHOICE == 'n' ]; then
	echo "Deletion aborted."
fi