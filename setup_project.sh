#!/bin/bash

virtualenv -p python3 venv
source venv/bin/activate
git clone https://github.com/vrachieru/samsung-tv-api.git
pip3 install ./samsung-tv-api

