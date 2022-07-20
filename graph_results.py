import csv
import subprocess as sp

import numpy as np

csvData = ""
file = ""
time_table = []
time_set = []
M_tab = []
S_tab = []
R_tab = []
F_tab = []



from pandas import read_csv, concat

data = read_csv("/home/kali/Research/data/MIDAS_test/UNSW_NB15_times.csv", header=0, names=['Stime'], dtype='category')
data.Stime = data.Stime.cat.codes + 1
data.Stime.to_csv("/home/kali/Research/CsvToG/times.csv")





print(time_table)
c1 = 0
c2 = 0
c3 = 0
c4 = 0




counter = 0
with open("/home/kali/Research/CsvToG/times.csv", newline='', encoding='latin1') as rows:
    for row in rows:
        if counter == 0:
            assert True
            counter += 1
        else:
            time_table.append(int(row[row.find(",")+1: ].strip()))


f1 = "/home/kali/Research/MIDAS/graphs/MIDAS.txt"

counter = 0
with open(f1, newline='', encoding='latin1') as rows:
    for row in rows:
        value = float(row.strip())
        M_tab.append(float(row.strip()))
        counter += 1


f2 = "/home/kali/Research/MIDAS/graphs/MIDASR.txt"

counter = 0
with open(f2, newline='', encoding='latin1') as rows:
    for row in rows:
        R_tab.append(float(row.strip()))
        counter += 1

f3 = "/home/kali/Research/MIDAS/graphs/MIDASF.txt"

counter = 0
with open(f3, newline='', encoding='latin1') as rows:
    for row in rows:
        F_tab.append(float(row.strip()))
        counter += 1

f4 = "/home/kali/Research/MIDAS/graphs/SedanSpot.txt"

counter = 0
with open(f4, newline='', encoding='latin1') as rows:
    for row in rows:
        S_tab.append(float(row.strip()))
        counter += 1


#print(time_table)

import matplotlib.pyplot as plt


x1 = np.array(M_tab)
x1_max = max(x1)
x1_new = [x / x1_max for x in x1]



x2 = np.array(R_tab)
x2_max = max(x2)
x2_new = [x / x2_max for x in x2]


x3 = np.array(F_tab)
x3_max = max(x3)
x3_new = [x / x3_max for x in x3]


x4 = np.array(S_tab)
x4_max = max(x1)
x4_new = [x / x4_max for x in x4]


x_axis = np.array(time_table)

#print(x)
plt.plot(x_axis,x1_new)
#plt.plot(x_axis,x2_new)
#plt.plot(x_axis,x3_new)
#plt.plot(x_axis,x4_new)
plt.show()

plt.plot(x_axis,x2_new)
plt.show()


plt.plot(x_axis,x3_new)
plt.show()

plt.plot(x_axis,x4_new)
plt.show()