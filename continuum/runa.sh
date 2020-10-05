#!/bin/sh
make
for a in 0.4 0.6 0.8
do
	./continuum 0.5 $a 0.001 500 1 2 0.05 > right_a_$a.txt
	./continuum 0.5 $a 0.001 500 2 2 0.05 > sym_a_$a.txt
	echo $a
done
echo "finished"
