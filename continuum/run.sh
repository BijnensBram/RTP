#!/bin/sh

for a in 0.4 0.6 0.8
do
	./continuum 0.1 $a 0.001 500 2 0.1 0.005 > right_a_$a\_c01.txt
	./continuum 0.1 $a 0.001 500 3 0.1 0.01 > sym_a_$a\_c01.txt
	echo $a
done
