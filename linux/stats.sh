#!/usr/bin/env bash

: ${1?"Usage: $0 /path/to/file"}

file=$1

stat -c '%a permissions %n' $file
stat -c '%A permissions %n' $file
stat -c '%u %U owns %n' $file
stat -c '%s bytes %n' $file
stat -c '%b blocks %n' $file
stat -c '%B size in bytes for each block %n' $file
stat -c 'file type: %F %n' $file
stat -c 'group: %g %G %n' $file
stat -c '%h hard links %n' $file
stat -c '%m mount point %n' $file
stat -c '%i inode %n' $file
stat -c '%w created %n' $file
stat -c '%x last accessed %n' $file
stat -c '%x last modified %n' $file
stat -c '%x last status change %n' $file
