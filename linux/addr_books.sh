#!/usr/bin/env bash

function usage() {
    echo "Usage: "
    echo "To create a database : ./addr_books.sh init"
    echo "To query the database: ./addr_books.sh name joe"
    echo "To list all records: ./addr_books.sh list"
    echo "To insert a record: ./addr_books.sh insert joe 123232 joe@test.com"
    echo "To delete a record: ./addr_books.sh delete name joe"
}

if [[ ! `command -v sqlite3` ]]; then
    echo "No sqlite3 detected. Install one first"
    exit 1
fi

command=${1:-list}

sql=""
shift
case $command in
    init )
        sql="CREATE TABLE addresses (name string, phone string, email string);"
        ;;
    query )
        sql="SELECT name, phone, email FROM addresses WHERE $1 LIKE '$2';"
        ;;
    list )
        if [[ ! -e address.db ]]; then
            usage
        else
            sql="SELECT name, phone, email FROM addresses;"
        fi
        ;;
    insert )
        sql="INSERT INTO addresses (name, phone, email) VALUES ('$1', '$2', '$3');"
        ;;
    delete )
        sql="DELETE FROM addresses WHERE $1 LIKE '$2';"
        ;;
    *)
        usage
        ;;
esac

echo $sql | sqlite3 address.db | sed 's/|/\n/g'