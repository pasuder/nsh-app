#!/bin/sh
cd $(dirname $0)
python -m python.test.runtests "$@"
