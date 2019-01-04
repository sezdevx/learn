#!/usr/bin/env bash

steps=10
sleep_time=1

for ((i=0; i < steps; i++)); do
    \ps -eocomm,pcpu | egrep -v '(0.0)|(%CPU)' >> /tmp/ps_cpu_usage.$$
    sleep $sleep_time
done

function cleanUp()
{
    \rm /tmp/ps_cpu_usage.$$
}

trap cleanUp EXIT
trap cleanUp TERM

cat /tmp/ps_cpu_usage.$$ | \
awk ' { ps[$1]+= $2; }
END{
  for(i in ps)
  {
    printf("%-20s %s\n",i, ps[i]) ;
  }
}' | sort -nrk 2 | head
