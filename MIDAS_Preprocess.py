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

filename = "/home/jaketay/Research/data/UNSW.csv"

# importing pandas package
import pandas as pandasForSortingCSV

# assign dataset
csvData = pandasForSortingCSV.read_csv(filename)

# sort data frame
csvData.sort_values(["Stime"],
                    axis=0,
                    ascending=[False],
                    inplace=True)


MIDAS = open("../../Research/data/MIDAS_test/DDoS_anoms.csv", 'w')
MIDAS_entries = open ("../../Research/data/MIDAS_test/DDoS_entries.txt", 'w')
anomCheck = open ("../../Research/data/MIDAS_test/anomCheck.txt", 'w')
gtd_list = []
with open(filename, newline='', encoding='latin1') as rows:
      row_reader = csv.DictReader(rows, delimiter=',')
      num_records = 0
      counter = 0
      for row in row_reader:
         gtd_list.append(dict(row))
         num_records += 1

         # if N <= 0:
         #     break
         # N -= 1


         value = row['Label']  ##
         if value != "":
            if value == "0":
                MIDAS.write("0")
            else:
                MIDAS.write("1")
                value = row['srcip']
                if value != "":
                    anomCheck.write(value)
                    anomCheck.write('\n')
            MIDAS.write('\n')


MIDAS_entries.write(str(num_records))
MIDAS_entries.close()
MIDAS.close()
anomCheck.close()