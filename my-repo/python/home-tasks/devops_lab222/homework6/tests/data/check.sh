#!/bin/bash

for i in $(seq 1 7)
do
    echo "Starting test${i}..."
    rm -f test*.zip
    rm -rf test_new
    cd tests/data/test${i}
    zip -qr ../../../test${i}.zip *
    cd ../../..
    python clean_app.py test${i}.zip

    unzip -qo test${i}_new.zip -d test_new
    if diff tests/data/test${i}_out test_new
    then
        echo "test${i} passed"
    else
        echo "Generated test${i}_new.zip differs from expected output"
        exit 1
    fi
    rm -f test*.zip
    rm -rf test_new
done
