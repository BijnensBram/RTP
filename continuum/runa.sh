#!/bin/sh
make

N=$1

for a in 0.4 0.6 0.8
do
	echo "./continuum 1 $a 0.001 500 1 1.05 0.05 > right_a_$a.txt"
	echo "./continuum 1 $a 0.001 500 2 1.05 0.05 > sym_a_$a.txt"
done | parallel -j $N
