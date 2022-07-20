import csv
import subprocess as sp

filename = "/home/kali/Research/results/Attack_Approach_UNSW.csv"

import sys
f = open("test_UNSW.out", 'w')
sys.stdout = f

array = []
MIDAS_fn, MIDASR_fn, MIDASF_fn, Sedan_fn = (0,0,0,0)

column_names = ['', 'Reconnaissance', 'Exploits', 'DoS', 'Generic', 'Shellcode',
' Fuzzers', 'Worms', 'Backdoors', 'Analysis', ' Reconnaissance ',
'Backdoor', ' Fuzzers ', ' Shellcode ']



counter, MIDAS_correct, MIDASR_correct,MIDASF_correct, Sedan_correct = (0,0,0,0,0)
recon_counter, recon_MIDAS_correct, recon_MIDASR_correct,recon_MIDASF_correct, recon_Sedan_correct = (0,0,0,0,0)
DoS_MIDAS, DoS_MIDASF, DoS_MIDASR, DoS_SedanSpot, DoS  = (0,0,0,0,0)
Generic_MIDAS, Generic_MIDASF, Generic_MIDASR, Generic_SedanSpot, Generic  = (0,0,0,0,0)
Shellcode_MIDAS, Shellcode_MIDASF, Shellcode_MIDASR, Shellcode_SedanSpot, Shellcode  = (0,0,0,0,0)
Fuzzers_MIDAS, Fuzzers_MIDASF, Fuzzers_MIDASR, Fuzzers_SedanSpot, Fuzzers  = (0,0,0,0,0)
Worms_MIDAS, Worms_MIDASF, Worms_MIDASR, Worms_SedanSpot, Worms  = (0,0,0,0,0)
Backdoors_MIDAS, Backdoors_MIDASF, Backdoors_MIDASR, Backdoors_SedanSpot, Backdoors  = (0,0,0,0,0)
Analysis_MIDAS, Analysis_MIDASF, Analysis_MIDASR, Analysis_SedanSpot, Analysis  = (0,0,0,0,0)
Exploits_MIDAS, Exploits_MIDASF, Exploits_MIDASR, Exploits_SedanSpot, Exploits  = (0,0,0,0,0)

ben_counter, anom_count = (0,0)

x, x1, x2, x3 = (0,0,0,0)


with open(filename, newline='', encoding='latin1') as rows:
    row_reader = csv.DictReader(rows, delimiter=',')
    for row in row_reader:
        counter += 1
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
            #print(str(value))
        else:
            print(row['Attack'])

for i in range(0, len(array)):

    if array[i][0] < 1:
        ben_counter += 1
        if (array[i][1] == 1):
            MIDAS_fn += 1
        if (array[i][2] == 1):
            MIDASR_fn += 1
        if (array[i][3] == 1):
            MIDASF_fn += 1
        if (array[i][4] == 1):
            Sedan_fn += 1

    elif array[i][0] >= 1:
        if array[i][0] == 1 or array[i][0] == 10:
            recon_counter += 1
            anom_count += 1
            if (array[i][1] == 1):
                recon_MIDAS_correct += 1
            if (array[i][2] == 1):
                recon_MIDASR_correct += 1
            if (array[i][3] == 1):
                recon_MIDASF_correct += 1
            if (array[i][4] == 1):
                recon_Sedan_correct += 1

        if array[i][0] == 2:
            Exploits += 1
            anom_count += 1
            if (array[i][1] == 1):
                Exploits_MIDAS += 1
            if (array[i][2] == 1):
                Exploits_MIDASR += 1
            if (array[i][3] == 1):
                Exploits_MIDASF += 1
            if (array[i][4] == 1):
                Exploits_SedanSpot += 1

        if array[i][0] == 3:
            DoS += 1
            anom_count += 1
            if (array[i][1] == 1):
                DoS_MIDAS += 1
            if (array[i][2] == 1):
                DoS_MIDASR += 1
            if (array[i][3] == 1):
                DoS_MIDASF += 1
            if (array[i][4] == 1):
                DoS_SedanSpot += 1

        if array[i][0] == 4:
            Generic += 1
            anom_count += 1
            if (array[i][1] == 1):
                Generic_MIDAS += 1
            if (array[i][2] == 1):
               Generic_MIDASR += 1
            if (array[i][3] == 1):
                Generic_MIDASF += 1
            if (array[i][4] == 1):
                Generic_SedanSpot += 1

        if array[i][0] == 5 or array[i][0] == 13:
            Shellcode += 1
            anom_count += 1
            if (array[i][1] == 1):
                Shellcode_MIDAS += 1
            if (array[i][2] == 1):
                Shellcode_MIDASR += 1
            if (array[i][3] == 1):
                Shellcode_MIDASF += 1
            if (array[i][4] == 1):
                Shellcode_SedanSpot += 1

        if array[i][0] == 6 or array[i][0] == 12:
            Fuzzers += 1
            anom_count += 1
            if (array[i][1] == 1):
                Fuzzers_MIDAS += 1
            if (array[i][2] == 1):
                Fuzzers_MIDASR += 1
            if (array[i][3] == 1):
                Fuzzers_MIDASF += 1
            if (array[i][4] == 1):
                Fuzzers_SedanSpot += 1

        if array[i][0] == 7:
            Worms += 1
            anom_count += 1
            if (array[i][1] == 1):
                Worms_MIDAS += 1
            if (array[i][2] == 1):
                Worms_MIDASR += 1
            if (array[i][3] == 1):
                Worms_MIDASF += 1
            if (array[i][4] == 1):
                Worms_SedanSpot += 1

        if array[i][0] == 8 or array[i][0] == 11:
            Backdoors += 1
            anom_count += 1
            if (array[i][1] == 1):
                Backdoors_MIDAS += 1
            if (array[i][2] == 1):
                Backdoors_MIDASR += 1
            if (array[i][3] == 1):
                Backdoors_MIDASF += 1
            if (array[i][4] == 1):
                Backdoors_SedanSpot += 1

        if array[i][0] == 9:
            Analysis += 1
            anom_count += 1
            if (array[i][1] == 1):
                Analysis_MIDAS += 1
            if (array[i][2] == 1):
                Analysis_MIDASR += 1
            if (array[i][3] == 1):
                Analysis_MIDASF += 1
            if (array[i][4] == 1):
                Analysis_SedanSpot += 1

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
        print("Total: " + str(N_percent) + "% of the data are correctly classified with " + str(
            (TC)) + " correctly classified packets out of the " + str(
            T) + " total packets")


Attacks = ["Denial of Service", "Backdoor", "Worm", "Reconnaissance", "Exploits", "Fuzzers", "Generic", "Shellcode", "Analysis"]

for i in range(0, len(Attacks)):
    if "Denial" in Attacks[i]:
        print("\n\n\t\t\t\tDenial of Service\n")
        print("---------------------------------------------------------------------------")
        percentage_of_attack(DoS_MIDAS, DoS_MIDASR, DoS_MIDASF, DoS_SedanSpot, DoS)
    if "Backdoor" in Attacks[i]:
        print("\n\n\t\t\t\tBackdoor\n")
        print("---------------------------------------------------------------------------")
        percentage_of_attack(Backdoors_MIDAS, Backdoors_MIDASR, Backdoors_MIDASF, Backdoors_SedanSpot, Backdoors)
    if "Worm" in Attacks[i]:
        print("\n\n\t\t\t\tWorms\n")
        print("---------------------------------------------------------------------------")
        percentage_of_attack(Worms_MIDAS, Worms_MIDASR, Worms_MIDASF,
                             Worms_SedanSpot, Worms)
    if "Reconnaissance" in Attacks[i]:
        print("\n\n\t\t\t\tRecon\n")
        print("---------------------------------------------------------------------------")
        percentage_of_attack(recon_MIDAS_correct, recon_MIDASR_correct, recon_MIDASF_correct,
                             recon_Sedan_correct, recon_counter)
    if "Exploits" in Attacks[i]:
        print("\n\n\t\t\t\tExploits\n")
        print("---------------------------------------------------------------------------")
        percentage_of_attack(Exploits_MIDAS, Exploits_MIDASR, Exploits_MIDASF,
                             Exploits_SedanSpot, Exploits)

    if "Fuzzers" in Attacks[i]:
        print("\n\n\t\t\t\tFuzzers\n")
        print("---------------------------------------------------------------------------")
        percentage_of_attack(Fuzzers_MIDAS, Fuzzers_MIDASR, Fuzzers_MIDASF,
                             Fuzzers_SedanSpot, Fuzzers)
    if "Generic" in Attacks[i]:
        print("\n\n\t\t\t\tGeneric\n")
        print("---------------------------------------------------------------------------")
        percentage_of_attack(Generic_MIDAS, Generic_MIDASR, Generic_MIDASF, Generic_SedanSpot, Generic)

    if "Shellcode" in Attacks[i]:
        print("\n\n\t\t\t\tShellcode\n")
        print("---------------------------------------------------------------------------")
        percentage_of_attack(Shellcode_MIDAS, Shellcode_MIDASR, Shellcode_MIDASF,Shellcode_SedanSpot, Shellcode)

    if "Analysis" in Attacks[i]:
        print("\n\n\t\t\t\tAnalysis\n")
        print("---------------------------------------------------------------------------")
        percentage_of_attack(Analysis_MIDAS, Analysis_MIDASR, Analysis_MIDASF,Analysis_SedanSpot, Analysis)




MIDAS_correct = Shellcode_MIDAS + Generic_MIDAS + Fuzzers_MIDAS + DoS_MIDAS + recon_MIDAS_correct + Exploits_MIDAS + Worms_MIDAS + Backdoors_MIDAS
MIDASF_correct = Shellcode_MIDASF + Generic_MIDASF + Fuzzers_MIDASF + DoS_MIDASF + recon_MIDASF_correct + Exploits_MIDASF + Worms_MIDASF + Backdoors_MIDASF
MIDASR_correct = Shellcode_MIDASR + Generic_MIDASR + Fuzzers_MIDASR + DoS_MIDASR + recon_MIDASR_correct + Exploits_MIDASR + Worms_MIDASR + Backdoors_MIDASR
Sedan_correct = Shellcode_SedanSpot + Generic_SedanSpot + Fuzzers_SedanSpot + DoS_SedanSpot + recon_Sedan_correct + Exploits_SedanSpot + Worms_SedanSpot + Backdoors_SedanSpot

print("\n\n\n\t\t\t\tTotals per Device")
print("---------------------------------------------------------------------------")
percentage_of_attack(MIDAS_correct, MIDASR_correct, MIDASF_correct, Sedan_correct, anom_count)


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
percentage_total(MIDAS_tn, (MIDAS_correct), counter, 3)
print("\nMIDASR\n" + "---------------------------------------------------------------------------")
percentage_total(MIDASR_tn, (MIDASR_correct), counter, 3)
print("\nMIDASF\n" + "---------------------------------------------------------------------------")
percentage_total(MIDASF_tn, (MIDASF_correct), counter, 3)
print("\nSedanSpot\n" + "---------------------------------------------------------------------------")
percentage_total(Sedan_tn, (Sedan_correct), counter, 3)

f.close