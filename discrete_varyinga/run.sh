#!/bin/sh
make

for e in 0.9 1.0 1.05 1.1 1.2 1.3 1.4
# e=1.05
do
	./discrete 1 $e 0.01 500 2 > 2varyinga_right_e_$e\_c1.txt 
	echo $e
done
./discrete 1 0.9 0.01 500 2 > varyinga_right_e_0.9_c1.txt 
echo "done"

