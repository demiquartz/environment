#!/bin/bash

clean() {
    rm -rf build doc Doxyfile
}

if [ $(cd `dirname $0` && pwd) = `pwd` ]; then
    ( cd . && clean )
else
    clean
fi
