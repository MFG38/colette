#!/bin/env bash

BUILDARGS=""
read -p "Clean PyInstaller cache and temp files before building? " CLEAN
read -p "Skip confirmation dialogs? " NOCONFIRM

if [ $CLEAN == 'y' ]; then
	BUILDARGS+=" --clean"
fi

if [ $NOCONFIRM == 'y' ]; then
	BUILDARGS+=" --noconfirm"
fi

echo "Final command: pyinstaller $(BUILDARGS) --onedir src/main.py"
read -p "Build Colette with this command? " BUILDWITHCMD

if [ $BUILDWITHCMD == 'y' ]; then
	pyinstaller $BUILDARGS --onedir --name colette src/main.py

	if [ $? -ne 0 ]; then
		echo "Application build failed. Make sure that pyinstaller is installed."
	fi
elif [ $BUILDWITHCMD == 'n' ]; then
	echo "Application build skipped."
fi

read -p "Rebuild documentation? [y/n]" RBDOCS

if [ $RBDOCS == 'y' ]; then
	mkdocs build

	if [ $? -ne 0 ]; then
		echo "Documentation (re)build failed. Make sure that mkdocs is installed."
	fi
elif [ $RBDOCS == 'n' ]; then
	echo "Documentation (re)build skipped."
fi