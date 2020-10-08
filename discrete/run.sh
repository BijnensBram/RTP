#!/bin/sh
make

N=$1
for c in 0.5 1.0
do
	for a in 0.4 0.6 0.8
	do
		((i=i%N)); ((i++==0)) && wait
		./discrete $c $a 0.01 500 2 2 0.05 > right_a_$a\_c$c.txt &
		# ./discrete 0.5 $a 0.01 500 3 2 0.05 > sym_a_$a\_c$c.txt 
		echo $i
	done
done
echo "done right"

for c in 0.5 1.0
do
	for a in 0.4 0.6 0.8
	do
		((i=i%N)); ((i++==0)) && wait
		# ./discrete 0.5 $a 0.01 500 2 2 0.05 > right_a_$a\_c$c.txt 
		./discrete $c $a 0.01 500 3 2 0.05 > sym_a_$a\_c$c.txt &
		echo $i
	done
done
echo "done sym"
