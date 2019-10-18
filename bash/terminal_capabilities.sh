#!/usr/bin/env bash

tput smcup
clear
echo "Processing...."
sleep 1
read -n1 -p "Press any key to continue..."

tput rmcup
echo "Restored the screen"