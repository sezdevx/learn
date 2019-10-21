#!/usr/bin/env bash

counter=0
line=0
# counts the number of lines that start with #
while IFS= read -r var ; do
    if [[ $var =~ ^[[:space:]]*#.* ]]; then
        if [[ $line != 0 ]]; then
            (( counter++ ))
        fi
    fi
    (( line++ ))
done

echo "Number of comment lines: " $counter
