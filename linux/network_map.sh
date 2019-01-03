#!/usr/bin/env bash

# to check available machines in a local network

for ip in 192.168.0.{1..255} ; do
    ping $ip -c 2 &> /dev/null ;

    if [ $? -eq 0 ]; then
    echo "$ip is up"
    fi
done
#wait