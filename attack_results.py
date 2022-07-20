import csv
import subprocess as sp

filename = "/home/kali/Research/results/Attack_Approach2.csv"

import sys
f = open("test2.out", 'w')
sys.stdout = f

NUGU_counter, NUGU_MIDAS_correct, NUGU_MIDASR_correct,NUGU_MIDASF_correct, NUGU_Sedan_correct = (0,0,0,0,0)
EZVIZ_counter, EZVIZ_MIDAS_correct, EZVIZ_MIDASR_correct,EZVIZ_MIDASF_correct, EZVIZ_Sedan_correct = (0,0,0,0,0)
EZVIZ_DoS_MIDAS, EZVIZ_DoS_MIDASF, EZVIZ_DoS_MIDASR, EZVIZ_DoS_SedanSpot, EZVIZ_DoS  = (0,0,0,0,0)
NUGU_DoS_MIDAS, NUGU_DoS_MIDASF, NUGU_DoS_MIDASR, NUGU_DoS_SedanSpot, NUGU_DoS = (0,0,0,0,0)
EZVIZ_MitM_MIDAS, EZVIZ_MitM_MIDASF, EZVIZ_MitM_MIDASR, EZVIZ_MitM_SedanSpot, EZVIZ_MitM  = (0,0,0,0,0)
NUGU_MitM_MIDAS, NUGU_MitM_MIDASF, NUGU_MitM_MIDASR, NUGU_MitM_SedanSpot, NUGU_MitM = (0,0,0,0,0)
EZVIZ_Mirai_HTTP_MIDAS, EZVIZ_Mirai_HTTP_MIDASF, EZVIZ_Mirai_HTTP_MIDASR, EZVIZ_Mirai_HTTP_SedanSpot,EZVIZ_Mirai_HTTP  = (0,0,0,0,0)
NUGU_Mirai_HTTP_MIDAS, NUGU_Mirai_HTTP_MIDASF, NUGU_Mirai_HTTP_MIDASR, NUGU_Mirai_HTTP_SedanSpot,NUGU_Mirai_HTTP = (0,0,0,0,0)
EZVIZ_Mirai_UDP_MIDAS, EZVIZ_Mirai_UDP_MIDASF, EZVIZ_Mirai_UDP_MIDASR, EZVIZ_Mirai_UDP_SedanSpot, EZVIZ_Mirai_UDP  = (0,0,0,0,0)
NUGU_Mirai_UDP_MIDAS, NUGU_Mirai_UDP_MIDASF, NUGU_Mirai_UDP_MIDASR, NUGU_Mirai_UDP_SedanSpot, NUGU_Mirai_UDP = (0,0,0,0,0)
EZVIZ_Mirai_bruteforce_MIDAS, EZVIZ_Mirai_bruteforce_MIDASF, EZVIZ_Mirai_bruteforce_MIDASR, EZVIZ_Mirai_bruteforce_SedanSpot, EZVIZ_Mirai_bruteforce  = (0,0,0,0,0)
NUGU_Mirai_bruteforce_MIDAS, NUGU_Mirai_bruteforce_MIDASF, NUGU_Mirai_bruteforce_MIDASR, NUGU_Mirai_bruteforce_SedanSpot, NUGU_Mirai_bruteforce = (0,0,0,0,0)
EZVIZ_Mirai_ack_MIDAS, EZVIZ_Mirai_ack_MIDASF, EZVIZ_Mirai_ack_MIDASR, EZVIZ_Mirai_ack_SedanSpot, EZVIZ_Mirai_ack  = (0,0,0,0,0)
NUGU_Mirai_ack_MIDAS, NUGU_Mirai_ack_MIDASF, NUGU_Mirai_ack_MIDASR, NUGU_Mirai_ack_SedanSpot, NUGU_Mirai_ack = (0,0,0,0,0)
EZVIZ_Hostport_MIDAS, EZVIZ_Hostport_MIDASF, EZVIZ_Hostport_MIDASR, EZVIZ_Hostport_SedanSpot, EZVIZ_Hostport  = (0,0,0,0,0)
NUGU_Hostport_MIDAS, NUGU_Hostport_MIDASF, NUGU_Hostport_MIDASR, NUGU_Hostport_SedanSpot, NUGU_Hostport = (0,0,0,0,0)
EZVIZ_PortOS_MIDAS, EZVIZ_PortOS_MIDASF, EZVIZ_PortOS_MIDASR, EZVIZ_PortOS_SedanSpot,EZVIZ_PortOS  = (0,0,0,0,0)
NUGU_PortOS_MIDAS, NUGU_PortOS_MIDASF, NUGU_PortOS_MIDASR, NUGU_PortOS_SedanSpot, NUGU_PortOS = (0,0,0,0,0)
counter, ben_counter = (0,0)
fcheck = 0
rcheck = 0
mcheck = 0
scheck = 0

array = []
MIDAS_fn, MIDASR_fn, MIDASF_fn, Sedan_fn = (0,0,0,0)

column_names = ['Benign',
'Denial of Service attack on EZVIZ Camera',
'Denial of Service attack on NUGU',
'Mirai Botnet Attack - Ack Flooding - Perfomed by EZVIZ',
'Mirai Botnet Attack - Ack Flooding - Perfomed by NUGU',
'Mirai Botnet Attack - Host Brute Force - Perfomed by EVZIZ - Target: NUGU',
'Mirai Botnet Attack - Host Brute Force - Perfomed by NUGU - Target: EVZIZ',
'Mirai Botnet Attack - HTTP Flooding - Perfomed by EZVIZ - Target: External Server',
'Mirai Botnet Attack - HTTP Flooding - Perfomed by NUGU - Target: External Server',
'Mirai Botnet Attack - UDP Flooding - Perfomed by EZVIZ - Target: External Server',
'Mirai Botnet Attack - UDP Flooding - Perfomed by NUGU - Target: External Server',
'Man in the Middle Attack on EZVIZ', 'Man in the Middle Attack on NUGU',
'Host Discovery/Port Scanning on EVZIZ', 'Host Discovery/Port Scanning on NUGU',
'Port Scanning/OS Detection on EVZIZ', 'Port Scanning/OS Detection on NUGU']
x, x1, x2, x3 = (0,0,0,0)


with open(filename, newline='', encoding='latin1') as rows:
    row_reader = csv.DictReader(rows, delimiter=',')
    for row in row_reader:
        if (row['Attack'] in column_names):
            value = column_names.index(row['Attack'])
            #print(value)
            array.append([value,int(row['MIDAS']), int(row['MIDASR']), int(row['MIDASF']), int(row['SedanSpot'])])
            #print(array)
            if int(row['MIDASF']) == 1:
                x += 1
            if int(row['MIDASR']) == 1:
                x1 += 1
            if int(row['MIDAS']) == 1:
                x2 += 1
            if int(row['SedanSpot']) == 1:
                x3 += 1
        else:
            print(row['Attack'])


#print(str(x) + "-" + str(x1) + "-" + str(x2)+ "-" + str(x3))

for i in range(0, len(array)):

            counter += 1
            if array[i][0] == 0:
                ben_counter += 1
                if(array[i][1] == 1):
                    MIDAS_fn += 1
                    #print(array)
                if (array[i][2] == 1):
                    MIDASR_fn += 1
                if (array[i][3] == 1):  # 194184
                    MIDASF_fn += 1
                if (array[i][4] == 1):
                    Sedan_fn += 1

          #NUGU Data Capture
            #if (array[i][0] == "Mirai Botnet Attack - HTTP Flooding - Perfomed by NUGU - Target: External Server"):
            if (array[i][0] == 10):
                NUGU_counter += 1
                NUGU_Mirai_UDP += 1
                if (array[i][1]== 1):
                    NUGU_Mirai_UDP_MIDAS += 1
                    NUGU_MIDAS_correct += 1
                if (array[i][2]== 1):
                    NUGU_Mirai_UDP_MIDASR += 1
                    NUGU_MIDASR_correct += 1
                if (array[i][3]== 1): #194184
                    NUGU_Mirai_UDP_MIDASF += 1
                    NUGU_MIDASF_correct += 1
                if (array[i][4]== 1):
                    NUGU_Mirai_UDP_SedanSpot += 1
                    NUGU_Sedan_correct += 1

            #if (array[i][0] =="Mirai Botnet Attack - Ack Flooding - Perfomed by NUGU"):
            if (array[i][0] == 4):
                NUGU_counter += 1
                NUGU_Mirai_ack += 1
                if (array[i][1]== 1):
                    NUGU_Mirai_ack_MIDAS += 1
                    NUGU_MIDAS_correct += 1
                if (array[i][2]== 1):
                    NUGU_Mirai_ack_MIDASR += 1
                    NUGU_MIDASR_correct += 1
                if (array[i][3]== 1):
                    NUGU_Mirai_ack_MIDASF += 1
                    NUGU_MIDASF_correct += 1
                if (array[i][4]== 1):
                    NUGU_Mirai_ack_SedanSpot += 1
                    NUGU_Sedan_correct += 1

            #if (array[i][0] == "Mirai Botnet Attack - HTTP Flooding - Perfomed by NUGU - Target: External Server" ):
            if (array[i][0] == 8):
                NUGU_counter += 1
                NUGU_Mirai_HTTP += 1
                if (array[i][1]== 1):
                    NUGU_Mirai_HTTP_MIDAS += 1
                    NUGU_MIDAS_correct += 1
                if (array[i][2]== 1):
                    NUGU_Mirai_HTTP_MIDASR += 1
                    NUGU_MIDASR_correct += 1
                if (array[i][3]== 1):
                    NUGU_Mirai_HTTP_MIDASF += 1
                    NUGU_MIDASF_correct += 1
                if (array[i][4]== 1):
                    NUGU_Mirai_HTTP_SedanSpot += 1
                    NUGU_Sedan_correct += 1

            #if (array[i][0] =="Mirai Botnet Attack - Host Brute Force - Perfomed by NUGU - Target: EVZIZ"):
            if (array[i][0] == 6):
                NUGU_counter += 1
                NUGU_Mirai_bruteforce += 1
                if (array[i][1]== 1):
                    NUGU_Mirai_bruteforce_MIDAS += 1
                    NUGU_MIDAS_correct += 1
                if (array[i][2]== 1):
                    NUGU_Mirai_bruteforce_MIDASR += 1
                    NUGU_MIDASR_correct += 1
                if (array[i][3]== 1):
                    NUGU_Mirai_bruteforce_MIDASF += 1
                    NUGU_MIDASF_correct += 1
                if (array[i][4]== 1):
                    NUGU_Mirai_bruteforce_SedanSpot += 1
                    NUGU_Sedan_correct += 1

            #if (array[i][0] =="Man in the Middle Attack on NUGU"):
            if (array[i][0] == 12):
                NUGU_counter += 1
                NUGU_MitM += 1
                if (array[i][1]== 1):
                    NUGU_MitM_MIDAS += 1
                    NUGU_MIDAS_correct += 1
                if (array[i][2]== 1):
                    NUGU_MitM_MIDASR += 1
                    NUGU_MIDASR_correct += 1
                if (array[i][3]== 1):
                    NUGU_MitM_MIDASF += 1
                    NUGU_MIDASF_correct += 1
                if (array[i][4]== 1):
                    NUGU_MitM_SedanSpot += 1
                    NUGU_Sedan_correct += 1

            #if (array[i][0] == "Port Scanning/OS Detection on NUGU"):
            if (array[i][0] == 16):
                NUGU_counter += 1
                NUGU_PortOS += 1
                #print(array[i])
                #print(len(array[i]))
                if (array[i][1]== 1):
                    NUGU_PortOS_MIDAS += 1
                    NUGU_MIDAS_correct += 1
                if (array[i][2]== 1):
                    NUGU_PortOS_MIDASR += 1
                    NUGU_MIDASR_correct += 1
                if (array[i][3]== 1):
                    NUGU_PortOS_MIDASF += 1
                    NUGU_MIDASF_correct += 1
                if (array[i][4]== 1):
                    NUGU_PortOS_SedanSpot += 1
                    NUGU_Sedan_correct += 1

            #if (array[i][0] == "Host Discovery/Port Scanning on NUGU"):
            if (array[i][0] == 14):
                NUGU_counter += 1
                NUGU_Hostport += 1
                if (array[i][1]== 1):
                    NUGU_Hostport_MIDAS += 1
                    NUGU_MIDAS_correct += 1
                if (array[i][2]== 1):
                    NUGU_Hostport_MIDASR += 1
                    NUGU_MIDASR_correct += 1
                if (array[i][3]== 1):
                    NUGU_Hostport_MIDASF += 1
                    NUGU_MIDASF_correct += 1
                if (array[i][4]== 1):
                    NUGU_Hostport_SedanSpot += 1
                    NUGU_Sedan_correct += 1

            #if (array[i][0] =="Denial of Service attack on NUGU"):
            if (array[i][0] == 2):
                NUGU_counter += 1
                NUGU_DoS += 1
                if (array[i][1]== 1):
                    NUGU_DoS_MIDAS += 1
                    NUGU_MIDAS_correct += 1
                if (array[i][2]== 1):
                    NUGU_DoS_MIDASR += 1
                    NUGU_MIDASR_correct += 1
                if (array[i][3]== 1):
                    NUGU_DoS_MIDASF += 1
                    NUGU_MIDASF_correct += 1
                if (array[i][4]== 1):
                    NUGU_DoS_SedanSpot += 1
                    NUGU_Sedan_correct += 1




            # EZVIZ Data Capture
            #if (array[i][0] == "Mirai Botnet Attack - UDP Flooding - Perfomed by EZVIZ - Target: External Server"):
            if (array[i][0] == 9):
                EZVIZ_counter += 1
                EZVIZ_Mirai_UDP += 1
                if (array[i][1]== 1):
                    EZVIZ_MIDAS_correct += 1
                    EZVIZ_Mirai_UDP_MIDAS += 1
                if (array[i][2]== 1):
                    EZVIZ_MIDASR_correct += 1
                    EZVIZ_Mirai_UDP_MIDASR += 1
                if (array[i][3]== 1):
                    EZVIZ_MIDASF_correct += 1
                    EZVIZ_Mirai_UDP_MIDASF += 1
                if (array[i][4]== 1):
                    EZVIZ_Mirai_UDP_SedanSpot += 1
                    EZVIZ_Sedan_correct += 1
            #if (array[i][0] == "Mirai Botnet Attack - Ack Flooding - Perfomed by EZVIZ" ):
            if (array[i][0] == 3):
                EZVIZ_counter += 1
                EZVIZ_Mirai_ack += 1
                if (array[i][1]== 1):
                    EZVIZ_MIDAS_correct += 1
                    EZVIZ_Mirai_ack_MIDAS += 1
                if (array[i][2]== 1):
                    EZVIZ_MIDASR_correct += 1
                    EZVIZ_Mirai_ack_MIDASR += 1
                if (array[i][3]== 1):
                    EZVIZ_MIDASF_correct += 1
                    EZVIZ_Mirai_ack_MIDASF += 1
                if (array[i][4]== 1):
                    EZVIZ_Mirai_ack_SedanSpot += 1
                    EZVIZ_Sedan_correct += 1
            #if (array[i][0] == "Mirai Botnet Attack - HTTP Flooding - Perfomed by EZVIZ - Target: External Server"):
            if (array[i][0] == 7):
                EZVIZ_counter += 1
                EZVIZ_Mirai_HTTP += 1
                if (array[i][1]== 1):
                    EZVIZ_MIDAS_correct += 1
                    EZVIZ_Mirai_HTTP_MIDAS += 1
                if (array[i][2]== 1):
                    EZVIZ_MIDASR_correct += 1
                    EZVIZ_Mirai_HTTP_MIDASR += 1
                if (array[i][3]== 1):
                    EZVIZ_MIDASF_correct += 1
                    EZVIZ_Mirai_HTTP_MIDASF += 1
                if (array[i][4]== 1):
                    EZVIZ_Mirai_HTTP_SedanSpot += 1
                    EZVIZ_Sedan_correct += 1
            #if (array[i][0] == "Mirai Botnet Attack - Host Brute Force - Perfomed by EVZIZ - Target: NUGU" ):
            if (array[i][0] == 5):
                EZVIZ_counter += 1
                EZVIZ_Mirai_bruteforce += 1
                if (array[i][1]== 1):
                    EZVIZ_MIDAS_correct += 1
                    EZVIZ_Mirai_bruteforce_MIDAS += 1
                if (array[i][2]== 1):
                    EZVIZ_MIDASR_correct += 1
                    EZVIZ_Mirai_bruteforce_MIDASR += 1
                if (array[i][3]== 1):
                    EZVIZ_MIDASF_correct += 1
                    EZVIZ_Mirai_bruteforce_MIDASF += 1
                if (array[i][4]== 1):
                    EZVIZ_Mirai_bruteforce_SedanSpot += 1
                    EZVIZ_Sedan_correct += 1

            #if (array[i][0] == "Man in the Middle Attack on EZVIZ" ):
            if (array[i][0] == 11):
                EZVIZ_counter += 1
                EZVIZ_MitM += 1
                if (array[i][1]== 1): #1229718
                    EZVIZ_MIDAS_correct += 1
                    EZVIZ_MitM_MIDAS += 1
                if (array[i][2]== 1):
                    EZVIZ_MIDASR_correct += 1
                    EZVIZ_MitM_MIDASR += 1
                if (array[i][3]== 1):
                    EZVIZ_MIDASF_correct += 1
                    EZVIZ_MitM_MIDASF += 1
                if (array[i][4]== 1):
                    EZVIZ_MitM_SedanSpot += 1
                    EZVIZ_Sedan_correct += 1

            #if (array[i][0] == "Port Scanning/OS Detection on EVZIZ" ):
            if (array[i][0] == 15):
                EZVIZ_counter += 1
                EZVIZ_PortOS += 1
                if (array[i][1]== 1):
                    EZVIZ_MIDAS_correct += 1
                    EZVIZ_PortOS_MIDAS += 1
                if (array[i][2]== 1):
                    EZVIZ_MIDASR_correct += 1
                    EZVIZ_PortOS_MIDASR += 1
                if (array[i][3]== 1):
                    EZVIZ_MIDASF_correct += 1
                    EZVIZ_PortOS_MIDASF += 1
                if (array[i][4]== 1):
                    EZVIZ_PortOS_SedanSpot += 1
                    EZVIZ_Sedan_correct += 1

            #if (array[i][0] == "Host Discovery/Port Scanning on EVZIZ" ):
            if (array[i][0] == 13):
                EZVIZ_counter += 1
                EZVIZ_Hostport += 1
                if (array[i][1]== 1):
                    EZVIZ_MIDAS_correct += 1
                    EZVIZ_Hostport_MIDAS += 1
                if (array[i][2]== 1):
                    EZVIZ_MIDASR_correct += 1
                    EZVIZ_Hostport_MIDASR += 1
                if (array[i][3]== 1):
                    EZVIZ_MIDASF_correct += 1
                    EZVIZ_Hostport_MIDASF += 1
                if (array[i][4]== 1):
                    EZVIZ_Hostport_SedanSpot += 1
                    EZVIZ_Sedan_correct += 1

            #if (array[i][0] =="Denial of Service attack on EZVIZ Camera"):
            if (array[i][0] == 1):
                EZVIZ_counter += 1
                EZVIZ_DoS += 1
                #print(array[i][1])
                #print(array[i][1])
                if (array[i][1]== 1):
                    #print("True")
                    EZVIZ_MIDAS_correct += 1
                    EZVIZ_DoS_MIDAS += 1
                if (array[i][2]== 1):
                    #print("True")
                    EZVIZ_MIDASR_correct += 1
                    EZVIZ_DoS_MIDASR += 1
                    #print(EZVIZ_DoS_MIDASR)
                if (array[i][3]== 1):
                    EZVIZ_MIDASF_correct += 1
                    EZVIZ_DoS_MIDASF += 1
                if (array[i][4]== 1):
                    EZVIZ_DoS_SedanSpot += 1
                    EZVIZ_Sedan_correct += 1



def percentage_of_attack(M,R,F,S,T):
    if(int(T) == 0):
        print("None")
        return
    M_percent = float(M)/float(T)
    M_percent = M_percent * 100
    M_percent = round(M_percent, 2)
    R_percent = float(R) / float(T)
    R_percent = R_percent * 100
    R_percent = round(R_percent, 2)
    F_percent = float(F) / float(T)
    F_percent = F_percent * 100
    F_percent = round(F_percent, 2)
    S_percent = float(S) / float(T)
    S_percent = S_percent * 100
    S_percent = round(S_percent, 2)


    print ("MIDAS: " + str(M_percent) + "% correctly classified as anomalies while missing " + str((T-M)) + " of the " + str(T) + " total anomalous packets" )
    print("MIDASR: " + str(R_percent) + "% correctly classified as anomalies while missing " + str((T - R)) + " of the " + str(T) + " total anomalous packets")
    print("MIDASF: " + str(F_percent) + "% correctly classified as anomalies while missing " + str((T - F)) + " of the " + str(T) + " total anomalous packets")
    print("SedanSpot: " + str(S_percent) + "% correctly classified as anomalies while missing " + str((T - S)) + " of the " + str(T) + " total anomalous packets" + "\n")

def percentage_total(EC, NC, T, method):
    N_percent = (float(NC) + float(EC))/ float(T)
    TC = NC + EC
    N_percent = N_percent * 100
    N_percent = round(N_percent, 2)

    if (method == 1):
        print("Total: " + str(N_percent) + "% correctly classified as anomalous while missing " + str((T - TC)) + " of the " + str(T) + " total anomalous packets")
    if method == 2:
        print("Total: " + str(N_percent) + "% of the data are false negatives with " + str((TC)) + " falsely classified out of the " + str(
            T) + " total benign packets")
    if method == 3:
        print("Total: " + str(N_percent) + "% of the data are correctly classfied with " + str(
            (TC)) + " correctly classified packets out of the " + str(
            T) + " total packets")


Attacks = ["Denial of Service", "UDP Flood", "ACK Flood", "HTTP Flood", "Man in the Middle", "Host Brute Force", "Port Scan/OS Detection", "Host Discovery/Port Scan"]

for i in range(0, len(Attacks)):
    if "Denial" in Attacks[i]:
        print("\n\n\t\t\t\tDenial of Service\n")
        print("EZVIZ\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(EZVIZ_DoS_MIDAS, EZVIZ_DoS_MIDASR, EZVIZ_DoS_MIDASF, EZVIZ_DoS_SedanSpot, EZVIZ_DoS)
        print("NUGU\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(NUGU_DoS_MIDAS, NUGU_DoS_MIDASR, NUGU_DoS_MIDASF, NUGU_DoS_SedanSpot, NUGU_DoS)
        print("Total\n" + "---------------------------------------------------------------------------")
        percentage_of_attack((EZVIZ_DoS_MIDAS+NUGU_DoS_MIDAS), (EZVIZ_DoS_MIDASR+NUGU_DoS_MIDASR), (EZVIZ_DoS_MIDASF+NUGU_DoS_MIDASF), (EZVIZ_DoS_SedanSpot+NUGU_DoS_SedanSpot), (EZVIZ_DoS+NUGU_DoS))
    if "Middle" in Attacks[i]:
        print("\n\n\t\t\t\tMan in the Middle Attack\n")
        print("EZVIZ\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(EZVIZ_MitM_MIDAS, EZVIZ_MitM_MIDASR, EZVIZ_MitM_MIDASF, EZVIZ_MitM_SedanSpot, EZVIZ_MitM)
        print("NUGU\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(NUGU_MitM_MIDAS, NUGU_MitM_MIDASR, NUGU_MitM_MIDASF, NUGU_MitM_SedanSpot, NUGU_MitM)
        print("Total\n" + "---------------------------------------------------------------------------")
        percentage_of_attack((EZVIZ_MitM_MIDAS + NUGU_MitM_MIDAS), (EZVIZ_MitM_MIDASR + NUGU_MitM_MIDASR),
                             (EZVIZ_MitM_MIDASF + NUGU_MitM_MIDASF), (EZVIZ_MitM_SedanSpot + NUGU_MitM_SedanSpot),
                             (EZVIZ_MitM + NUGU_MitM))
    if "UDP" in Attacks[i]:
        print("\n\n\t\t\t\tMirai Botnet - UDP Flooding\n")
        print("EZVIZ\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(EZVIZ_Mirai_UDP_MIDAS, EZVIZ_Mirai_UDP_MIDASR, EZVIZ_Mirai_UDP_MIDASF, EZVIZ_Mirai_UDP_SedanSpot, EZVIZ_Mirai_UDP)
        print("NUGU\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(NUGU_Mirai_UDP_MIDAS, NUGU_Mirai_UDP_MIDASR, NUGU_Mirai_UDP_MIDASF, NUGU_Mirai_UDP_SedanSpot, NUGU_Mirai_UDP)
        print("Total\n" + "---------------------------------------------------------------------------")
        percentage_of_attack((EZVIZ_Mirai_UDP_MIDAS + NUGU_Mirai_UDP_MIDAS), (EZVIZ_Mirai_UDP_MIDASR + NUGU_Mirai_UDP_MIDASR),
                             (EZVIZ_Mirai_UDP_MIDASF + NUGU_Mirai_UDP_MIDASF), (EZVIZ_Mirai_UDP_SedanSpot + NUGU_Mirai_UDP_SedanSpot),
                             (EZVIZ_Mirai_UDP + NUGU_Mirai_UDP))

    if "ACK" in Attacks[i]:
        print("\n\n\t\t\t\tMirai Botnet - ACK Flooding\n")
        print("EZVIZ\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(EZVIZ_Mirai_ack_MIDAS, EZVIZ_Mirai_ack_MIDASR, EZVIZ_Mirai_ack_MIDASF, EZVIZ_Mirai_ack_SedanSpot, EZVIZ_Mirai_ack)
        print("NUGU\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(NUGU_Mirai_ack_MIDAS, NUGU_Mirai_ack_MIDASR, NUGU_Mirai_ack_MIDASF,NUGU_Mirai_ack_SedanSpot, NUGU_Mirai_ack)
        print("Total\n" + "---------------------------------------------------------------------------")
        percentage_of_attack((EZVIZ_Mirai_ack_MIDAS + NUGU_Mirai_ack_MIDAS), (EZVIZ_Mirai_ack_MIDASR + NUGU_Mirai_ack_MIDASR),
                             (EZVIZ_Mirai_ack_MIDASF + NUGU_Mirai_ack_MIDASF), (EZVIZ_Mirai_ack_SedanSpot + NUGU_Mirai_ack_SedanSpot),
                             (EZVIZ_Mirai_ack + NUGU_Mirai_ack))
    if "HTTP" in Attacks[i]:
        print("\n\n\t\t\t\tMirai Botnet - HTTP Flooding\n")
        print("EZVIZ\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(EZVIZ_Mirai_HTTP_MIDAS, EZVIZ_Mirai_HTTP_MIDASR, EZVIZ_Mirai_HTTP_MIDASF,EZVIZ_Mirai_HTTP_SedanSpot, EZVIZ_Mirai_HTTP)
        print("NUGU\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(NUGU_Mirai_HTTP_MIDAS, NUGU_Mirai_HTTP_MIDASR, NUGU_Mirai_HTTP_MIDASF,NUGU_Mirai_HTTP_SedanSpot, NUGU_Mirai_HTTP)
        print("Total\n" + "---------------------------------------------------------------------------")
        percentage_of_attack((EZVIZ_Mirai_HTTP_MIDAS + NUGU_Mirai_HTTP_MIDAS), (EZVIZ_Mirai_HTTP_MIDASR + NUGU_Mirai_HTTP_MIDASR),
                             (EZVIZ_Mirai_HTTP_MIDASF + NUGU_Mirai_HTTP_MIDASF), (EZVIZ_Mirai_HTTP_SedanSpot + NUGU_Mirai_HTTP_SedanSpot),
                             (EZVIZ_Mirai_HTTP + NUGU_Mirai_HTTP))

    if "Brute" in Attacks[i]:
        print("\n\n\t\t\t\tMirai Botnet - Host Brute Force\n")
        print("EZVIZ\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(EZVIZ_Mirai_bruteforce_MIDAS, EZVIZ_Mirai_bruteforce_MIDASR, EZVIZ_Mirai_bruteforce_MIDASF,EZVIZ_Mirai_bruteforce_SedanSpot, EZVIZ_Mirai_bruteforce)
        print("NUGU\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(NUGU_Mirai_bruteforce_MIDAS, NUGU_Mirai_bruteforce_MIDASR, NUGU_Mirai_bruteforce_MIDASF, NUGU_Mirai_bruteforce_SedanSpot, NUGU_Mirai_bruteforce)
        print("Total\n" + "---------------------------------------------------------------------------")
        percentage_of_attack((EZVIZ_Mirai_bruteforce_MIDAS + NUGU_Mirai_bruteforce_MIDAS), (EZVIZ_Mirai_bruteforce_MIDASR + NUGU_Mirai_bruteforce_MIDASR),
                             (EZVIZ_Mirai_bruteforce_MIDASF + NUGU_Mirai_bruteforce_MIDASF), (EZVIZ_Mirai_bruteforce_SedanSpot + NUGU_Mirai_bruteforce_SedanSpot),
                             (EZVIZ_Mirai_bruteforce + NUGU_Mirai_bruteforce))
    if "OS" in Attacks[i]:
        print("\n\n\t\t\t\tOS Detection/Port Scan\n")
        print("EZVIZ\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(EZVIZ_PortOS_MIDAS, EZVIZ_PortOS_MIDASR, EZVIZ_PortOS_MIDASF, EZVIZ_PortOS_SedanSpot, EZVIZ_PortOS)
        print("NUGU\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(NUGU_PortOS_MIDAS, NUGU_PortOS_MIDASR, NUGU_PortOS_MIDASF,NUGU_PortOS_SedanSpot, NUGU_PortOS)
        print("Total\n" + "---------------------------------------------------------------------------")
        percentage_of_attack((EZVIZ_PortOS_MIDAS + NUGU_PortOS_MIDAS), (EZVIZ_PortOS_MIDASR + NUGU_PortOS_MIDASR),
                             (EZVIZ_PortOS_MIDASF + NUGU_PortOS_MIDASF), (EZVIZ_PortOS_SedanSpot + NUGU_PortOS_SedanSpot),
                             (EZVIZ_PortOS + NUGU_PortOS))

    if "Discovery" in Attacks[i]:
        print("\n\n\t\t\t\tHost Discovery/Port Scan\n")
        print("EZVIZ\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(EZVIZ_Hostport_MIDAS, EZVIZ_Hostport_MIDASR, EZVIZ_Hostport_MIDASF, EZVIZ_Hostport_SedanSpot, EZVIZ_Hostport)
        print("NUGU\n" + "---------------------------------------------------------------------------")
        percentage_of_attack(NUGU_Hostport_MIDAS, NUGU_Hostport_MIDASR, NUGU_Hostport_MIDASF,NUGU_Hostport_SedanSpot, NUGU_Hostport)
        print("Total\n" + "---------------------------------------------------------------------------")
        percentage_of_attack((EZVIZ_Hostport_MIDAS + NUGU_Hostport_MIDAS), (EZVIZ_Hostport_MIDASR + NUGU_Hostport_MIDASR),
                             (EZVIZ_Hostport_MIDASF + NUGU_Hostport_MIDASF), (EZVIZ_Hostport_SedanSpot + NUGU_Hostport_SedanSpot),
                             (EZVIZ_Hostport + NUGU_Hostport))
        

print("\n\n\n\t\t\t\tTotals per Device")
print("EZVIZ\n" + "---------------------------------------------------------------------------")
percentage_of_attack(EZVIZ_MIDAS_correct, EZVIZ_MIDASR_correct, EZVIZ_MIDASF_correct, EZVIZ_Sedan_correct, EZVIZ_counter)

print("NUGU\n" + "---------------------------------------------------------------------------")
percentage_of_attack(NUGU_MIDAS_correct, NUGU_MIDASR_correct, NUGU_MIDASF_correct, NUGU_Sedan_correct, NUGU_counter)



print("\n\n\n\t\t\t\tTotal Anomalies Captured")
print("\nMIDAS\n" + "---------------------------------------------------------------------------")
percentage_total(EZVIZ_MIDAS_correct, NUGU_MIDAS_correct, x, 1)
print("\nMIDASR\n" + "---------------------------------------------------------------------------")
percentage_total(EZVIZ_MIDASR_correct, NUGU_MIDASR_correct, x1, 1)
print("\nMIDASF\n" + "---------------------------------------------------------------------------")
percentage_total(EZVIZ_MIDASF_correct, NUGU_MIDASF_correct, x2, 1)
print("\nSedanSpot\n" + "---------------------------------------------------------------------------")
percentage_total(EZVIZ_Sedan_correct, NUGU_Sedan_correct, x3, 1)



print("\n\n\n\n\n\t\t\t\tTotal Benign Data")
print("\t\t\t\t(" + str(ben_counter) + " benign packets)")
print("\nMIDAS\n" + "---------------------------------------------------------------------------")
percentage_total(MIDAS_fn, 0, ben_counter, 2)
print("\nMIDASR\n" + "---------------------------------------------------------------------------")
percentage_total(MIDASR_fn, 0, ben_counter, 2)
print("\nMIDASF\n" + "---------------------------------------------------------------------------")
percentage_total(MIDASF_fn, 0, ben_counter, 2)
print("\nSedanSpot\n" + "---------------------------------------------------------------------------")
percentage_total(Sedan_fn, 0, ben_counter, 2)


MIDAS_tn = ben_counter - MIDAS_fn
MIDASR_tn = ben_counter - MIDASR_fn
MIDASF_tn = ben_counter - MIDASF_fn
Sedan_tn = ben_counter - Sedan_fn

print("\n\n\n\n\n\t\t\t\tTotal Data Percentages")
print("\nMIDAS\n" + "---------------------------------------------------------------------------")
percentage_total(MIDAS_tn, (NUGU_MIDAS_correct + EZVIZ_MIDAS_correct), counter, 3)
print("\nMIDASR\n" + "---------------------------------------------------------------------------")
percentage_total(MIDASR_tn, (NUGU_MIDASR_correct + EZVIZ_MIDASR_correct), counter, 3)
print("\nMIDASF\n" + "---------------------------------------------------------------------------")
percentage_total(MIDASF_tn, (NUGU_MIDASF_correct + EZVIZ_MIDASF_correct), counter, 3)
print("\nSedanSpot\n" + "---------------------------------------------------------------------------")
percentage_total(Sedan_tn, (NUGU_Sedan_correct + EZVIZ_Sedan_correct), counter, 3)

f.close