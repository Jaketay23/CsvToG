#
import csv
import time
import glob
import os.path


filename = "/home/kali/Research/data/MIDAS_test/MIDAS_Test.csv"
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
dest_ips_justIPs = []
src_ips = []
val_temp = []

ip_dict = {"Sichuani_4b:ae:ba": "192.168.0.13", "EFMNetwo_d7:1c:56": "192.168.0.1", "Apple_c9:bf:fc": "192.168.0.16", "fe80::44c:2fec:17e8:c1f5": "192.168.0.23", "SamsungE_d6:5d:9c": "192.168.0.23" , "bc:e8:2f:2a:20:ee":"15.5.5.5"
           , "bc:1c:92:4b:ae:ba":"192.168.0.13", "bc:1c:01:b2:33:ba":"192.168.0.2", "Broadcast":"192.168.0.125", "Partron_45:17:b3":"192.168.0.24", "88:36:6c:d7:1c:56": "192.168.0.1", "ff02::2": "192.168.0.16",
           "bc:1c:81:4b:ae:ba":"192.168.0.13", "b4:1c:81:4b:ae:ba": "192.168.0.1", "Apple_0e:3f:54": "192.168.0.14"}



#Place Label on Traffic for better identifier for GBAD ('high' is better than 10,11,12)
def traffic_label(number):
        if int(number) >= 500:
            return "High"
        elif int(number) >= 100:
            return "Medium"
        elif int(number) < 100:
            return "Low"

#Label Node for Destination IP for Better Anomaly Recogniton by GBAD
def item_type(dest_IP):
    system = ""
    if (dest_IP.startswith("192")):
        system = "Workstation"
    elif (dest_IP.startswith("222")):
        system = "Outsider"
    else:
        system = "Other"
    return system


#Label Node for First Octet for Better Anomaly Recogniton by GBAD
def first_octet_item_type(src_IP):
    system = ""
    if (src_IP.startswith("192")):
        system = "Local"
    else:
        system = "Outside Domain"
    return system


#Start Next Example (XP)
#Default Value: 15 Seconds
def XP_New(Stime, CTime):
    global xp_counter, starting_time, current_time, vertex_number, dest_ips
    #print(CTime)
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
            if (ips[i][0] == dest):
                val_check = ips[i][1]
                ###print(val_check)
    return val_check


# #Label Node for Destination IP for Better Anomaly Recogniton by GBAD
# def item_type(dest_ip):
#     system = ""
#     if (dest_ip.startswith("192")):
#         system = "Workstation"
#     elif (dest_ip.startswith("222")):
#         system = "External"
#     else:
#         system = "Other"
#     return system


#Label Node for First Octet for Better Anomaly Recogniton by GBAD
def item_type(src_IP):
    system = ""
    if (src_IP.startswith("192") and src_IP.endswith("13")):
        system = "Sichuani"
    elif (src_IP.startswith("192") and src_IP.endswith("1")):
        system = "EFM"
    elif (src_IP.startswith("192") and src_IP.endswith("16")):
        system = "Apple"
    elif (src_IP.startswith("192") and src_IP.endswith("14")):
        system = "Apple"
    elif (src_IP.startswith("192") and src_IP.endswith("23")):
        system = "Samsung"
    elif (src_IP.startswith("192") and src_IP.endswith("24")):
        system = "Partron"
    elif (src_IP.startswith("192") and src_IP.endswith("25")):
        system = "Broadcast"
    elif (src_IP.startswith('192')):
        system = "Workstation"
    elif (src_IP.startswith("222") and src_IP.startswith("111")):
        system = "External"
    elif (src_IP.startswith("210.89")):
        system = "Mirai HTTP"
    else:
        system = "Other"
    return system


#Set Up Relationships to Clean up how Graph File looks
#**Improves Readibility this way*
def set_Up_Relationship(file, array, dest_ips):
    global vertex_number


    #Call to Traffic Label to get Traffic Label
    for i in array:
        label = traffic_label(i[2])
        i[2] = label

    src_ip_array = []
    counter = 0


    #For Loop to Traverse through values in Array
    for i in array:
            #print(i)
            if("." not in array[counter][1]):
                print(array[counter][1])
                array[counter][1] = "192.169.0.13"

            #Create Vertice and Connection of Sender Nodes
            outputFile.write('v ')
            outputFile.write(str(vertex_number))
            outputFile.write(' ')
            outputFile.write('\"')
            #src_type = item_type(array[counter][1])
            outputFile.write("Sender")
            #outputFile.write(array[counter][1])
            outputFile.write('\"')
            outputFile.write('\n')
            target_vertex = vertex_number
            vertex_number += 1

            #Relationship from Sender to Destination IP
            outputFile.write(directed_edge)
            outputFile.write(' ')
            outputFile.write(str(target_vertex))  ##
            outputFile.write(' ')
            destination = dest_check(array[counter][0], dest_ips)
            outputFile.write(str(destination))
            outputFile.write(' ')
            outputFile.write("\"" + str(array[counter][2]) + "\"\n")
            #
            #Split up IP Address Nodes
            src_ip_array.append(array[counter][1].split('.', 3))
            src_node_vertex = vertex_number - 1


            #First Octet Vertice
            outputFile.write('v ')
            outputFile.write(str(vertex_number))
            outputFile.write(' ')
            outputFile.write('\"')
            #first_octype = item_type(src_ip_array[counter][0])
            outputFile.write(src_ip_array[counter][0])
            outputFile.write('\"')
            outputFile.write('\n')
            target_vertex = vertex_number
            vertex_number += 1

            #Relationship to First Octet
            outputFile.write(directed_edge)
            outputFile.write(' ')
            outputFile.write(str(target_vertex))  ##
            outputFile.write(' ')
            # destination = dest_check(array[counter][0], dest_ips)
            # outputFile.write(str(destination))
            sender_v = src_node_vertex
            outputFile.write(str(sender_v))
            outputFile.write(' ')
            # outputFile.write("\"" + str(array[counter][2]) + "\"\n")
            outputFile.write("\"First Octet\"\n")

            # Second Octet Vertice
            outputFile.write('v ')
            outputFile.write(str(vertex_number))
            outputFile.write(' ')
            outputFile.write('\"')
            ##print(src_ip_array[counter])
            #print(src_ip_array[counter])
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
            outputFile.write("\"Second Octet\"\n")
            #
            # Third Octet Vertice
            outputFile.write('v ')
            outputFile.write(str(vertex_number))
            outputFile.write(' ')
            outputFile.write('\"')
            outputFile.write(src_ip_array[counter][2])
            outputFile.write('\"')
            outputFile.write('\n')
            target_vertex = vertex_number
            vertex_number += 1

            #Relationship to Third Octet
            outputFile.write(directed_edge)
            outputFile.write(' ')
            outputFile.write(str(target_vertex))  ##
            outputFile.write(' ')
            outputFile.write(str(src_node_vertex))
            outputFile.write(' ')
            outputFile.write("\"Third Octet\"\n")

            # Fourth Octet Vertice
            outputFile.write('v ')
            outputFile.write(str(vertex_number))
            outputFile.write(' ')
            outputFile.write('\"')
            #value = last_octet_item_type(src_ip_array[counter][0], src_ip_array[counter][3])
            outputFile.write(src_ip_array[counter][3])
            outputFile.write('\"')
            outputFile.write('\n')
            target_vertex = vertex_number
            vertex_number += 1

            #Relationship to the Fourth Octet
            outputFile.write(directed_edge)
            outputFile.write(' ')
            outputFile.write(str(target_vertex))  ##
            outputFile.write(' ')
            outputFile.write(str(src_node_vertex))
            outputFile.write(' ')
            outputFile.write("\"Fourth Octet\"\n")



            counter += 1


def name_to_IP(value):
    if (value.startswith("Sichuani") or value.startswith("bc")):
        value = ip_dict['Sichuani_4b:ae:ba']
    elif (value.startswith("EFM") or value.startswith("b4") or value.startswith("88")):
        value = ip_dict['EFMNetwo_d7:1c:56']
    elif (value.startswith("Apple") or value.startswith("ff") or value.startswith("48") or value.startswith("e1")):
        value = ip_dict['Apple_c9:bf:fc']
    elif (value.startswith("Partron_45:17:b3")):
        value = ip_dict['Partron_45:17:b3']
    elif (value.startswith("Sam") or value.startswith("fe80")):
        value = ip_dict['SamsungE_d6:5d:9c']
    elif (value.startswith("ba")):
        value = "192.168.0.2"
    elif (value.startswith("Broad")):
        value = "192.168.0.125"
    elif (value.startswith("a8")):
        value = ip_dict["Apple_0e:3f:54"]
    elif (value.startswith("6e") or value.startswith("e8")):
        value = "111.0.0.0"
    elif (value.startswith("fb") or value.startswith("fc") or value.startswith("05") or value.startswith("3c") or value.startswith("96")): #Bogus IPs
        value = "222.0.0.0"
    return value

#Create G File
outputFile = open("DDoSGraph.g", "w")


#Limit Values for Quicker Testing
N = 1000000

src_counter = 0

#Start Timer
tic = time.perf_counter()
outputFile.write("XP # 1 //Time Tag: 0\n")



#Run Through CSV file and Extract Data
gtd_list = []
with open(filename, newline='', encoding='latin1') as rows:
      row_reader = csv.DictReader(rows, delimiter=',')
      num_records = 0
      temp_val = []
      counter = 0
      for row in row_reader:
         gtd_list.append(dict(row))
         num_records += 1

         # #print Statement to ensure Program is Still Running
         counter += 1
         if counter % 25000 == 0:
             print(str(counter))

         val_check = 0


         # Create New XP every 15 Seconds
         current_time = row['Stime']
         # #print(str(current_time) + " --- " + str(starting_time) + '\n')
         if (int(current_time) - int(starting_time)) >= 10:
             # src_ips = collapse_IPS(src_ips)

             # #print("Source Counter " + str(src_counter) + " ")

             set_Up_Relationship(outputFile,src_ips,dest_ips)

             src_ips = []
             dest_ips = []
             dest_ips_justIPs = []

             src_counter = 0

         if N == 0:
             break

         N -= 1


         #Call New XP Check
         XP_New(starting_time, current_time)


         #Create Vertice For Destination IPs
         dst_val = row['dstip']
         value = name_to_IP(dst_val)


         if value != "":
                     if (value in dest_ips_justIPs):
                         for i in range(0,len(dest_ips)):
                             if (dest_ips[i][0] == value):
                                 val_check = i
                     else:
                         dest_ips.append([value, vertex_number])
                         dest_ips_justIPs.append(value)
                         outputFile.write('v ')
                         outputFile.write(str(vertex_number))
                         outputFile.write(' ')
                         outputFile.write('\"')
                         #sysType = item_type(value)
                         #outputFile.write(sysType)
                         outputFile.write(value)
                         outputFile.write('\"')
                         outputFile.write("\t// " + value)
                         outputFile.write('\n')
                         target_vertex = vertex_number
                         information_vertex = vertex_number
                         vertex_number += 1


         #Create Vertice For Destination IPs
         src_val = row['srcip']
         src_val = name_to_IP(src_val)
         ##print(src_val)

         if src_val != "":
             if (src_counter == 0):
                 src_ips.append([value, src_val, 1])
                 #print(src_ips)
             else:
                 run = 0
                 for i in range(0, len(src_ips)):
                            if (src_ips[i][0] == value and src_ips[i][1] == src_val):
                                 src_ips[i][2] = src_ips[i][2] + 1
                                 run = 1

                 if (run == 0):
                    src_ips.append([value,src_val,1])
                    ##print(src_ips)



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

##print(src_ips)
set_Up_Relationship(outputFile,src_ips,dest_ips)