#!/usr/bin/env bash

logFile=${1:-/var/log/auth.log}

tmpFile=$(mktemp -u /tmp/failed_users.XXXXXX)

function cleanUp()
{
    \rm $tmpFile
}

trap cleanUp EXIT
trap cleanUp TERM

grep "Failed pass" $logFile > $tmpFile

users=$(cat $tmpFile | awk '{print $(NF-5) }' | sort | uniq)
ips="$(egrep -o "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" $tmpFile | sort | uniq)"

if [[ -n $ips ]]; then
    for ip in $ips; do
        echo $ip
    done
    for user in $users; do
        echo $user
    done
else
    echo "No failed attempt"
fi