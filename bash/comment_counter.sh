#!/usr/bin/env bash

file=""
if [[ $# != 0 ]]; then
    file="$*"
fi

counter=0
line=0
# counts the number of lines that start with #

if [[ -n $file ]]; then
    while IFS= read -r var ; do
        if [[ $var =~ ^[[:space:]]*#.* ]]; then
            if [[ $line != 0 ]]; then
                (( counter++ ))
            fi
        fi
        (( line++ ))
    done < "$file"
else
    while IFS= read -r var ; do
        if [[ $var =~ ^[[:space:]]*#.* ]]; then
            if [[ $line != 0 ]]; then
                (( counter++ ))
            fi
        fi
        (( line++ ))
    done
fi
echo "Number of comment lines: " $counter
