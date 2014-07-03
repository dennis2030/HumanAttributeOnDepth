#!/bin/bash

for f in $(find GT/ -name '*_GT.txt');do
    ./splitTo5Fold.py ${f}
done

