#!/usr/bin/env bash

if [[ $# == 0 ]]; then
    echo "Please provide the path"
    exit 1
fi

file="$*"
base=$(basename "$file")

printf "%20s: ${file#*.}\n" "Full Extension"
printf "%20s: ${file##*.}\n" "Last Extension"
printf "%20s: ${file##*/}\n" "File name"
if [[ -e $file ]]; then
    if [[ -f $file ]]; then
        printf "%20s: Regular File \n" "$base"
        lsOutput=$(ls -ld "$file")
        declare -a fileInfo
        fileInfo=($lsOutput)
        printf "%20s: %s bytes \n" "$base" ${fileInfo[4]}
        if [[ -x $file ]]; then
            printf "%20s: Executable \n" "$base"
        else
            printf "%20s: NOT Executable \n" "$base"
        fi
        if [[ -r $file ]]; then
            printf "%20s: Readable \n" "$base"
        else
            printf "%20s: NOT Readable \n" "$base"
        fi
        if [[ -w $file ]]; then
            printf "%20s: Writable \n" "$base"
        else
            printf "%20s: NOT Writable \n" "$base"
        fi
    elif [[ -d $file ]]; then
        printf "%20s: Directory \n" "$base"
    elif [[ -b $file ]]; then
        printf "%20s: Block Device \n" "$base"
    elif [[ -h $file ]]; then
        printf "%20s: Symbolic Link \n" "$base"
    elif [[ -c $file ]]; then
        printf "%20s: Character Device \n" "$base"
    fi
else
    printf "%20s: Does NOT exist \n" "$base"
fi
