#!/bin/bash


python3 -m venv canvas_drawer_test_venv
source canvas_drawer_test_venv
pip install --upgrade pip
pip install -r requirements.txt

python -m unittest


python -m unittest domain/test/operations_tests.py


testReturn=$?

exit $testReturn
#exit 0