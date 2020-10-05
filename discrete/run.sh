#!/bin/sh
make

for a in 0.4 0.6 0.8
do
	./discrete 0.5 $a 0.01 500 2 2 0.05 > right_a_$a\_c0.5.txt 
	./discrete 0.5 $a 0.01 500 3 2 0.05 > sym_a_$a\_c0.5.txt 
	echo $i
done
echo "done"

