#!/bin/bash

#rm testSingle.txt

for testNum in "$@"; do
	#read testNum

	echo "***** Testing Query #$testNum! *****"
	echo "Your query is:\n"
	cat Results/$testNum.sql
	
	printf "\n\n"
	echo "Your output is:"
	#cat Results/$testNum.sql | sqlite3 ../TPCH.db
	#cat Results/$testNum.sql | sqlite3 ../TPCH.db >> testSingle.txt
	
	((cat Results/$testNum.sql) | sqlite3 ../TPCH.db) >> testSingle.txt
	cat testSingle.txt
	
	printf "\n\n"
	echo "The sample output is:"
	cat Results/$testNum.out
	
	printf "\n\nThe difference is:\n"
	#diff cat Results/$testNum.out (cat Results/$testNum.sql | sqlite3 ../TPCH.db)
	git diff <(cat testSingle.txt) <(cat Results/$testNum.out)
done

rm testSingle.txt