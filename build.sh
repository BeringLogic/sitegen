#!/bin/env bash

echo "Building the site from markdown in content/ using basepath /sitegen/ in order to be publishes on github pages."
python3 src/main.py /sitegen/

