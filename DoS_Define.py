
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
src_ips = []
val_temp = []



ip_dict = {"Sichuani_4b:ae:ba": "192.168.0.13", "EFMNetwo_d7:1c:56": "192.168.0.1", "Apple_c9:bf:fc": "192.168.0.125", "fe80::44c:2fec:17e8:c1f5": "10.0.0.1", "SamsungE_d6:5d:9c": "192.168.0.23" , "bc:e8:2f:2a:20:ee":"15.5.5.5"
           , "bc:1c:92:4b:ae:ba":"192.168.0.13", "bc:1c:01:b2:33:ba":"192.168.0.2"}


#Place Label on Traffic for better identifier for GBAD ('high' is better than 10,11,12)
def traffic_label(number):
        if int(number) >= 500:
            return "High"
        elif int(number) >= 100:
            return "Medium"
        elif int(number) < 100:
            return "Low"



#def count_src_usage():
    #for i in

#Cut out Traffic Values to make Relationship Checking Easier
def cut_out_vals(array):
    temp_array = []
    for i in range(0, len(array)):
        temp_array.append([array[i][0], array[i][1]])
    print(temp_array)
    return temp_array


#Corrects Error where there are Duplicate IPS sending traffic to Destination IP
def collapse_IPS(array):
    counter_temp = 0

    # print(array)
    temp_arr = cut_out_vals(array)
    temp_list = []
    temp_final = []

    #Pseudo Set for Source IP names
    for i in array:
        if i not in temp_list:
            temp_list.append(i)


    # #Count traffic sent between each Relationship
    # value = 0
    # for i in temp_list:
    #     counterx = 0
    #     for q in array:
    #         if i[0] == q[0] and i[1] == q[1]:
    #             counterx += 1
    #     if (str(i[0][0]).isdigit()):
    #     temp_final.append([value,i[1], counterx])


    #Reset Array to Fixed Array
    array = temp_list
    print(temp_list)
    return array



#Start Next Example (XP)
#Default Value: 15 Seconds
def XP_New(Stime, CTime):
    global xp_counter, starting_time, current_time, vertex_number, dest_ips
    if ((int(CTime) - int(Stime)) >= 15):
        Stime = current_time
        outputFile.write("XP # " + str(xp_counter) + "  // Stime Tag: " + str(current_time) + "  \n")
        xp_counter += 1
        vertex_number = 1
        starting_time = Stime
        dest_ips = []

#Label Node for Destination IP for Better Anomaly Recogniton by GBAD
def item_type(dest_IP):
    system = ""
    if(dest_IP.startswith("Sichuani")):
            dest_IP = ip_dict['Sichuani_4b:ae:ba']
    elif (dest_IP.startswith("EFM")):
            dest_IP = ip_dict['EFMNetwo_d7:1c:56']
    elif (dest_IP.startswith("Apple")):
        dest_IP = ip_dict['Apple_c9:bf:fc']
    elif (dest_IP.startswith("fe80") or dest_IP.startswith("ff")):
        dest_IP = ip_dict['fe80::44c:2fec:17e8:c1f5']
    elif (dest_IP.startswith("Sam")):
        dest_IP = ip_dict['SamsungE_d6:5d:9c']

    if (dest_IP.startswith("192")):
        system = "Workstation"
    elif (dest_IP.startswith("222")):
        system = "Outsider"
    else:
        system = "Other"
    return system

#Label Node for Source IP for Better Anomaly Recogniton by GBAD
def src_item_type(src_IP):
    system = ""
    if (src_IP.startswith("57")):
        system = "Local"
    # elif (src_IP.startswith("10.")):
    #     system = "Internet"
    else:
        system = "Sender"
    return system


#Label Node for First Octet for Better Anomaly Recogniton by GBAD
def first_octet_item_type(src_IP):
    system = ""
    if (src_IP.startswith("192")):
        system = "Local"
    else:
        system = "Outside Domain"
    return system


#A check to make sure given Destination IP is contained within the Array of values
def dest_check(dest, ips):
    val_check = 0
    for i in range(0, len(ips)):
            if (ips[i] == dest):
                val_check = i + 1
    return val_check


#Set Up Relationships to Clean up how Graph File looks
#**Improves Readibility this way*
def set_Up_Relationship(file, array, dest_ips):
    global vertex_number


    # #Call to Traffic Label to get Traffic Label
    # for i in array:
    #     label = traffic_label(i[2])
    #     i[2] = label

    src_ip_array = []
    counter = 0

    #For Loop to Traverse through values in Array
    for i in array:
        if array[counter][1] in dest_ips:

            #Create Vertice and Connection of Sender Nodes
            outputFile.write('v ')
            outputFile.write(str(vertex_number))
            outputFile.write(' ')
            outputFile.write('\"')
            src_type = src_item_type(array[counter][0])
            outputFile.write(src_type)
            outputFile.write('\"')
            outputFile.write('\n')
            target_vertex = vertex_number
            vertex_number += 1

            #Relationship from Sender to Destination IP
            outputFile.write(directed_edge)
            outputFile.write(' ')
            outputFile.write(str(target_vertex))  ##
            outputFile.write(' ')
            destination = dest_check(array[counter][1], dest_ips)
            outputFile.write(str(destination))
            outputFile.write(' ')
            outputFile.write("\"" + str(array[counter][2]) + "\"\n")


            #Split up IP Address Nodes
            src_ip_array.append(array[counter][0].split('.', 1))
            src_node_vertex = vertex_number

            #First Octet Vertice
            outputFile.write('v ')
            outputFile.write(str(vertex_number))
            outputFile.write(' ')
            outputFile.write('\"')
            first_octype = first_octet_item_type(src_ip_array[counter][0])
            outputFile.write(first_octype)
            outputFile.write('\"')
            outputFile.write('\n')
            target_vertex = vertex_number
            vertex_number += 1

            #Relationship to First Octet
            outputFile.write(directed_edge)
            outputFile.write(' ')
            outputFile.write(str(target_vertex))  ##
            outputFile.write(' ')
            outputFile.write(str(target_vertex - 1))
            outputFile.write(' ')
            outputFile.write("\"First Octet\"\n")

            # Second Octet Vertice
            outputFile.write('v ')
            outputFile.write(str(vertex_number))
            outputFile.write(' ')
            outputFile.write('\"')
            print(src_ip_array[counter])
            outputFile.write(src_ip_array[counter][1])
            outputFile.write('\"')
            outputFile.write('\n')
            target_vertex = vertex_number
            vertex_number += 1
            #
            #Relationship to the Second Octet
            outputFile.write(directed_edge)
            outputFile.write(' ')
            outputFile.write(str(target_vertex))  ##
            outputFile.write(' ')
            outputFile.write(str(src_node_vertex))
            outputFile.write(' ')
            outputFile.write("\"End of IP\"\n")
            #
            # # Third Octet Vertice
            # outputFile.write('v ')
            # outputFile.write(str(vertex_number))
            # outputFile.write(' ')
            # outputFile.write('\"')
            # outputFile.write(src_ip_array[counter][2])
            # outputFile.write('\"')
            # outputFile.write('\n')
            # target_vertex = vertex_number
            # vertex_number += 1
            #
            # #Relationship to Third Octet
            # outputFile.write(directed_edge)
            # outputFile.write(' ')
            # outputFile.write(str(target_vertex))  ##
            # outputFile.write(' ')
            # outputFile.write(str(src_node_vertex))
            # outputFile.write(' ')
            # outputFile.write("\"Third Octet\"\n")
            #
            # # Fourth Octet Vertice
            # outputFile.write('v ')
            # outputFile.write(str(vertex_number))
            # outputFile.write(' ')
            # outputFile.write('\"')
            # outputFile.write(src_ip_array[counter][3])
            # outputFile.write('\"')
            # outputFile.write('\n')
            # target_vertex = vertex_number
            # vertex_number += 1
            #
            # #Relationship to the Fourth Octet
            # outputFile.write(directed_edge)
            # outputFile.write(' ')
            # outputFile.write(str(target_vertex))  ##
            # outputFile.write(' ')
            # outputFile.write(str(src_node_vertex))
            # outputFile.write(' ')
            # outputFile.write("\"Fourth Octet\"\n")



            counter += 1



def call_src(count):
    global filename, vertex_number, src_ips, dest_ips

    count2 = count

    val_array = []
    val_temp = []


    gtd_list = []
    with open(filename, newline='', encoding='latin1') as rows:
        row_reader = csv.DictReader(rows, delimiter=',')
        for row in row_reader:
            gtd_list.append(dict(row))

            value = row['srcip']
            if (value.startswith("Sichuani")):
                value = ip_dict['Sichuani_4b:ae:ba']
            elif (value.startswith("EFM")):
                value = ip_dict['EFMNetwo_d7:1c:56']
            elif (value.startswith("Apple")):
                value = ip_dict['Apple_c9:bf:fc']
            elif (value.startswith("fe80") or value.startswith("ff") or value.startswith("Par")):
                value = ip_dict['fe80::44c:2fec:17e8:c1f5']
            elif (value.startswith("Sam")):
                value = ip_dict['SamsungE_d6:5d:9c']
            elif (value.startswith("bc") or value.startswith("48")):
                value = "192.168.0.2"

            dst_val = row['dstip']
            if (dst_val.startswith("Sichuani")):
                dst_val = ip_dict['Sichuani_4b:ae:ba']
            elif (dst_val.startswith("EFM")):
                dst_val = ip_dict['EFMNetwo_d7:1c:56']
            elif (dst_val.startswith("Apple")):
                dst_val = ip_dict['Apple_c9:bf:fc']
            elif (dst_val.startswith("fe80") or dst_val.startswith("ff") or dst_val.startswith('Par')):
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
            elif (dst_val.startswith("88") or dst_val.startswith("48")):
                dst_val = "192.168.0.99"

            if value != "":
                val_array = [value, dst_val, 1]
                if val_array not in src_ips:
                    if (value not in src_ips or dst_val not in dest_ips):
                        src_ips.append(val_array)
                        val_temp = val_array
                else:
                    for i in range(len(src_ips)):
                        if src_ips[i][0] == value and src_ips[i][1] == dst_val:
                            val_temp = val_temp
                            val_temp[2] = val_temp[2] + 1
                            src_ips[i] = val_temp
                            print(val_temp)

            if (count2 <= 0):
                break

            count2 -= 1

    src_ips = collapse_IPS(src_ips)

    set_Up_Relationship(outputFile, src_ips, dest_ips)




    # #print(count)
    # # Run Through CSV file and Extract Data
    # gtd_list = []
    # with open(filename, newline='', encoding='latin1') as rows:
    #     row_reader = csv.DictReader(rows, delimiter=',')
    #     for row in row_reader:
    #         gtd_list.append(dict(row))
    #
    #         value = row['srcip']
    #         if (value.startswith("Sichuani")):
    #             value = ip_dict['Sichuani_4b:ae:ba']
    #         elif (value.startswith("EFM")):
    #             value = ip_dict['EFMNetwo_d7:1c:56']
    #             #print(value)
    #         elif (value.startswith("Apple")):
    #             value = ip_dict['Apple_c9:bf:fc']
    #         elif (value.startswith("fe80") or value.startswith("ff")):
    #             value = ip_dict['fe80::44c:2fec:17e8:c1f5']
    #         elif (value.startswith("Sam")):
    #             value = ip_dict['SamsungE_d6:5d:9c']
    #         elif (value.startswith("bc")):
    #             value = "192.168.0.2"
    #
    #         dst_val = row['dstip']
    #         if (dst_val.startswith("Sichuani")):
    #             dst_val = ip_dict['Sichuani_4b:ae:ba']
    #         elif (dst_val.startswith("EFM")):
    #             dst_val = ip_dict['EFMNetwo_d7:1c:56']
    #         elif (dst_val.startswith("Apple")):
    #             dst_val = ip_dict['Apple_c9:bf:fc']
    #         elif (dst_val.startswith("fe80") or value.startswith("ff")):
    #             dst_val = ip_dict['fe80::44c:2fec:17e8:c1f5']
    #         elif (dst_val.startswith("Sam")):
    #             dst_val = ip_dict['SamsungE_d6:5d:9c']
    #         elif (dst_val.startswith("bc")):
    #             dst_val = "192.168.0.2"
    #         elif (dst_val.startswith("Broad")):
    #             dst_val = "10.0.0.1"
    #         elif (dst_val.startswith("a8")):
    #             dst_val = "192.168.0.95"
    #         elif (dst_val.startswith("fb")):
    #             dst_val = "192.168.0.95"
    #         elif (dst_val.startswith("05")):
    #             dst_val = "192.168.0.97"
    #         elif (dst_val.startswith("88")):
    #             dst_val = "192.168.0.99"
    #
    #         if (count <= 0):
    #             break
    #
    #         count -= 0
    #
    #         value = row['srcip']
    #         #print(value)   ##
    #         if (value.startswith("Sichuani")):
    #             value = ip_dict['Sichuani_4b:ae:ba']
    #         elif (value.startswith("EFM")):
    #             value = ip_dict['EFMNetwo_d7:1c:56']
    #             #print(value)
    #         elif (value.startswith("Apple")):
    #             value = ip_dict['Apple_c9:bf:fc']
    #         elif (value.startswith("fe80") or value.startswith("ff")):
    #             value = ip_dict['fe80::44c:2fec:17e8:c1f5']
    #         elif (value.startswith("Sam")):
    #             value = ip_dict['SamsungE_d6:5d:9c']
    #         elif (value.startswith("bc")):
    #             value = "192.168.0.2"
    #
    #         dst_val = row['dstip']
    #         if (dst_val.startswith("Sichuani")):
    #             dst_val = ip_dict['Sichuani_4b:ae:ba']
    #         elif (dst_val.startswith("EFM")):
    #             dst_val = ip_dict['EFMNetwo_d7:1c:56']
    #         elif (dst_val.startswith("Apple")):
    #             dst_val = ip_dict['Apple_c9:bf:fc']
    #         elif (dst_val.startswith("fe80") or value.startswith("ff")):
    #             dst_val = ip_dict['fe80::44c:2fec:17e8:c1f5']
    #         elif (dst_val.startswith("Sam")):
    #             dst_val = ip_dict['SamsungE_d6:5d:9c']
    #         elif (dst_val.startswith("bc")):
    #             dst_val = "192.168.0.2"
    #         elif (dst_val.startswith("Broad")):
    #             dst_val = "10.0.0.1"
    #         elif (dst_val.startswith("a8")):
    #             dst_val = "192.168.0.95"
    #         elif (dst_val.startswith("fb")):
    #             dst_val = "192.168.0.95"
    #         elif (dst_val.startswith("05")):
    #             dst_val = "192.168.0.97"
    #         elif (dst_val.startswith("88")):
    #             dst_val = "192.168.0.99"
    #
    #         outputFile.write('v ')
    #         outputFile.write(str(vertex_number))
    #         outputFile.write(' ')
    #         outputFile.write('\"')
    #         outputFile.write(value)
    #         outputFile.write('\"')
    #         outputFile.write("\t// " + value)
    #         outputFile.write('\n')
    #         target_vertex = vertex_number
    #         information_vertex = vertex_number
    #         vertex_number += 1
    #
    #         # Relationship to the Second Octet
    #         outputFile.write(directed_edge)
    #         outputFile.write(' ')
    #         outputFile.write(str(target_vertex))  ##
    #         outputFile.write(' ')
    #         for i in range(0, len(dest_ips)):
    #             if dest_ips[i] == dst_val:
    #                 int_val = i + 1
    #                 outputFile.write(str(int_val))
    #         outputFile.write(' ')
    #         outputFile.write("\"Rest of IP""\"\n")




#Create G File
outputFile = open("DDoSGraph.g", "w")


#Limit Values for Quicker Testing
N = 10000

src_counter = 0

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

         # Print Statement to ensure Program is Still Running
         counter += 1
         if counter % 500 == 0:
             print(str(counter))

         val_check = 0


         #Create New XP every 15 Seconds
         current_time =  row['Stime']
         # print(str(current_time) + " --- " + str(starting_time) + '\n')
         if (int(current_time) - int(starting_time)) >= 15:


             #src_ips = collapse_IPS(src_ips)

             #print("Source Counter " + str(src_counter) + " ")

             call_src(src_counter)

             src_counter = 0




         N -= 1


         #Call New XP Check
         XP_New(starting_time, current_time)


         #Create Vertice For Destination IPs
         value = row['dstip']
         if (value.startswith("Sichuani")):
             value = ip_dict['Sichuani_4b:ae:ba']
         elif (value.startswith("EFM")):
             value = ip_dict['EFMNetwo_d7:1c:56']
         elif (value.startswith("Apple")):
             value = ip_dict['Apple_c9:bf:fc']
         elif (value.startswith("fe80") or value.startswith("ff") or value.startswith("Par")):
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

         if value != "":
                     if (value in dest_ips):
                         for i in range(0,len(dest_ips)):
                             if (dest_ips[i] == value):
                                 val_check = i
                     else:
                         dest_ips.append(value)
                         outputFile.write('v ')
                         outputFile.write(str(vertex_number))
                         outputFile.write(' ')
                         outputFile.write('\"')
                         sysType = item_type(value)
                         outputFile.write(sysType)
                         outputFile.write('\"')
                         outputFile.write("\t// " + value)
                         outputFile.write('\n')
                         target_vertex = vertex_number
                         information_vertex = vertex_number
                         vertex_number += 1




         src_counter += 1


         # if value != "":
         #     val_array = [value, dst_val, 1]
         #     if val_array not in src_ips:
         #         if (value not in src_ips or value not in src_ips):
         #             src_ips.append(val_array)
         #             val_temp = val_array
         #     else:
         #         for i in range(len(src_ips)):
         #             if src_ips[i] == val_array:
         #                 val_temp = val_temp
         #                 val_temp[2] = val_temp[2] + 1
         #                 src_ips[i] = val_temp



call_src(src_counter)
set_Up_Relationship(outputFile, src_ips, dest_ips)
outputFile.close()