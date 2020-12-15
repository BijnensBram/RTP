#!/bin/sh
make 

N=$1
for c in 0.05 0.2 0.4 0.6 0.8 1.0 2.0 3.0 4.0 5.0
do
	echo "./discrete $c 0.5 0.01 500 4 0.05 > right_c_$c.txt"
done | parallel -j $N
