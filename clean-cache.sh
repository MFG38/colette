#!/bin/env bash

read -p "Deleting __pycache__. Are you sure? [y/n] " CHOICE

if [ $CHOICE == 'y' ]; then
	cd src/

	if [ -d __pycache__ ]; then
		echo "Cleaning __pycache__..."
		rm -r __pycache__/
	else
		echo "No cache to clean!"
	fi
elif [ $CHOICE == 'n' ]; then
	echo "Deletion aborted."
fi