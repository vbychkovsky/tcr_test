#!/bin/sh

(./selftest.py && git commit -am "good" ) || git reset --hard HEAD
