#!/bin/bash
# script tested on Ubuntu 18.04.3 LTS using Python 3.6.9

# update pip
pip install -U pip

# update python packages
pip install -r requirements.txt

# pull latest stable version of ESOtoonBuilder
git pull origin master
