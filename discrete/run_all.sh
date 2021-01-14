#!/bin/sh

N=$1
for script in ./runa.sh ./runc.sh
do
	$script $N
done 

