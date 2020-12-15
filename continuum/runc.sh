#!/bin/sh
make

N=$1

for c in 
do
	echo "./continuum $c 0.5 0.001 500 1 1.05 0.05 > right_a_$a.txt"
done | parallel -j $N
