#!/bin/bash 

root=`pwd`

echo version=\'`cat VERSION.txt`\' > sheets_pkg/sheets/version.py

pip3 install .

bash install_daemon.bash


