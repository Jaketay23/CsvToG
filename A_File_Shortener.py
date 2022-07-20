#!/usr/bin/python

import sys
import re
import csv

import pandas as pd
import time
import os
import glob
import os.path


#filename = "/home/kali/Research/HRCL/CSV/Processed/HRCL_dataset_1dos.csv"
#filename = "/home/kali/Research/HRCL/CSV/Processed/HRCL_dataset_bothdos.csv"
#filename = "/home/kali/Research/HRCL/CSV/Processed/HRCL_dataset_3dos.csv"
#filename = "/home/kali/Research/HRCL/CSV/Processed/HRCL_dataset_2dos.csv"
#filename = "/home/kali/Research/HRCL/CSV/Processed/HRCL_dataset_1mirai.csv"
#filename = "/home/kali/Research/HRCL/CSV/Processed/HRCL_dataset_1dos2mirai.csv"
#filename = "/home/kali/Research/HRCL/CSV/Processed/HRCL_dataset_2dos_111222.csv"
#filename = "/home/kali/Research/HRCL/CSV/Processed/HRCL_dataset_2mirai.csv"
#filename = "/home/kali/Research/HRCL/CSV/Processed/HRCL_dataset_2dos2mirai_111222.csv"
#filename = "/home/kali/Research/HRCL/CSV/Processed/HRCL_dataset_1mirai_1dos.csv"
#filename = "/home/kali/Research/HRCL/CSV/Processed/HRCL_full.csv"
#filename = "/home/kali/Research/dataset_copy/Processed/HCRL_full_AttackInfo.csv"





#filename = "/home/kali/Research/data/MIDAS_test/UNSW_NB15.csv"
filename = "/home/kali/Research/MIDAS/data/DARPA/darpa_full.csv"
#filename = "/home/jaketay/Research/data/IoTScenarios/out_91_wlabels.csv"
outputFileName = "/home/kali/Research/data/MIDAS_test/MIDAS_Test.csv"

# # importing pandas package
import pandas as pandasForSortingCSV
#
# csvData = ""
# file = ""
#
# # assign dataset
# csvData = pandasForSortingCSV.read_csv(filename, usecols=['srcip', 'dstip', 'Stime', 'attack_cat', 'Label'], low_memory=False)
# # sort data frame
# csvData.sort_values(["Stime"],
#                     axis=0,
#                     ascending=[True],
#                     inplace=True)
# csvData.to_csv(filename)



for f in glob.glob(outputFileName):
    os.remove(f)
out = open(outputFileName, 'w')

out.write("srcip,dstip,Stime,Label\n")

epoch_time_arr = []

N = 0

gtd_list = []
with open(filename, newline='', encoding='latin1') as rows:
      row_reader = csv.DictReader(rows, delimiter=',')
      file = "UNSW"
      num_records = 0
      counter = 0
      for row in row_reader:
         gtd_list.append(dict(row))
         num_records += 1

         print(num_records)


         if (file == "HCRL"):
             value = row['Source']  ##
         else:
            value = row['srcip']
         if value != "":
             out.write(value)
             out.write(',')

         if (file == "HCRL"):
             value = row['Destination']  ##
         else:
             value = row['dstip']  ##
         if value != "":
             out.write(value)
             out.write(',')

         if (file == "HCRL"):
            value = row['Time']  ##
            if value.__contains__("e"):
                temp = ""
                temp = "0."
                for i in range(0, int(value[-1:])):
                    temp = temp + "0"
                temp = temp + (str(float(value[:value.find("e")])))
                value = temp
                print(value)
            value = value[:value.find('.')]
            #value = int(value)/30
            value = int(value) + 1
         else:
            value = row['Stime']  ##
         # #
         # #
         # #importing the datetime package
         # import datetime
         #
         # if (file == "UNSW"):
         #     # given epoch time
         #     epoch_time = int(value)
         #
         #     # using datetime.fromtimestamp() function to convert epoch time into datetime object
         #     mytimestamp = datetime.datetime.fromtimestamp(epoch_time)
         #
         #     # using strftime() function to convert
         #     datetime_str = mytimestamp.strftime("%Y - %m - %d  %H : %M : %S")
         #     value = datetime_str


         if value != "":
             out.write(str(value))
             out.write(',')

         value = row['Label']  ##
         if value != "":
             out.write(value)
             out.write('\n')

print("Done")
print(num_records)

# if (filename.startswith("/home/kali/Research/data/UNSW-NB15.csv")):
#     file = "UNSW"
#
#     # assign dataset
#     csvData = pandasForSortingCSV.read_csv(filename, usecols = ['srcip','dstip', 'Stime', 'Label'], low_memory=False)
#     # sort data frame
#     csvData.sort_values(["Stime"],
#                         axis=0,
#                         ascending=[True],
#                         inplace=True)

if (filename.startswith("/home/kali/Research/MIDAS/data/DARPA")):
    file = "DARPA"

    # assign dataset
    csvData = pandasForSortingCSV.read_csv(filename, usecols=['srcip', 'dstip', 'Stime', 'Label'], low_memory=False)
    # sort data frame
    csvData.sort_values(["Stime"],
                        axis=0,
                        ascending=[True],
                        inplace=True)



    # assign dataset
    csvData = pandasForSortingCSV.read_csv(filename, usecols=['Source', 'Destination', 'Time', 'Label'], low_memory=False)
    # sort data frame
    csvData.sort_values(["Time"],
                        axis=0,
                        ascending=[True],
                        inplace=True)



#csvData.to_csv(filename)
out.close()
