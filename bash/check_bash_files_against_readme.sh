#!/usr/bin/env bash

ls *.sh | while IFS= read -r line ; do
    grep $line readme.md > /dev/null
    if [[ $? != 0 ]]; then
        echo "Not FOUND: $line"
    fi
done

