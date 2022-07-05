#
# This script converts the GTD CSV file to graph increments by day
#
# NOTE: The format of the resulting graph input files is for SUBDUE (not GBAD)
#
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

#####################################################################################
#
# Set the modification time of a given filename to the given mtime.
# mtime must be a datetime object.
#
#####################################################################################
def datetime_to_timestamp(dt):
   return time.mktime(dt.timetuple()) + dt.microsecond/1e6

def set_file_modification_time(filename, mtime):
   stat = os.stat(filename)
   atime = stat.st_atime
   os.utime(filename, (atime, datetime_to_timestamp(mtime)))


filename = "/home/jaketay/Research/data/DoS_TCP.csv"
for f in glob.glob("*.g"):
    os.remove(f)

# Create a different increment file for each set of rows with the same date
 #
file_increment_number = 0
increment_number = 1
row_count = 1         # Create a different increment file for each set of rows with the same date
source_port_num = 3
dest_port_num = 5
prev_year = "0"
prev_month = "0"
prev_day = "0"
prev_minute = "0"
prev_second = "0"
prev_hour = "0"
undirected_edge = "u"
directed_edge = "d"
#
eventid_list = []
related_events_list = []


#Clear File
# shortenedFile = open("../../Research/data/MIDAS_test/DDoS_WO_Headers.csv", "w")
# shortenedFile.close()
MIDAS = open("../../Research/data/MIDAS_test/DDoS_anoms.csv", 'w')

N = 10
# with open(filename, "r") as file:
#     counter = 0
#     for line in file:
#         shortenedFile = open("DDoSshort.csv", "w")
#         print("Writing to new Shortened file")
#         shortenedFile.write(line)
#         print(line)
#         counter += 1
#         if counter == N: break

# shortenedFile.close()
# shortenedFileRead = open("DDoSshort.csv", "r")
# print(shortenedFileRead.read())

# outputFile = open("DDoSGraph.g", "w")

N = 10
gtd_list = []
with open(filename, newline='', encoding='latin1') as rows:
      row_reader = csv.DictReader(rows, delimiter=',')
      num_records = 0
      counter = 0
      for row in row_reader:
         gtd_list.append(dict(row))
         num_records += 1
         counter += 1
         # if counter == N:
         #     break
         increment_number = 1
         vertex_number = 1
         #

         # month = row['timestamp'][0:4]
         # day = row['eventid'][4:6].lstrip('0')
         # year = row['eventid'][6:8].lstrip('0')
         #
         hour = row['Timestamp'][11:13]
         minutes = row['Timestamp'][14:16].lstrip('0')
         seconds = row['Timestamp'][17:19].lstrip('0')


         print(prev_hour + prev_minute)
         print(hour + minutes)

         #
         if hour != prev_hour or hour != prev_minute or minutes:
             prev_hour = hour
             prev_minute = minutes
             #file_increment_number += 1
             outputFileName = "DDoSGraph_" + hour + minutes + ".g"
             if(os.path.exists(outputFileName)):
                 outputFile = open(outputFileName, "a")
                 outputFile.write("XP\n")
             else:
                 outputFile = open(outputFileName, "w")
                 outputFile.write("XP\n")
         else:
             prev_hour = hour
             prev_minute= minutes
             #file_increment_number += 1
             outputFileName = "DDoSGraph_" + hour + minutes + ".g"
             outputFile = open(outputFileName, "a")
             outputFile.write("XP\n")


         information_vertex = vertex_number

         value = row['Flow_ID']  ##
         if value != "":
             outputFile.write('v ')
             outputFile.write(str(vertex_number))
             outputFile.write(' ')
             outputFile.write('\"')
             outputFile.write(value)
             outputFile.write('\"')
             outputFile.write('\n')
             vertex_number += 1
             target_vertex = vertex_number
             #

         # value = row['Timestamp']  ##
         # if value != "":
         #     outputFile.write('v ')
         #     outputFile.write(str(vertex_number))
         #     outputFile.write(' ')
         #     outputFile.write('\"')
         #     outputFile.write(value)
         #     outputFile.write('\"')
         #     outputFile.write('\n')
         #     target_vertex = vertex_number
         #     vertex_number += 1
         #     #
         #     outputFile.write(undirected_edge)
         #     outputFile.write(' ')
         #     outputFile.write(str(information_vertex))  ##
         #     outputFile.write(' ')
         #     outputFile.write(str(target_vertex))
         #     outputFile.write(' ')
         #     outputFile.write('\"Timestamp\"\n')

         value = row['Src_IP']  ##
         if value != "":
             outputFile.write('v ')
             outputFile.write(str(vertex_number))
             outputFile.write(' ')
             outputFile.write('\"')
             outputFile.write(value)
             outputFile.write('\"')
             outputFile.write('\n')
             target_vertex = vertex_number
             vertex_number += 1
             #
             outputFile.write(directed_edge)
             outputFile.write(' ')
             outputFile.write(str(target_vertex))  ##
             outputFile.write(' ')
             outputFile.write(str(information_vertex))
             outputFile.write(' ')
             outputFile.write('\"Sent From"\n')

         value = row['Src_Port']  ##
         if value != "":
             outputFile.write('v ')
             outputFile.write(str(vertex_number))
             outputFile.write(' ')
             outputFile.write('\"')
             outputFile.write(value)
             outputFile.write('\"')
             outputFile.write('\n')
             target_vertex = vertex_number
             vertex_number += 1
             #
             outputFile.write(undirected_edge)
             outputFile.write(' ')
             outputFile.write(str(vertex_number - 2))
             outputFile.write(' ')
             outputFile.write(str(target_vertex))
             outputFile.write(' ')
             outputFile.write('\"Using this Port"\n')

         value = row['Dst_IP']  ##
         if value != "":
             outputFile.write('v ')
             outputFile.write(str(vertex_number))
             outputFile.write(' ')
             outputFile.write('\"')
             outputFile.write(value)
             outputFile.write('\"')
             outputFile.write('\n')
             target_vertex = vertex_number
             vertex_number += 1
             #
             outputFile.write(directed_edge)
             outputFile.write(' ')
             outputFile.write(str(information_vertex))  ##
             outputFile.write(' ')
             outputFile.write(str(target_vertex))
             outputFile.write(' ')
             outputFile.write('\"Sent To\"\n')

         value = row['Dst_Port']  ##
         if value != "":
             outputFile.write('v ')
             outputFile.write(str(vertex_number))
             outputFile.write(' ')
             outputFile.write('\"')
             outputFile.write(value)
             outputFile.write('\"')
             outputFile.write('\n')
             target_vertex = vertex_number
             vertex_number += 1
             #
             outputFile.write(undirected_edge)
             outputFile.write(' ')
             outputFile.write(str(vertex_number - 2))
             outputFile.write(' ')
             outputFile.write(str(target_vertex))
             outputFile.write(' ')
             outputFile.write('\"Using This Port\"\n')

         value = row['Protocol']  ##
         if value != "":
             outputFile.write('v ')
             outputFile.write(str(vertex_number))
             outputFile.write(' ')
             outputFile.write('\"')
             outputFile.write(value)
             outputFile.write('\"')
             outputFile.write('\n')
             target_vertex = vertex_number
             vertex_number += 1
             #
             outputFile.write(undirected_edge)
             outputFile.write(' ')
             outputFile.write(str(information_vertex))  ##
             outputFile.write(' ')
             outputFile.write(str(target_vertex))
             outputFile.write(' ')
             outputFile.write('\"Protocol Used\"\n')

         value = row['Flow_Duration']  ##
         if value != "":
             outputFile.write('v ')
             outputFile.write(str(vertex_number))
             outputFile.write(' ')
             outputFile.write('\"')
             outputFile.write(value)
             outputFile.write('\"')
             outputFile.write('\n')
             target_vertex = vertex_number
             vertex_number += 1
             #
             outputFile.write(undirected_edge)
             outputFile.write(' ')
             outputFile.write(str(information_vertex))  ##
             outputFile.write(' ')
             outputFile.write(str(target_vertex))
             outputFile.write(' ')
             outputFile.write('\"Duration of Flow\"\n')

         value = row['Tot_Fwd_Pkts']  ##
         if value != "":
             outputFile.write('v ')
             outputFile.write(str(vertex_number))
             outputFile.write(' ')
             outputFile.write('\"')
             outputFile.write(value)
             outputFile.write('\"')
             outputFile.write('\n')
             target_vertex = vertex_number
             vertex_number += 1
             #

             outputFile.write(undirected_edge)
             outputFile.write(' ')
             outputFile.write(str(information_vertex))  ##
             outputFile.write(' ')
             outputFile.write(str(target_vertex))
             outputFile.write(' ')
             outputFile.write('\"Total Forward Packets\"\n')

         value = row['Tot_Bwd_Pkts']  ##
         if value != "":
             outputFile.write('v ')
             outputFile.write(str(vertex_number))
             outputFile.write(' ')
             outputFile.write('\"')
             outputFile.write(value)
             outputFile.write('\"')
             outputFile.write('\n')
             target_vertex = vertex_number
             vertex_number += 1
             #
             outputFile.write(undirected_edge)
             outputFile.write(' ')
             outputFile.write(str(information_vertex))  ##
             outputFile.write(' ')
             outputFile.write(str(target_vertex))
             outputFile.write(' ')
             outputFile.write('\"Total Backward Packets\"\n')

             value = row['Tot_Fwd_Pkts']  ##
             if value != "":
                 outputFile.write('v ')
                 outputFile.write(str(vertex_number))
                 outputFile.write(' ')
                 outputFile.write('\"')
                 outputFile.write(value)
                 outputFile.write('\"')
                 outputFile.write('\n')
                 target_vertex = vertex_number
                 vertex_number += 1
                 #
                 outputFile.write(undirected_edge)
                 outputFile.write(' ')
                 outputFile.write(str(information_vertex))  ##
                 outputFile.write(' ')
                 outputFile.write(str(target_vertex))
                 outputFile.write(' ')
                 outputFile.write('\"Total Forward Packets\"\n')


             value = row['TotLen_Fwd_Pkts']  ##
             if value != "":
                 outputFile.write('v ')
                 outputFile.write(str(vertex_number))
                 outputFile.write(' ')
                 outputFile.write('\"')
                 outputFile.write(value)
                 outputFile.write('\"')
                 outputFile.write('\n')
                 target_vertex = vertex_number
                 vertex_number += 1
                 #
                 outputFile.write(undirected_edge)
                 outputFile.write(' ')
                 outputFile.write(str(information_vertex))  ##
                 outputFile.write(' ')
                 outputFile.write(str(target_vertex))
                 outputFile.write(' ')
                 outputFile.write('\"Total Length of Packet\"\n')

             value = row['TotLen_Bwd_Pkts']  ##
             if value != "":
                 outputFile.write('v ')
                 outputFile.write(str(vertex_number))
                 outputFile.write(' ')
                 outputFile.write('\"')
                 outputFile.write(value)
                 outputFile.write('\"')
                 outputFile.write('\n')
                 target_vertex = vertex_number
                 vertex_number += 1
                 #
                 outputFile.write(undirected_edge)
                 outputFile.write(' ')
                 outputFile.write(str(information_vertex))  ##
                 outputFile.write(' ')
                 outputFile.write(str(target_vertex))
                 outputFile.write(' ')
                 outputFile.write('\"Total Length of Packet\"\n')

             # value = row['Fwd_Pkt_Len_Max']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Max Length of Packet\"\n')
             #
             # value = row['Fwd_Pkt_Len_Min']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Min Length of Packet\"\n')
             #
             # value = row['Fwd_Pkt_Len_Mean']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Mean Length of Packet\"\n')
             #
             # value = row['Fwd_Pkt_Len_Std']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Std Length of Packet"\n')
             #
             # value = row['Bwd_Pkt_Len_Max']  ##
             # if value != "":
             #      outputFile.write('v ')
             #      outputFile.write(str(vertex_number))
             #      outputFile.write(' ')
             #      outputFile.write('\"')
             #      outputFile.write(value)
             #      outputFile.write('\"')
             #      outputFile.write('\n')
             #      target_vertex = vertex_number
             #      vertex_number += 1
             #      #
             #      outputFile.write(undirected_edge)
             #      outputFile.write(' ')
             #      outputFile.write(str(information_vertex))  ##
             #      outputFile.write(' ')
             #      outputFile.write(str(target_vertex))
             #      outputFile.write(' ')
             #      outputFile.write('\"Max Length of Packet\"\n')
             #
             # value = row['Bwd_Pkt_Len_Min']  ##
             # if value != "":
             #      outputFile.write('v ')
             #      outputFile.write(str(vertex_number))
             #      outputFile.write(' ')
             #      outputFile.write('\"')
             #      outputFile.write(value)
             #      outputFile.write('\"')
             #      outputFile.write('\n')
             #      target_vertex = vertex_number
             #      vertex_number += 1
             #      #
             #      outputFile.write(undirected_edge)
             #      outputFile.write(' ')
             #      outputFile.write(str(information_vertex))  ##
             #      outputFile.write(' ')
             #      outputFile.write(str(target_vertex))
             #      outputFile.write(' ')
             #      outputFile.write('\"Min Length of Packet\"\n')
             #
             # value = row['Bwd_Pkt_Len_Mean']  ##
             # if value != "":
             #      outputFile.write('v ')
             #      outputFile.write(str(vertex_number))
             #      outputFile.write(' ')
             #      outputFile.write('\"')
             #      outputFile.write(value)
             #      outputFile.write('\"')
             #      outputFile.write('\n')
             #      target_vertex = vertex_number
             #      vertex_number += 1
             #      #
             #      outputFile.write(undirected_edge)
             #      outputFile.write(' ')
             #      outputFile.write(str(information_vertex))  ##
             #      outputFile.write(' ')
             #      outputFile.write(str(target_vertex))
             #      outputFile.write(' ')
             #      outputFile.write('\"Mean Length of Packet\"\n')
             #
             # value = row['Bwd_Pkt_Len_Std']  ##
             # if value != "":
             #      outputFile.write('v ')
             #      outputFile.write(str(vertex_number))
             #      outputFile.write(' ')
             #      outputFile.write('\"')
             #      outputFile.write(value)
             #      outputFile.write('\"')
             #      outputFile.write('\n')
             #      target_vertex = vertex_number
             #      vertex_number += 1
             #      #
             #      outputFile.write(undirected_edge)
             #      outputFile.write(' ')
             #      outputFile.write(str(information_vertex))  ##
             #      outputFile.write(' ')
             #      outputFile.write(str(target_vertex))
             #      outputFile.write(' ')
             #      outputFile.write('\"Std Length of Packet"\n')
             #
             # value = row['Flow_Byts/s']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Bytes per Second of Flow\"\n')
             #
             # value = row['Flow_Pkts/s']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Packets per Second from Flow\"\n')
             #
             # value = row['Flow_IAT_Mean']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Mean IAT of Flow\"\n')
             #
             # value = row['Flow_IAT_Std']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Std Length of Flow"\n')
             #
             # value = row['Flow_IAT_Max']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Max Length of Flow\"\n')
             #
             # value = row['Flow_IAT_Min']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Min Length of Packet\"\n')
             #
             # value = row['Fwd_IAT_Tot']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"IAT Total\"\n')
             #
             # value = row['Fwd_IAT_Mean']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Mean IAT"\n')
             #
             # value = row['Bwd_IAT_Mean']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Std Length of Flow"\n')
             #
             # value = row['Fwd_IAT_Max']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Max Length of Fwd\"\n')
             #
             # value = row['Fwd_IAT_Min']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Min Length of Fwd\"\n')
             #
             # value = row['Bwd_IAT_Tot']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"IAT Total\"\n')
             #
             # value = row['Fwd_IAT_Std']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Std IAT"\n')
             #
             # value = row['Bwd_IAT_Std']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Std of Bwd IAT\"\n')
             #
             # value = row['Bwd_IAT_Max']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Bwd IAT Max\"\n')
             #
             # value = row['Bwd_IAT_Min']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Bwd IAT Min\"\n')
             #
             # value = row['Fwd_PSH_Flags']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Forward Push Flags"\n')
             #
             # value = row['Bwd_PSH_Flags']  ##
             # if value != "":
             #         outputFile.write('v ')
             #         outputFile.write(str(vertex_number))
             #         outputFile.write(' ')
             #         outputFile.write('\"')
             #         outputFile.write(value)
             #         outputFile.write('\"')
             #         outputFile.write('\n')
             #         target_vertex = vertex_number
             #         vertex_number += 1
             #         #
             #         outputFile.write(undirected_edge)
             #         outputFile.write(' ')
             #         outputFile.write(str(information_vertex))  ##
             #         outputFile.write(' ')
             #         outputFile.write(str(target_vertex))
             #         outputFile.write(' ')
             #         outputFile.write('\"Backward Push Flags"\n')
             #
             # value = row['Fwd_URG_Flags']  ##
             # if value != "":
             #         outputFile.write('v ')
             #         outputFile.write(str(vertex_number))
             #         outputFile.write(' ')
             #         outputFile.write('\"')
             #         outputFile.write(value)
             #         outputFile.write('\"')
             #         outputFile.write('\n')
             #         target_vertex = vertex_number
             #         vertex_number += 1
             #         #
             #         outputFile.write(undirected_edge)
             #         outputFile.write(' ')
             #         outputFile.write(str(information_vertex))  ##
             #         outputFile.write(' ')
             #         outputFile.write(str(target_vertex))
             #         outputFile.write(' ')
             #         outputFile.write('\"Forward URG Flags\"\n')
             #
             # value = row['Bwd_URG_Flags']  ##
             # if value != "":
             #         outputFile.write('v ')
             #         outputFile.write(str(vertex_number))
             #         outputFile.write(' ')
             #         outputFile.write('\"')
             #         outputFile.write(value)
             #         outputFile.write('\"')
             #         outputFile.write('\n')
             #         target_vertex = vertex_number
             #         vertex_number += 1
             #         #
             #         outputFile.write(undirected_edge)
             #         outputFile.write(' ')
             #         outputFile.write(str(information_vertex))  ##
             #         outputFile.write(' ')
             #         outputFile.write(str(target_vertex))
             #         outputFile.write(' ')
             #         outputFile.write('\"Backward URG Flags\"\n')
             #
             # value = row['Fwd_Header_Len']  ##
             # if value != "":
             #         outputFile.write('v ')
             #         outputFile.write(str(vertex_number))
             #         outputFile.write(' ')
             #         outputFile.write('\"')
             #         outputFile.write(value)
             #         outputFile.write('\"')
             #         outputFile.write('\n')
             #         target_vertex = vertex_number
             #         vertex_number += 1
             #         #
             #         outputFile.write(undirected_edge)
             #         outputFile.write(' ')
             #         outputFile.write(str(information_vertex))  ##
             #         outputFile.write(' ')
             #         outputFile.write(str(target_vertex))
             #         outputFile.write(' ')
             #         outputFile.write('\"Forward Header Length\"\n')
             #
             # value = row['Bwd_Header_Len']  ##
             # if value != "":
             #         outputFile.write('v ')
             #         outputFile.write(str(vertex_number))
             #         outputFile.write(' ')
             #         outputFile.write('\"')
             #         outputFile.write(value)
             #         outputFile.write('\"')
             #         outputFile.write('\n')
             #         target_vertex = vertex_number
             #         vertex_number += 1
             #         #
             #         outputFile.write(undirected_edge)
             #         outputFile.write(' ')
             #         outputFile.write(str(information_vertex))  ##
             #         outputFile.write(' ')
             #         outputFile.write(str(target_vertex))
             #         outputFile.write(' ')
             #         outputFile.write('\"Backward Header Length"\n')
             #
             # value = row['Fwd_Pkts/s']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Forward Packets per Second"\n')
             #
             # value = row['Bwd_Pkts/s']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Backward Packets per Second"\n')
             #
             # value = row['Pkt_Len_Min']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Packet Length Min"\n')
             #
             # value = row['Pkt_Len_Max']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Packet Length Max"\n')
             #
             # value = row['Pkt_Len_Mean']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Packet Length Mean"\n')
             #
             # value = row['Pkt_Len_Std']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Packet Length Std"\n')
             #
             # value = row['Pkt_Len_Var']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Packet Length Var"\n')
             #
             # value = row['FIN_Flag_Cnt']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Fin Flag Count"\n')
             #
             # value = row['SYN_Flag_Cnt']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"SYN Flag Count"\n')
             #
             # value = row['RST_Flag_Cnt']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"RST Flag Count"\n')
             #
             # value = row['PSH_Flag_Cnt']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"PSH Flag Count"\n')
             #
             # value = row['ACK_Flag_Cnt']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"ACK Flag Count"\n')
             #
             # value = row['URG_Flag_Cnt']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"URG Flag Count"\n')
             #
             # value = row['CWE_Flag_Count']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"CWE Flag Count"\n')
             #
             # value = row['ECE_Flag_Cnt']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"ECE Flag Count"\n')
             #
             # value = row['Down/Up_Ratio']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Down/Up Ratio"\n')
             #
             # value = row['Pkt_Size_Avg']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Average Size of Packet"\n')
             #
             # value = row['Fwd_Seg_Size_Avg']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Forward Seg Size Average"\n')
             #
             # value = row['Bwd_Seg_Size_Avg']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Backward Seg Size Average"\n')
             #
             # value = row['Fwd_Byts/b_Avg']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Forward Bytes Divided by some Average"\n')
             #
             # value = row['Fwd_Pkts/b_Avg']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Forward Packets Divided by some Average"\n')
             #
             # value = row['Fwd_Blk_Rate_Avg']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Forward Blk Rate Average"\n')
             #
             # value = row['Bwd_Byts/b_Avg']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Backward Bytes Divided by some Average"\n')
             #
             # value = row['Bwd_Pkts/b_Avg']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Backward Packets Divided by some Average"\n')
             #
             # value = row['Bwd_Blk_Rate_Avg']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Backward Blk Rate Average"\n')
             #
             # value = row['Subflow_Fwd_Pkts']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Subflow Forward Packets"\n')
             #
             # value = row['Subflow_Fwd_Byts']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Subflow Forward Bytes"\n')
             #
             # value = row['Subflow_Bwd_Pkts']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Subflow Backward Packets"\n')
             #
             # value = row['Subflow_Bwd_Byts']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Subflow Backward Bytes"\n')
             #
             # value = row['Init_Fwd_Win_Byts']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Initial Forward Win Bytes"\n')
             #
             # value = row['Init_Bwd_Win_Byts']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Initial Backward Win Bytes"\n')
             #
             # value = row['Fwd_Act_Data_Pkts']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Forward Act Data Packets"\n')
             #
             # value = row['Fwd_Seg_Size_Min']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Forward Seg Size Min"\n')
             #
             # value = row['Active_Mean']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"The Active Mean"\n')
             #
             # value = row['Active_Std']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"The Active Std"\n')
             #
             # value = row['Active_Max']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"The Active Max"\n')
             #
             # value = row['Active_Min']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"The Active Min"\n')
             #
             # value = row['Idle_Mean']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Idle Mean"\n')
             #
             # value = row['Idle_Std']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Idle Std"\n')
             #
             # value = row['Idle_Max']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Idle Max"\n')
             #
             # value = row['Idle_Min']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Idle Min"\n')

             # value = row['Cat']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Cat"\n')
             #
             # value = row['Sub_Cat']  ##
             # if value != "":
             #     outputFile.write('v ')
             #     outputFile.write(str(vertex_number))
             #     outputFile.write(' ')
             #     outputFile.write('\"')
             #     outputFile.write(value)
             #     outputFile.write('\"')
             #     outputFile.write('\n')
             #     target_vertex = vertex_number
             #     vertex_number += 1
             #     #
             #     outputFile.write(undirected_edge)
             #     outputFile.write(' ')
             #     outputFile.write(str(information_vertex))  ##
             #     outputFile.write(' ')
             #     outputFile.write(str(target_vertex))
             #     outputFile.write(' ')
             #     outputFile.write('\"Sub Cat"\n')
             #
             value = row['Label']  ##
             if value != "":
                    if value == "Anomaly":
                        MIDAS.write("1")
                    else:
                        MIDAS.write("0")
                    MIDAS.write('\n')

                    outputFile.write('v ')
                    outputFile.write(str(vertex_number))
                    outputFile.write(' ')
                    outputFile.write('\"')
                    outputFile.write(value)
                    outputFile.write('\"')
                    outputFile.write('\n')
                    target_vertex = vertex_number
                    vertex_number += 1
                    #
                    outputFile.write(undirected_edge)
                    outputFile.write(' ')
                    outputFile.write(str(information_vertex))  ##
                    outputFile.write(' ')
                    outputFile.write(str(target_vertex))
                    outputFile.write(' ')
                    outputFile.write('\"anomaly or normal?\"\n')


MIDAS.close()
print("... read in " + str(num_records) + " records")
MIDAS_entries = open("../../Research/data/MIDAS_test/DDoS_entries.txt", 'w')
MIDAS_entries.write(str(num_records))
MIDAS_entries.close()

# prev_year = year
# prev_month = month
# prev_day = day
# file_increment_number += 1
# outputFileName = sys.argv[2] + "_" + year + month + day + ".g"
# increment_number = 1
# vertex_number = 1
# #
# outputFile.write('XP # 1')
# outputFile.write('\n')
#
# # Create a different increment file for each set of rows with the same date
# #
# file_increment_number = 0
# increment_number = 1
# row_count = 1
# prev_year = "0"
# prev_month = "0"
# prev_day = "0"
# undirected_edge = "u"
# directed_edge = "d"
# #
# eventid_list = []
# related_events_list = []
#
# information_vertex = vertex_number
#
#
# value = row['dataid']  ##
# if value != "":
#     outputFile.write('v ')
#     outputFile.write(str(vertex_number))
#     outputFile.write(' ')
#     outputFile.write('\"')
#     outputFile.write(value)
#     outputFile.write('\"')
#     outputFile.write('\n')
#     vertex_number += 1
#     target_vertex = vertex_number
#     #
#
# value = row['pkSeqID']  ##
# if value != "":
#     outputFile.write('v ')
#     outputFile.write(str(vertex_number))
#     outputFile.write(' ')
#     outputFile.write('\"')
#     outputFile.write(value)
#     outputFile.write('\"')
#     outputFile.write('\n')
#     target_vertex = vertex_number
#     vertex_number += 1
#     #
#     outputFile.write(undirected_edge)
#     outputFile.write(' ')
#     outputFile.write(str(information_vertex))  ##
#     outputFile.write(' ')
#     outputFile.write(str(target_vertex))
#     outputFile.write(' ')
#     outputFile.write('\"Packet Sequence ID\"\n')
#
# value = row['stime']  ##
# if value != "":
#     outputFile.write('v ')
#     outputFile.write(str(vertex_number))
#     outputFile.write(' ')
#     outputFile.write('\"')
#     outputFile.write(value)
#     outputFile.write('\"')
#     outputFile.write('\n')
#     target_vertex = vertex_number
#     vertex_number += 1
#     #
#     outputFile.write(undirected_edge)
#     outputFile.write(' ')
#     outputFile.write(str(information_vertex))  ##
#     outputFile.write(' ')
#     outputFile.write(str(target_vertex))
#     outputFile.write(' ')
#     outputFile.write('\"Start Time"\n')
#
# value = row['flgs']  ##
# if value != "":
#     outputFile.write('v ')
#     outputFile.write(str(vertex_number))
#     outputFile.write(' ')
#     outputFile.write('\"')
#     outputFile.write(value)
#     outputFile.write('\"')
#     outputFile.write('\n')
#     target_vertex = vertex_number
#     vertex_number += 1
#     #
#     outputFile.write(undirected_edge)
#     outputFile.write(' ')
#     outputFile.write(str(information_vertex))  ##
#     outputFile.write(' ')
#     outputFile.write(str(target_vertex))
#     outputFile.write(' ')
#     outputFile.write('\"Flags\"\n')
#
# value = row['flgs_number']  ##
# if value != "":
#     outputFile.write('v ')
#     outputFile.write(str(vertex_number))
#     outputFile.write(' ')
#     outputFile.write('\"')
#     outputFile.write(value)
#     outputFile.write('\"')
#     outputFile.write('\n')
#     target_vertex = vertex_number
#     vertex_number += 1
#     #
#     outputFile.write(undirected_edge)
#     outputFile.write(' ')
#     outputFile.write(str(information_vertex))  ##
#     outputFile.write(' ')
#     outputFile.write(str(target_vertex))
#     outputFile.write(' ')
#     outputFile.write('\"Number of Flags\"\n')
#
# value = row['proto']  ##
# if value != "":
#     outputFile.write('v ')
#     outputFile.write(str(vertex_number))
#     outputFile.write(' ')
#     outputFile.write('\"')
#     outputFile.write(value)
#     outputFile.write('\"')
#     outputFile.write('\n')
#     target_vertex = vertex_number
#     vertex_number += 1
#     #
#     outputFile.write(undirected_edge)
#     outputFile.write(' ')
#     outputFile.write(str(information_vertex))  ##
#     outputFile.write(' ')
#     outputFile.write(str(target_vertex))
#     outputFile.write(' ')
#     outputFile.write('\"Protocol\"\n')
#
# value = row['proto_number']  ##
# if value != "":
#     outputFile.write('v ')
#     outputFile.write(str(vertex_number))
#     outputFile.write(' ')
#     outputFile.write('\"')
#     outputFile.write(value)
#     outputFile.write('\"')
#     outputFile.write('\n')
#     target_vertex = vertex_number
#     vertex_number += 1
#     #
#     outputFile.write(undirected_edge)
#     outputFile.write(' ')
#     outputFile.write(str(information_vertex))  ##
#     outputFile.write(' ')
#     outputFile.write(str(target_vertex))
#     outputFile.write(' ')
#     outputFile.write('\"Number of Protocols\"\n')
#
# value = row['saddr']  ##
# if value != "":
#     outputFile.write('v ')
#     outputFile.write(str(vertex_number))
#     outputFile.write(' ')
#     outputFile.write('\"')
#     outputFile.write(value)
#     outputFile.write('\"')
#     outputFile.write('\n')
#     target_vertex = vertex_number
#     vertex_number += 1
#     #
#     outputFile.write(undirected_edge)
#     outputFile.write(' ')
#     outputFile.write(str(information_vertex))  ##
#     outputFile.write(' ')
#     outputFile.write(str(target_vertex))
#     outputFile.write(' ')
#     outputFile.write('\"Source IP Address\"\n')
#
# value = row['sport']  ##
# if value != "":
#     outputFile.write('v ')
#     outputFile.write(str(vertex_number))
#     outputFile.write(' ')
#     outputFile.write('\"')
#     outputFile.write(value)
#     outputFile.write('\"')
#     outputFile.write('\n')
#     target_vertex = vertex_number
#     vertex_number += 1
#     #
#     outputFile.write(undirected_edge)
#     outputFile.write(' ')
#     outputFile.write(str(information_vertex))  ##
#     outputFile.write(' ')
#     outputFile.write(str(target_vertex))
#     outputFile.write(' ')
#     outputFile.write('\"Source Port\"\n')
#
# value = row['daddr']  ##
# if value != "":
#     outputFile.write('v ')
#     outputFile.write(str(vertex_number))
#     outputFile.write(' ')
#     outputFile.write('\"')
#     outputFile.write(value)
#     outputFile.write('\"')
#     outputFile.write('\n')
#     target_vertex = vertex_number
#     vertex_number += 1
#     #
#     outputFile.write(undirected_edge)
#     outputFile.write(' ')
#     outputFile.write(str(information_vertex))  ##
#     outputFile.write(' ')
#     outputFile.write(str(target_vertex))
#     outputFile.write(' ')
#     outputFile.write('\"Destination IP Address\"\n')





