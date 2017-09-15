#!/bin/bash

# Make sure we have virtualenv configured
source venv3/bin/activate

# cleanup
rm -rf docs

# run lint to check code
pylint ecosystem/*.py test/*.py

# Genrate docs
#pydoc -w *.py
pycco ecosystem/*.py

# Run the unit tests
export PYTHONPATH=test
python -m unittest discover test

# build package for distribution
rm -rf dist/
python setup.py sdist
