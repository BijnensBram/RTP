#!/bin/sh
make
N=$1

for a in 0.2 0.4 0.6
do
	for c in 0.6 0.9 1.2 1.5
	do
		echo "./discrete $c $a 0.01 500 2 6 0.1 > ./DATA/fitting_c_$c\_a_$a.txt"
	done | parallel -j $N
done
