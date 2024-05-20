#!/bin/env bash

cd src/

if [ -d __pycache__ ]; then
	echo "Cleaning __pycache__..."
	rm -r __pycache__/
else
	echo "No cache to clean!"
fi