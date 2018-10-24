#!/bin/bash

rm -f result

corr=0;

for i in `seq 1 10`; do
    rm -f tempresult
    #./MatrixChain.exe < ./testfiles/t$i >> tempresult
	cat Results/$i.sql | sqlite3 ../TPCH.db >> tempresult
    diff tempresult ./Results/$i.out >> tempcnt
    if [ -s tempcnt ] ; then
      echo "test $i: fail"
      echo "test $i: fail" >> result
    else
      echo "test $i: success"
      echo "test $i: success" >> result
      ((corr=corr+1))
    fi;
done

echo "score: $corr";
echo $(whoami) "score: ${corr}" >> result

rm -f tempresult
rm -f tempcnt

