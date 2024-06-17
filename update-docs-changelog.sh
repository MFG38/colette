#!/bin/env bash

echo "Updating changelog in docs/..."
cp CHANGELOG.md docs/changelog.md
sed -i -e "s/##/###/g" docs/changelog.md