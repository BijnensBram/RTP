#!/bin/sh

for c in 0.5 1.0 1.5 2.0
do
	for a in 0.4 0.6 0.8
	do
		./continuumsmall 0.1 $a 0.001 500 2 0.1 0.005 > ./datafit/right_a_$a\_c_$c.txt
		./continuumsmall 0.1 $a 0.001 500 3 0.1 0.01 > ./datafit/sym_a_$a\_c_$c.txt
		echo $a
	done
done
