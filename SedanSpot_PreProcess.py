import sys
import re
import csv

import pandas as pd
import time
import os
import glob
import os.path
from os import path
import datetime

anomaly_count = 0

filename = "/home/jaketay/Research/data/MIDAS_test/MIDAS_Test.csv"
#filename = "/home/jaketay/Research/MIDAS/"


Sedan = open("/home/jaketay/Desktop/sedanspot-master/example/sd1.csv", 'w')
values = []
count = 0

gtd_list = []
with open(filename, newline='', encoding='latin1') as rows:
      row_reader = csv.DictReader(rows, delimiter=',')
      num_records = 0
      counter = 0
      for row in row_reader:
         gtd_list.append(dict(row))

         # value = row['Flow Duration']  ##
         value = row['Stime']

         #IoT
         value = value[21:]

         # #DARPA
         # value = value[:-6]
         # if (value in values):
         #    value = values.index(value)
         # else:
         #    values.append(value)
         #    value = count
         #    count += 1


         Sedan.write(str(value))
         Sedan.write(',')

         value_dst = row['dstip']
         Sedan.write(value_dst)
         Sedan.write(',')

         value = row['srcip']
         Sedan.write(value)
         Sedan.write(',')

         Sedan.write('1')
         Sedan.write(',')
         
         


         value = row['Label']  ##
         if value != "":
            # #if value == "BENIGN":
            # if value == "0":
            #     Sedan.write("0")
            # else:
            #     Sedan.write("1")
            Sedan.write(value)
            Sedan.write('\n')

Sedan.close()