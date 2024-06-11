#!/bin/env bash

VERNUM="v0.1"

if [ -d './dist/colette/' ]; then
	echo "Packing distributable..."
	if [ -d './site/' ]; then
		cp -r ./site ./dist/colette/docs
	fi
	cd ./dist/colette/
	7za a -tzip colette-$VERNUM.zip colette docs/* _internal/*
fi