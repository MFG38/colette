#!/bin/env bash

read -p "Deleting __pycache__. Are you sure? [Y/n] " CHOICE

if [ ! $CHOICE == 'n' ]; then
	cd src/

	if [ -d __pycache__ ]; then
		echo "Cleaning __pycache__..."
		rm -r __pycache__/
	else
		echo "No cache to clean!"
	fi
else
	echo "Deletion aborted."
fi