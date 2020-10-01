#!/bin/sh
make
for c in 0.5 1 1.5
do
	for a in 0.4 0.6 0.8 
	do
		./discrete $c $a 0.01 500 2 > fitting_c_$c\_a_$a.txt
		echo "c = $c and a = $a"
	done
done

echo "finished"
