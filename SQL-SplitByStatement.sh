#!/bin/bash

# Check if a filename was passed as input before running
if [ -z "$1" ]
    then
        echo "Please pass in the sql filename you want to parse as the first argument"
        exit
fi

# This block will separate your sql file by semicolon and drop the statements in 1.sql ascending.
CNT=0
while read -r -d ";" line; do
    let "CNT++"
    echo "$line;" > $CNT.sql
done < "$1"