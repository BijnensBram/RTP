#!/bin/sh
make 

N=$1
for c in 0.5 1.0
do
	for a in 0.4 0.6 0.8
	do
		echo "./discrete $c $a 0.01 500 2 > right_a_$a\_c_$c.txt"
	done
done | parallel -j $N

for c in 0.5 1.0
do
	for a in 0.4 0.6 0.8
	do
		echo "./discrete $c $a 0.01 500 3 > sym_a_$a\_c_$c.txt"
	done
done | parallel -j $N