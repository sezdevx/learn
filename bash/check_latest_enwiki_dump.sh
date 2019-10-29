#!/usr/bin/env bash

latest="latest_enwiki_dumps.html"
compressed_stats="enwiki-latest-site_stats.sql.gz"
stats="enwiki-latest-site_stats.sql"
function cleanUp()
{
    \rm -f $latest
    \rm -f $compressed_stats
    \rm -f $stats
}

trap cleanUp EXIT
trap cleanUp TERM

if curl -s "https://dumps.wikimedia.org/enwiki/latest/" > "$latest" ; then
    if grep -q $compressed_stats\" "$latest" ; then
        curl -s "https://dumps.wikimedia.org/enwiki/latest/${compressed_stats}" > "$compressed_stats"
        gunzip $compressed_stats
        echo $(grep VALUES $stats | grep -Eo '\(.*\)')
    fi
else
    echo "Couldn't download from https://dumps.wikimedia.org/enwiki/latest/"
fi

