#!/usr/bin/env bash


length=${#USER}
x=$((15-length))
SPACE=''
for (( i=0; i < $x ; i++ )); do
    SPACE="$SPACE "
done
cat <<End-of-Message
                   _________________
           .--H--.|             jgs |
         _//_||  ||  $USER${SPACE}|
        [    -|  |'--;--------------'
        '-()-()----()"()-------()"()'
End-of-Message

declare -a names
declare -a values
while read name value; do
    echo "$name = $value"
    names+=($name)
    values+=($value)
done <<EOF
name1 value1
name2 value2
name3 value3
name4 value4
name5 value5
name6 value6
EOF

echo "${names[*]}"
echo "${values[*]}"

OUT="/tmp/ljask_output_kjasm.txt"
cat <<EOF >$OUT
  This is a sample here document
  The output file's name: $OUT
EOF
cat $OUT
\rm -rf $OUT
cat <<'EOF' >$OUT
  This is a sample here document
  The output file's name can not be printed here: $OUT
EOF
cat $OUT
\rm -rf $OUT

exec 9<<EOF
  This is an interesting here document
  The output file's name: $OUT
EOF
cat <&9 >$OUT
cat $OUT
\rm -rf $OUT

tee $OUT <<EOF >/dev/null
  This is a here document outputted to $OUT with tee command
EOF
cat $OUT
\rm -rf $OUT

tee $OUT <<EOF
  This is a here document outputted to $OUT and STDOUT with tee command
EOF
cat $OUT
\rm -rf $OUT

