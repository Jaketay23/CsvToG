import csv
import pandas as pd


prefix = ""
f1 = ""
f2 = ""
f3 = ""
f4 = ""
out = ""
count = 0
run_count = 0

#HCRL
#output = open("/home/kali/Research/results/Attack_Approach2.csv", "w")
#getAttackInfo = "/home/kali/Research/dataset_copy/Processed/HCRL_full_AttackInfo.csv"

#UNSW
# output = open("/home/kali/Research/results/Attack_Approach_UNSW.csv", "w")
# getAttackInfo = "/home/kali/Research/data/MIDAS_test/UNSW_NB15.csv"

#DARPA
output = open("/home/kali/Research/results/Attack_Approach_DARPA.csv", "w")
getAttackInfo = "/home/kali/Research/MIDAS/data/DARPA/darpa_full.csv"

# assign dataset
# csvData = pd.read_csv(getAttackInfo, usecols=['Source', 'Destination', 'Time', 'Label', 'Attack'],
#                                        low_memory=False)
# # sort data frame
# csvData.sort_values(["Time"],
#                     axis=0,
#                     ascending=[True],
#                     inplace=True)
#
# csvData.to_csv(getAttackInfo)


while (run_count == 0):

    test = input("Enter Test #: ")

    if (int(test) == 1):
        prefix = "/home/kali/Research/results/1DoS_Epoch/"
        f1 = prefix + "MIDAS.txt"
        f2 = prefix + "MIDASR.txt"
        f3 = prefix + "MIDASF.txt"
        f4 = prefix + "SedanSpot.txt"
        out_prefix = "/home/kali/Research/results/Comparisons/1DoS_Epoch/"
        all_anoms = out_prefix + "All_Anomalies.txt"
        false_positives = out_prefix + "False_Postives"
        false_negatives = out_prefix + "False_Negatives"

    elif (int(test) == 2):
        prefix = "/home/kali/Research/results/1DoS_1Mirai_Epoch/"
        f1 = prefix + "MIDAS.txt"
        f2 = prefix + "MIDASR.txt"
        f3 = prefix + "MIDASF.txt"
        f4 = prefix + "SedanSpot.txt"
        out_prefix = "/home/kali/Research/results/Comparisons/1DoS_1Mirai_Epoch/"
        all_anoms = out_prefix + "All_Anomalies.txt"
        false_positives = out_prefix + "False_Postives"
        false_negatives = out_prefix + "False_Negatives"

    elif (int(test) == 3):
        prefix = "/home/kali/Research/results/1Mirai_Epoch/"
        f1 = prefix + "MIDAS.txt"
        f2 = prefix + "MIDASR.txt"
        f3 = prefix + "MIDASF.txt"
        f4 = prefix + "SedanSpot.txt"
        out_prefix = "/home/kali/Research/results/Comparisons/1Mirai_Epoch/"
        all_anoms = out_prefix + "All_Anomalies.txt"
        false_positives = out_prefix + "False_Postives"
        false_negatives = out_prefix + "False_Negatives"

    elif (int(test) == 4):
        prefix = "/home/kali/Research/results/2DoS_Epoch/"
        f1 = prefix + "MIDAS.txt"
        f2 = prefix + "MIDASR.txt"
        f3 = prefix + "MIDASF.txt"
        f4 = prefix + "SedanSpot.txt"
        out_prefix = "/home/kali/Research/results/Comparisons/2DoS_Epoch/"
        all_anoms = out_prefix + "All_Anomalies.txt"
        false_positives = out_prefix + "False_Postives"
        false_negatives = out_prefix + "False_Negatives"

    elif (int(test) == 5):
        prefix = "/home/kali/Research/results/2Mirai_Epoch/"
        f1 = prefix + "MIDAS.txt"
        f2 = prefix + "MIDASR.txt"
        f3 = prefix + "MIDASF.txt"
        f4 = prefix + "SedanSpot.txt"
        out_prefix = "/home/kali/Research/results/Comparisons/2Mirai_Epoch/"
        all_anoms = out_prefix + "All_Anomalies.txt"
        false_positives = out_prefix + "False_Postives"
        false_negatives = out_prefix + "False_Negatives"


    elif (int(test) == 6):
        prefix = "/home/kali/Research/results/DARPA/"
        f1 = prefix + "MIDAS.txt"
        f2 = prefix + "MIDASR.txt"
        f3 = prefix + "MIDASF.txt"
        f4 = prefix + "SedanSpot.txt"
        out_prefix = "/home/kali/Research/results/Comparisons/DARPA/"
        all_anoms = out_prefix + "All_Anomalies.txt"
        false_positives = out_prefix + "False_Postives"
        false_negatives = out_prefix + "False_Negatives"

    elif (int(test) == 8):
        prefix = "/home/kali/Research/results/full_1sec/"
        f1 = prefix + "MIDAS.txt"
        f2 = prefix + "MIDASR.txt"
        f3 = prefix + "MIDASF.txt"
        f4 = prefix + "SedanSpot.txt"
        out_prefix = "/home/kali/Research/results/Comparisons/"
        all_anoms = out_prefix + "All_Anomalies.txt"
        false_positives = out_prefix + "False_Postives"
        false_negatives = out_prefix + "False_Negatives"


    elif (int(test) == 7):
        prefix = "/home/kali/Research/results/UNSW_seconds/"
        f1 = prefix + "MIDAS.txt"
        f2 = prefix + "MIDASR.txt"
        f3 = prefix + "MIDASF.txt"
        f4 = prefix + "SedanSpot.txt"
        out_prefix = "/home/kali/Research/results/Comparisons/UNSW_seconds/"
        all_anoms = out_prefix + "All_Anomalies.txt"
        false_positives = out_prefix + "False_Postives"
        false_negatives = out_prefix + "False_Negatives"

    else:
        output.close()
        quit()




    r1 = open(f1, "r")
    r2 = open(f2, "r")
    r3 = open(f3, "r")
    r4 = open(f4, "r")
    attack_table = []
    ground_table = []
    all = open(all_anoms, "w")
    fp = open(false_positives, "w")
    fn = open(false_negatives, "w")

    with open(f1, 'r') as f:
        for count, line in enumerate(f):
            pass
    print('Total Lines', count + 1)

    N = 0
    R = 0
    F = 0
    S = 0

    gtd_list = []
    with open(getAttackInfo, newline='', encoding='latin1') as rows:
        row_reader = csv.DictReader(rows, delimiter=',')
        num_records = 0
        counter = 0
        for row in row_reader:
            gtd_list.append(dict(row))
            num_records += 1

            #ground = row["Label"] #HCRL/UNSW
            #info = row["Attack"] #HCRL
            #info = row["attack_cat"] #UNSW
            info = row['Label']
            MIDAS = "0"
            MIDASF = "0"
            MIDASR = "0"
            SEDAN = "0"

            attack_table.append(info)
            #ground_table.append(ground)
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    res = []
    for q in attack_table:
        if q not in res:
            res.append(q)
    print(res)
    print(len(attack_table))
    #output.write("Attack,Ground,MIDAS,MIDASR,MIDASF,SedanSpot\n") #UNSW
    output.write("Attack,MIDAS,MIDASR,MIDASF,SedanSpot\n") #DARPA
    for i in range(0, count):
        r1_line = r1.readline().strip()
        r2_line = r2.readline().strip()
        r3_line = r3.readline().strip()
        r4_line = r4.readline().strip()


        #output.write(attack_table[i] + "," +  ground_table[i] + "," +  r1_line[-1] + "," + r2_line[-1] + "," +  r3_line[-1] + "," + r4_line[-1] + "\n")
        output.write(
            attack_table[i] + "," + r1_line[-1] + "," + r2_line[-1] + "," + r3_line[-1] + "," +
            r4_line[-1] + "\n")
        #print(attack_table[i] + "," +  r1_line[-1] + "," + r2_line[-1] + "," +  r3_line[-1] + "," + r4_line[-1])

        if (r1_line[-1] == "1"):
            #print(r1_line[r1_line.find("(") + 1:r1_line.find(")") - 1])
            c1 += 1
            #attack_table[int(r1_line[r1_line.find("(") + 1:r1_line.find(")") - 1])-1][2] = "1"

        if (r2_line[-1] == "1"):
            #print(r1_line[r1_line.find("(") + 1:r1_line.find(")") - 1])
            c2 += 1
           # attack_table[int(r2_line[r2_line.find("(") + 1:r2_line.find(")") - 1])-1][3] = "1"

        if (r3_line[-1] == "1"):
            c3 += 1
            #print(r1_line[r1_line.find("(") + 1:r1_line.find(")") - 1])
            # attack_table[int(r3_line[r3_line.find("(") + 1:r3_line.find(")") - 1])-1][4] = "1"

        if (r4_line[-1] == "1"):
            c4 += 1
            #print(r4_line[r4_line.find("(") + 1:r4_line.find(")") - 1])
            # attack_table[int(r4_line[r4_line.find("(") + 1:r4_line.find(")") - 1])-1][5] = "1"


        #Catch All Anomalous Entries
        if (r1_line[-3] == "1"):
                all.write("MIDAS: " + r1_line + " MIDAS-R: " + r2_line + " MIDAS-F: " + r3_line + " SedanSpot: " + r4_line)
                #all.write(attack_table[int()])
                all.write("\n")

        # Catch All False Positives
        if (r1_line[-3] == "1"):
            if(r1_line[-1] == "0" or r2_line[-1] == "0" or r3_line[-1] == "0" or r4_line[-1] == "0"):
                fp.write("MIDAS: " + r1_line + " MIDAS-R: " + r2_line + " MIDAS-F: " + r3_line + " SedanSpot: " + r4_line)
                fp.write("\n")

        # Catch All False Negatives
        if (r1_line[-3] == "0"):
            if (r1_line[-1] == "1" or r2_line[-1] == "1" or r3_line[-1] == "1" or r4_line[-1] == "1"):
                fn.write("MIDAS: " + r1_line + " MIDAS-R: " + r2_line + " MIDAS-F: " + r3_line + " SedanSpot: " + r4_line)
                fn.write("\n")


    all.close()
    print(str(c1))
    print(str(c2))
    print(str(c3))
    print(str(c4))
    fp.close()
    fn.close()