#!/bin/sh
make
N=$1
for c in $(seq 0.5 0.1 1.5)
do
	echo "./continuum $c 0.4 0.01 500 2 6 0.1 > ./DATA/fitting_c_$c.txt"
done | parallel -j $N
