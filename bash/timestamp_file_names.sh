#!/usr/bin/env bash

printf "Enter file name: "
read -r input
timestamp=`date -u +"%Y_%m_%dT%H%M%S"`
echo "${input}_${timestamp}"
