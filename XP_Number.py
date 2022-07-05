#!/usr/bin/python

import sys

inFile = sys.argv[1]

N = 0


fin = open(inFile, "rt")
#output file to write the result to
fout = open(inFile + "_processed.g", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output fil
    if (line.strip() == 'XP'):
        N += 1
    fout.write(line.replace('XP', 'XP # ' + str(N)))
#close input and output files
fin.close()
fout.close()