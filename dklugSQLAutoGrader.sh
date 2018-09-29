#!/bin/bash

# This block runs all of the .sql files and makes a corresponding .out file
for i in $(ls); do
    DB=./TPCH.db
    EXTENSION="${i##*.}"
    FILENAME="${i%.*}"
    if [ $EXTENSION = "sql" ]
        then
            echo $i
            sqlite3 $DB <./$i > $FILENAME.out
    fi
done

# This block compares the new .out files with the .out solution files stored in ./lab3-results
for i in $(ls); do
    EXTENSION="${i##*.}"
    FILENAME="${i%.*}"
    if [ $EXTENSION = "out" ]
        then
            echo $i
            DIFFERENCE= diff $i ./lab3-results/$FILENAME.out
            echo $DIFFERENCE
            echo
            echo /===========================================================/
            echo
    fi
done