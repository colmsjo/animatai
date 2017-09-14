#!/bin/bash

# Make sure we have virtualenv configured
source venv3/bin/activate

# cleanup
rm -rf docs

# run lint to check code
pylint ecosystem/*.py test/*.py

# Genrate docs
#pydoc -w *.py
pycco *.py

# Run the unit tests
python -m unittest discover test

# build package for distribution
python setup.py sdist
