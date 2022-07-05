
# This script converts the GTD CSV file to graph increments by day
#
# NOTE: The format of the resulting graph input files is for SUBDUE (not GBAD)
#
import csv
import time
import glob
import os.path


filename = "/home/jaketay/Research/data/MIDAS_test/MIDAS_Test.csv"
for f in glob.glob("*.g"):
    os.remove(f)

# Create a different increment file for each set of rows with the same date
 #
file_increment_number = 0
increment_number = 1
row_count = 1         # Create a different increment file for each set of rows with the same date
prev_ip = "0"
information_vertex = 1
undirected_edge = "u"
directed_edge = "d"
vertex_number = 1
xp_counter = 2
starting_time = 0
current_time = 0

dest_ips = []
sO_values = []
src_ips = []
val_temp = []


ip_dict = {"Sichuani_4b:ae:ba": "192.168.0.13", "EFMNetwo_d7:1c:56": "192.168.0.1", "Apple_c9:bf:fc": "192.168.0.125", "fe80::44c:2fec:17e8:c1f5": "10.0.0.1", "SamsungE_d6:5d:9c": "192.168.0.23" , "bc:e8:2f:2a:20:ee":"15.5.5.5"
           , "bc:1c:92:4b:ae:ba":"192.168.0.13", "bc:1c:01:b2:33:ba":"192.168.0.2"}

#Create G File
outputFile = open("DDoSGraph.g", "w")


#Cut out Traffic Values to make Relationship Checking Easier
def cut_out_vals(array):
    temp_array = []
    for i in array:
        temp_array.append([i[0], i[1]])
    #print(temp_array)
    return temp_array


#Corrects Error where there are Duplicate IPS sending traffic to Destination IP
def collapse_src_IPS(array):
    temp_arr = cut_out_vals(array)
    temp_list = []
    temp_final = []

    #Pseudo Set for Source IP names
    for i in temp_arr:
        if i not in temp_list:
            temp_list.append(i)


    #Count traffic sent between each Relationship
    value = 0
    for i in temp_list:
        counterx = 0
        for q in array:
            if i[0] == q[0] and i[1] == q[1]:
                counterx += 1
        if (str(i[0][0]).isdigit()):
            value = i[0]
        else:
            value = ip_dict[i[0]]
        temp_final.append([value,i[1], counterx])


    #Reset Array to Fixed Array
    array = temp_final
    #print(temp_final)
    return array

#Corrects Error where there are Duplicate IPS sending traffic to Destination IP
def collapse_IPS(array):
    temp_arr = array
    temp_list = []
    temp_final = []

    #Pseudo Set for Source IP names
    for i in temp_arr:
        if i not in temp_list:
            temp_list.append(i)


    #Count traffic sent between each Relationship
    value = 0
    for i in temp_list:
        counterx = 0
        for q in array:
            if i[0] == q[0] and i[1] == q[1]:
                #print(counterx)
                counterx += 1
        temp_final.append([i[0],i[1], counterx])


    #Reset Array to Fixed Array
    array = temp_final
    #print(temp_final)
    return array

#Set Up Relationships to Clean up how Graph File looks
#**Improves Readibility this way*
def set_Up_Src_Relationship(file, array, array2):
    global vertex_number


    # #Call to Traffic Label to get Traffic Label
    # for i in array:
    #     label = traffic_label(i[2])
    #     i[2] = label

    src_ip_array = []


    for i in array2:
        src_ip_array.append(i[1])

    print(src_ip_array)
    src_first_ip = []

    for i in array2:
        src_first_ip.append((i[0]))
    print(src_first_ip)

    # for i in src_first_ip:
    #     for q in src_ip_array:
    #         if i






#Set Up Relationships to Clean up how Graph File looks
#**Improves Readibility this way*
def set_Up_Relationship(file, array, dest_ips):
    global vertex_number


    # #Call to Traffic Label to get Traffic Label
    # for i in array:
    #     label = traffic_label(i[2])
    #     i[2] = label

    src_ip_array = []
   # print(array)
    counter = 0

    #For Loop to Traverse through values in Array
    for i in array:
        #print(i)

        #Create Vertice and Connection of Sender Nodes
        outputFile.write('v ')
        outputFile.write(str(vertex_number))
        outputFile.write(' ')
        outputFile.write('\"')
        outputFile.write(str(array[counter][1]))
        outputFile.write('\"')
        outputFile.write('\n')
        target_vertex = vertex_number
        vertex_number += 1

        #Relationship from Sender to Destination IP
        outputFile.write(directed_edge)
        outputFile.write(' ')
        outputFile.write(str(target_vertex))  ##
        outputFile.write(' ')
        vals = dest_ips[array[counter][0]]
        #destination = dest_check(vals, dest_ips)
        outputFile.write(str(array[counter][0] + 1))
        outputFile.write(' ')
        outputFile.write("\"" + str(array[counter][2]) + "\"\n")

        counter += 1

#Start Next Example (XP)
#Default Value: 15 Seconds
def XP_New(Stime, CTime):
    global xp_counter, starting_time, current_time, vertex_number, dest_ips
    if ((int(CTime) - int(Stime)) >= 10):
        Stime = current_time
        outputFile.write("XP # " + str(xp_counter) + "  // Stime Tag: " + str(current_time) + "  \n")
        xp_counter += 1
        vertex_number = 1
        starting_time = Stime
        dest_ips = []

#A check to make sure given Destination IP is contained within the Array of values
def dest_check(dest, ips):
    val_check = 0
    for i in range(0, len(ips)):
            if (ips[i] == dest):
                val_check = i + 1
    return val_check




#Limit Values for Quicker Testing
N = 10000

#Start Timer
tic = time.perf_counter()
outputFile.write("XP # 1 //Time Tag: 0\n")

#Run Through CSV file and Extract Data
gtd_list = []
with open(filename, newline='', encoding='latin1') as rows:
      row_reader = csv.DictReader(rows, delimiter=',')
      num_records = 0
      counter = 0
      for row in row_reader:
         gtd_list.append(dict(row))
         num_records += 1


         if N == 0:
             break

         if N % 500 == 0:
             print(N)

         N -= 1

         # Call New XP Check
         XP_New(starting_time, current_time)

         # Create Vertice For Destination IPs
         value = row['dstip']
         if (value.startswith("Sichuani")):
             value = ip_dict['Sichuani_4b:ae:ba']
         elif (value.startswith("EFM")):
             value = ip_dict['EFMNetwo_d7:1c:56']
         elif (value.startswith("Apple")):
             value = ip_dict['Apple_c9:bf:fc']
         elif (value.startswith("fe80") or value.startswith("ff")):
             value = ip_dict['fe80::44c:2fec:17e8:c1f5']
         elif (value.startswith("Sam")):
             value = ip_dict['SamsungE_d6:5d:9c']
         elif (value.startswith("bc")):
             value = "192.168.0.2"
         elif (value.startswith("Broad")):
             value = "10.0.0.1"
         elif (value.startswith("a8")):
             value = "192.168.0.95"
         elif (value.startswith("fb")):
             value = "192.168.0.95"
         elif (value.startswith("05")):
             value = "192.168.0.97"
         elif (value.startswith("88")):
             value = "192.168.0.99"
         elif (value.startswith("Partron")):
             value = "192.168.0.100"


         vals = value.split(".", 1)
         #print(vals)
         if value != "":
             if (vals[0] in dest_ips):
                 for i in range(0, len(dest_ips)):
                     if (dest_ips[i] == vals[0]):
                         val_check = i
                         i = i + 1
                         sO_values.append([val_check,vals[1]])
                         # finale = collapse_IPS(sO_values)


                         # outputFile.write('v ')
                         # outputFile.write(str(vertex_number))
                         # outputFile.write(' ')
                         # outputFile.write('\"')
                         # outputFile.write(str(vals[1]))
                         # outputFile.write('\"')
                         # outputFile.write("\t// " + str(vals[1]))
                         # outputFile.write('\n')
                         # target_vertex = vertex_number
                         # information_vertex = vertex_number
                         # vertex_number += 1
                         #
                         # # Relationship from Sender to Destination IP
                         # outputFile.write(directed_edge)
                         # outputFile.write(' ')
                         # outputFile.write(str(information_vertex))
                         # outputFile.write(' ')
                         # outputFile.write(str(i))  ##
                         # outputFile.write(' ')
                         # outputFile.write("\"Rest of IP""\"\n")
             else:
                 dest_ips.append(vals[0])
                 outputFile.write('v ')
                 outputFile.write(str(vertex_number))
                 outputFile.write(' ')
                 outputFile.write('\"')
                 outputFile.write(str(vals[0]))
                 outputFile.write('\"')
                 outputFile.write("\t// " + str(vals[0]))
                 outputFile.write('\n')
                 target_vertex = vertex_number
                 information_vertex = vertex_number
                 vertex_number += 1

                 outputFile.write('v ')
                 outputFile.write(str(vertex_number))
                 outputFile.write(' ')
                 outputFile.write('\"')
                 outputFile.write(str(vals[1]))
                 outputFile.write('\"')
                 outputFile.write("\t// " + str(vals[1]))
                 outputFile.write('\n')
                 target_vertex = vertex_number
                 vertex_number += 1

                 # Relationship from Sender to Destination IP
                 outputFile.write(directed_edge)
                 outputFile.write(' ')
                 outputFile.write(str(target_vertex))  ##
                 outputFile.write(' ')
                 outputFile.write(str(information_vertex))
                 outputFile.write(' ')
                 outputFile.write("\"1""\"\n")

         value = row['srcip']  ##
         if (value.startswith("Sichuani")):
             value = ip_dict['Sichuani_4b:ae:ba']
         elif (value.startswith("EFM")):
             value = ip_dict['EFMNetwo_d7:1c:56']
             #print(value)
         elif (value.startswith("Apple")):
             value = ip_dict['Apple_c9:bf:fc']
         elif (value.startswith("fe80") or value.startswith("ff")):
             value = ip_dict['fe80::44c:2fec:17e8:c1f5']
         elif (value.startswith("Sam")):
             value = ip_dict['SamsungE_d6:5d:9c']
         elif (value.startswith("bc")):
             value = "192.168.0.2"
         elif (value.startswith("Partron")):
             value = "192.168.0.100"

         dst_val = row['dstip']
         if (dst_val.startswith("Sichuani")):
             dst_val = ip_dict['Sichuani_4b:ae:ba']
         elif (dst_val.startswith("EFM")):
             dst_val = ip_dict['EFMNetwo_d7:1c:56']
         elif (dst_val.startswith("Apple")):
             dst_val = ip_dict['Apple_c9:bf:fc']
         elif (dst_val.startswith("fe80") or value.startswith("ff")):
             dst_val = ip_dict['fe80::44c:2fec:17e8:c1f5']
         elif (dst_val.startswith("Sam")):
             dst_val = ip_dict['SamsungE_d6:5d:9c']
         elif (dst_val.startswith("bc")):
             dst_val = "192.168.0.2"
         elif (dst_val.startswith("Broad")):
             dst_val = "10.0.0.1"
         elif (dst_val.startswith("a8")):
             dst_val = "192.168.0.95"
         elif (dst_val.startswith("fb")):
             dst_val = "192.168.0.95"
         elif (dst_val.startswith("05")):
             dst_val = "192.168.0.97"
         elif (dst_val.startswith("88")):
             dst_val = "192.168.0.99"
         elif (dst_val.startswith("Partron")):
             dst_val = "192.168.0.100"



         dst_val = dst_val.split('.', 1)
         #print(dst_val[1])
         if value != "":
             val_array = [value, dst_val[1], 1]
             if val_array not in src_ips:
                 if (value not in src_ips or value not in src_ips):
                     src_ips.append(val_array)
                     val_temp = val_array
             else:
                 for i in range(len(src_ips)):
                     if src_ips[i] == val_array:
                         val_temp = val_temp
                         val_temp[2] = val_temp[2] + 1
                         src_ips[i] = val_temp

finale = collapse_IPS(sO_values)
src_ips = collapse_src_IPS(src_ips)
#set_Up_Relationship(outputFile, finale, dest_ips)
set_Up_Src_Relationship(outputFile, src_ips, finale)
outputFile.close()
