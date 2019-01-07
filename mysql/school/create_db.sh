#!/usr/bin/env bash

user=${1:?"Provide a user name"}
pass=${2:?"Provide a password"}

mysql -u $user -p$pass <<EOF 2>/dev/null
CREATE DATABASE school;
EOF

if [[ $? == 0 ]]; then
    echo "Created school database"
else
    echo "school database already exists"
fi

mysql -u $user -p$pass school <<EOF 2>/dev/null
CREATE TABLE students(
    id int,
    name varchar(120),
    grade int
);
EOF

if [[ $? == 0 ]]; then
    echo "Created students table"
else
    echo "students table already exists"
fi

mysql -u $user -p$pass school <<EOF
DELETE FROM students;
EOF

while read line; do
    oldIFS=$IFS
    IFS=,
    values=($line)
    data="\"${values[0]}\", \"${values[1]}\", \"${values[2]}\""
    IFS=$oldIFS
    echo "INSERT INTO students VALUES($data);"
    mysql -u $user -p$pass school<<EOF
    INSERT INTO students VALUES($data);
EOF
done < ../../data/school/students.txt

echo "Populated school database"


