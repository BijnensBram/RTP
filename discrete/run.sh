#!/bin/sh
make

for i in 0.05 0.2 0.4 0.6 0.8 1.0
do
	./discrete $i 0.5 0.01 500 2 > 2smallc_right_$i.txt 
	echo $i
done
echo "done"

