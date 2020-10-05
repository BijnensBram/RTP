#!/bin/sh
make

for e in 0.55
do
	./discrete 0.5 $e 0.01 500 2 > 2varyinga_right_e_$e\_c0.5.txt 
	./discrete 0.5 $e 0.01 500 2 > varyinga_right_e_$e\_c0.5.txt 
	echo $e
done
echo "done"

