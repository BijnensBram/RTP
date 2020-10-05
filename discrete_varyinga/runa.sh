#!/bin/sh
make 

for i in 0.4 0.6 0.8
do
	./discrete 1 $i 0.01 500 3 > sym_$i.txt 
	echo $i
done
echo "done"
