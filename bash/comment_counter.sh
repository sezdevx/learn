#!/usr/bin/env bash

counter=0
# counts the number of lines that start with #
while IFS= read -r var ; do
    if [[ $var =~ ^[[:space:]]*#.* ]]; then
         (( counter++ ))
    fi
done

echo "Number of comment lines: " $counter
