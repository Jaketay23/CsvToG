#!/usr/bin/python

import sys
import re
import csv

import pandas as pd
import time
import os
import glob
import os.path


filename = "/home/jaketay/Research/Possible_Dataset/copies/HRCL_dataset.csv"
# filename = "/home/jaketay/Research/MIDAS/data/DARPA/UNSW.csv"
#filename = "/home/jaketay/Research/MIDAS/data/DARPA/darpa_try.csv"
#filename = "/home/jaketay/Research/data/IoTScenarios/out_91_wlabels.csv"
outputFileName = "/home/jaketay/Research/data/MIDAS_test/MIDAS_Test.csv"

# importing pandas package
import pandas as pandasForSortingCSV

# assign dataset
csvData = pandasForSortingCSV.read_csv(filename, dtype='unicode')

# # sort data frame
# csvData.sort_values(["Time"],
#                     axis=0,
#                     ascending=[True],
#                     inplace=True)
#

# # sort data frame
# csvData.sort_values(["Stime"],
#                     axis=0,
#                     ascending=[True],
#                     inplace=True)

csvData.to_csv(filename)

for f in glob.glob(outputFileName):
    os.remove(f)
out = open(outputFileName, 'w')

out.write("srcip,dstip,Stime,Label\n")
gtd_list = []
with open(filename, newline='', encoding='latin1') as rows:
      row_reader = csv.DictReader(rows, delimiter=',')
      num_records = 0
      counter = 0
      for row in row_reader:
         gtd_list.append(dict(row))
         num_records += 1
         #print(row['Source'])
         # N += 1
         # if (N%1000 == 0):
         #     print("Still Running")

         value = row['Source']  ##
         #value = row['srcip']
         if value != "":
             out.write(value)
             out.write(',')

         value = row['Destination']  ##
         #value = row['dstip']  ##
         if value != "":
             out.write(value)
             out.write(',')

         value = row['Time']  ##
         # value = row['Stime']  ##
         value = value[:value.find('.')]
         # # print(value)
         val = int(value) / 15
         # #
         # #
         # #importing the datetime package
         # import datetime
         #
         # # given epoch time
         # epoch_time = int(value)
         #
         # # using datetime.fromtimestamp() function to convert epoch time into datetime object
         # mytimestamp = datetime.datetime.fromtimestamp(epoch_time)
         #
         # # using strftime() function to convert
         # datetime_str = mytimestamp.strftime("%Y - %m - %d  %H : %M : %S")

         if value != "":
             out.write(value)
             # out.write(datetime_str)
             out.write(',')

         value = row['Label']  ##
         if value != "":
             # if "Benign" in value:
             #    out.write('0')
             # else:
             #     out.write('1')
             out.write(value)
             out.write('\n')

print("Done")
print(num_records)
out.close()
