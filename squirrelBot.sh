#!/usr/bin/env bash
cd /home/pi/Documents/NUTZ
rm -R data/
mkdir data -m 777
/usr/bin/python3 build_dataset.py