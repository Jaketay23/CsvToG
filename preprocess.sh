#!/bin/bash

for f in DDoSGraph*
do
	./XP_Number.py $f
	echo "Ran"
done
