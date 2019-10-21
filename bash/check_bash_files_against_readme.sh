#!/usr/bin/env bash

ls *.sh | while IFS= read -r line ; do
    grep $line readme.md > /dev/null
    if [[ $? != 0 ]]; then
        echo "Not FOUND: $line"
    fi
done

# a different method using a one liner
find *.sh -print0 | xargs -I {} -r0 sh -c "grep {} readme.md > /dev/null || echo NOT FOUND: {}"
