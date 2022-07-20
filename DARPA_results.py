import csv
import subprocess as sp

filename = "/home/kali/Research/results/Attack_Approach_DARPA.csv"

import sys
f = open("test_DARPA.out", 'w')
sys.stdout = f

array = []
MIDAS_fn, MIDASR_fn, MIDASF_fn, Sedan_fn = (0,0,0,0)
counter, ben_counter = (0,0)

MIDAS_1, MIDASR_1, MIDASF_1, Sedan_1, count_1 = (0,0,0,0,0)
MIDAS_2, MIDASR_2, MIDASF_2, Sedan_2, count_2 = (0,0,0,0,0)
MIDAS_4, MIDASR_4, MIDASF_4, Sedan_4, count_4 = (0,0,0,0,0)
MIDAS_3, MIDASR_3, MIDASF_3, Sedan_3, count_3 = (0,0,0,0,0)
MIDAS_5, MIDASR_5, MIDASF_5, Sedan_5, count_5 = (0,0,0,0,0)
MIDAS_6, MIDASR_6, MIDASF_6, Sedan_6, count_6 = (0,0,0,0,0)
MIDAS_7, MIDASR_7, MIDASF_7, Sedan_7, count_7 = (0,0,0,0,0)
MIDAS_8, MIDASR_8, MIDASF_8, Sedan_8, count_8 = (0,0,0,0,0)
MIDAS_9, MIDASR_9, MIDASF_9, Sedan_9, count_9 = (0,0,0,0,0)
MIDAS_10, MIDASR_10, MIDASF_10, Sedan_10, count_10 = (0,0,0,0,0)
MIDAS_11, MIDASR_11, MIDASF_11, Sedan_11, count_11 = (0,0,0,0,0)
MIDAS_12, MIDASR_12, MIDASF_12, Sedan_12, count_12 = (0,0,0,0,0)
MIDAS_13, MIDASR_13, MIDASF_13, Sedan_13, count_13 = (0,0,0,0,0)
MIDAS_14, MIDASR_14, MIDASF_14, Sedan_14, count_14 = (0,0,0,0,0)
MIDAS_15, MIDASR_15, MIDASF_15, Sedan_15, count_15 = (0,0,0,0,0)
MIDAS_16, MIDASR_16, MIDASF_16, Sedan_16, count_16 = (0,0,0,0,0)
MIDAS_17, MIDASR_17, MIDASF_17, Sedan_17, count_17 = (0,0,0,0,0)
MIDAS_18, MIDASR_18, MIDASF_18, Sedan_18, count_18 = (0,0,0,0,0)
MIDAS_19, MIDASR_19, MIDASF_19, Sedan_19, count_19 = (0,0,0,0,0)
MIDAS_20, MIDASR_20, MIDASF_20, Sedan_20, count_20 = (0,0,0,0,0)
MIDAS_21, MIDASR_21, MIDASF_21, Sedan_21, count_21 = (0,0,0,0,0)
MIDAS_22, MIDASR_22, MIDASF_22, Sedan_22, count_22 = (0,0,0,0,0)
MIDAS_23, MIDASR_23, MIDASF_23, Sedan_23, count_23 = (0,0,0,0,0)
MIDAS_24, MIDASR_24, MIDASF_24, Sedan_24, count_24 = (0,0,0,0,0)
MIDAS_25, MIDASR_25, MIDASF_25, Sedan_25, count_25 = (0,0,0,0,0)
MIDAS_26, MIDASR_26, MIDASF_26, Sedan_26, count_26 = (0,0,0,0,0)
MIDAS_27, MIDASR_27, MIDASF_27, Sedan_27, count_27 = (0,0,0,0,0)
MIDAS_28, MIDASR_28, MIDASF_28, Sedan_28, count_28 = (0,0,0,0,0)
MIDAS_29, MIDASR_29, MIDASF_29, Sedan_29, count_29 = (0,0,0,0,0)
MIDAS_30, MIDASR_30, MIDASF_30, Sedan_30, count_30 = (0,0,0,0,0)
MIDAS_31, MIDASR_31, MIDASF_31, Sedan_31, count_31 = (0,0,0,0,0)
MIDAS_32, MIDASR_32, MIDASF_32, Sedan_32, count_32 = (0,0,0,0,0)
MIDAS_33, MIDASR_33, MIDASF_33, Sedan_33, count_33 = (0,0,0,0,0)
MIDAS_34, MIDASR_34, MIDASF_34, Sedan_34, count_34 = (0,0,0,0,0)
MIDAS_35, MIDASR_35, MIDASF_35, Sedan_35, count_35 = (0,0,0,0,0)
MIDAS_36, MIDASR_36, MIDASF_36, Sedan_36, count_36 = (0,0,0,0,0)
MIDAS_37, MIDASR_37, MIDASF_37, Sedan_37, count_37 = (0,0,0,0,0)
MIDAS_38, MIDASR_38, MIDASF_38, Sedan_38, count_38 = (0,0,0,0,0)
MIDAS_39, MIDASR_39, MIDASF_39, Sedan_39, count_39 = (0,0,0,0,0)
MIDAS_40, MIDASR_40, MIDASF_40, Sedan_40, count_40 = (0,0,0,0,0)
MIDAS_41, MIDASR_41, MIDASF_41, Sedan_41, count_41 = (0,0,0,0,0)
MIDAS_42, MIDASR_42, MIDASF_42, Sedan_42, count_42 = (0,0,0,0,0)
MIDAS_43, MIDASR_43, MIDASF_43, Sedan_43, count_43 = (0,0,0,0,0)
MIDAS_44, MIDASR_44, MIDASF_44, Sedan_44, count_44 = (0,0,0,0,0)
MIDAS_45, MIDASR_45, MIDASF_45, Sedan_45, count_45 = (0,0,0,0,0)
MIDAS_46, MIDASR_46, MIDASF_46, Sedan_46, count_46 = (0,0,0,0,0)
MIDAS_47, MIDASR_47, MIDASF_47, Sedan_47, count_47 = (0,0,0,0,0)
MIDAS_48, MIDASR_48, MIDASF_48, Sedan_48, count_48 = (0,0,0,0,0)
MIDAS_49, MIDASR_49, MIDASF_49, Sedan_49, count_49 = (0,0,0,0,0)
MIDAS_50, MIDASR_50, MIDASF_50, Sedan_50, count_50 = (0,0,0,0,0)
MIDAS_51, MIDASR_51, MIDASF_51, Sedan_51, count_51 = (0,0,0,0,0)
MIDAS_52, MIDASR_52, MIDASF_52, Sedan_52, count_52 = (0,0,0,0,0)
MIDAS_53, MIDASR_53, MIDASF_53, Sedan_53, count_53 = (0,0,0,0,0)
MIDAS_54, MIDASR_54, MIDASF_54, Sedan_54, count_54 = (0,0,0,0,0)
MIDAS_55, MIDASR_55, MIDASF_55, Sedan_55, count_55 = (0,0,0,0,0)
MIDAS_56, MIDASR_56, MIDASF_56, Sedan_56, count_56 = (0,0,0,0,0)
MIDAS_57, MIDASR_57, MIDASF_57, Sedan_57, count_57 = (0,0,0,0,0)
MIDAS_58, MIDASR_58, MIDASF_58, Sedan_58, count_58 = (0,0,0,0,0)
MIDAS_59, MIDASR_59, MIDASF_59, Sedan_59, count_59 = (0,0,0,0,0)
MIDAS_60, MIDASR_60, MIDASF_60, Sedan_60, count_60 = (0,0,0,0,0)
MIDAS_61, MIDASR_61, MIDASF_61, Sedan_61, count_61 = (0,0,0,0,0)
MIDAS_62, MIDASR_62, MIDASF_62, Sedan_62, count_62 = (0,0,0,0,0)
MIDAS_63, MIDASR_63, MIDASF_63, Sedan_63, count_63 = (0,0,0,0,0)
MIDAS_64, MIDASR_64, MIDASF_64, Sedan_64, count_64 = (0,0,0,0,0)
MIDAS_65, MIDASR_65, MIDASF_65, Sedan_65, count_65 = (0,0,0,0,0)
MIDAS_66, MIDASR_66, MIDASF_66, Sedan_66, count_66 = (0,0,0,0,0)
MIDAS_67, MIDASR_67, MIDASF_67, Sedan_67, count_67 = (0,0,0,0,0)
MIDAS_68, MIDASR_68, MIDASF_68, Sedan_68, count_68 = (0,0,0,0,0)
MIDAS_69, MIDASR_69, MIDASF_69, Sedan_69, count_69 = (0,0,0,0,0)
MIDAS_70, MIDASR_70, MIDASF_70, Sedan_70, count_70 = (0,0,0,0,0)
MIDAS_71, MIDASR_71, MIDASF_71, Sedan_71, count_71 = (0,0,0,0,0)
MIDAS_72, MIDASR_72, MIDASF_72, Sedan_72, count_72 = (0,0,0,0,0)
MIDAS_73, MIDASR_73, MIDASF_73, Sedan_73, count_73 = (0,0,0,0,0)
MIDAS_74, MIDASR_74, MIDASF_74, Sedan_74, count_74 = (0,0,0,0,0)
MIDAS_75, MIDASR_75, MIDASF_75, Sedan_75, count_75 = (0,0,0,0,0)
MIDAS_76, MIDASR_76, MIDASF_76, Sedan_76, count_76 = (0,0,0,0,0)
MIDAS_77, MIDASR_77, MIDASF_77, Sedan_77, count_77 = (0,0,0,0,0)
MIDAS_78, MIDASR_78, MIDASF_78, Sedan_78, count_78 = (0,0,0,0,0)
MIDAS_79, MIDASR_79, MIDASF_79, Sedan_79, count_79 = (0,0,0,0,0)
MIDAS_80, MIDASR_80, MIDASF_80, Sedan_80, count_80 = (0,0,0,0,0)
MIDAS_81, MIDASR_81, MIDASF_81, Sedan_81, count_81 = (0,0,0,0,0)
MIDAS_82, MIDASR_82, MIDASF_82, Sedan_82, count_82 = (0,0,0,0,0)
MIDAS_83, MIDASR_83, MIDASF_83, Sedan_83, count_83 = (0,0,0,0,0)
MIDAS_84, MIDASR_84, MIDASF_84, Sedan_84, count_84 = (0,0,0,0,0)
MIDAS_85, MIDASR_85, MIDASF_85, Sedan_85, count_85 = (0,0,0,0,0)
MIDAS_86, MIDASR_86, MIDASF_86, Sedan_86, count_86 = (0,0,0,0,0)
MIDAS_87, MIDASR_87, MIDASF_87, Sedan_87, count_87 = (0,0,0,0,0)
MIDAS_88, MIDASR_88, MIDASF_88, Sedan_88, count_88 = (0,0,0,0,0)
MIDAS_89, MIDASR_89, MIDASF_89, Sedan_89, count_89 = (0,0,0,0,0)
anom_count = 0

DOS_MIDAS, DOS_MIDASR, DOS_MIDASF, DOS_SEDAN, DOS = (0,0,0,0,0)
PROBE_MIDAS, PROBE_MIDASR, PROBE_MIDASF, PROBE_SEDAN, PROBE = (0,0,0,0,0)
U2R_MIDAS, U2R_MIDASR, U2R_MIDASF, U2R_SEDAN, U2R = (0,0,0,0,0)
R2L_MIDAS, R2L_MIDASR, R2L_MIDASF, R2L_SEDAN, R2L = (0,0,0,0,0)
MISC_MIDAS, MISC_MIDASR, MISC_MIDASF, MISC_SEDAN, MISC = (0,0,0,0,0)

dos_array = [DOS_MIDAS, DOS_MIDASR, DOS_MIDASF, DOS_SEDAN, DOS]
probe_array = [PROBE_MIDAS, PROBE_MIDASR, PROBE_MIDASF, PROBE_SEDAN, PROBE]
u2r_array = [U2R_MIDAS, U2R_MIDASR, U2R_MIDASF, U2R_SEDAN, U2R]
r2l_array = [R2L_MIDAS, R2L_MIDASR, R2L_MIDASF, R2L_SEDAN, R2L]
misc_array = [MISC_MIDAS, MISC_MIDASR, MISC_MIDASF, MISC_SEDAN, MISC]



midas_array = [MIDAS_1, MIDAS_2, MIDAS_3, MIDAS_4, MIDAS_5, MIDAS_6, MIDAS_7, MIDAS_8, MIDAS_9, MIDAS_10, MIDAS_11, MIDAS_12, MIDAS_13, MIDAS_14, MIDAS_15, MIDAS_16, MIDAS_17, MIDAS_18, MIDAS_19, MIDAS_20, MIDAS_21, MIDAS_22, MIDAS_23, MIDAS_24, MIDAS_25, MIDAS_26, MIDAS_27, MIDAS_28, MIDAS_29, MIDAS_30, MIDAS_31, MIDAS_32, MIDAS_33, MIDAS_34, MIDAS_35, MIDAS_36, MIDAS_37, MIDAS_38, MIDAS_39, MIDAS_40, MIDAS_41, MIDAS_42, MIDAS_43, MIDAS_44, MIDAS_45, MIDAS_46, MIDAS_47, MIDAS_48, MIDAS_49, MIDAS_50, MIDAS_51, MIDAS_52, MIDAS_53, MIDAS_54, MIDAS_55, MIDAS_56, MIDAS_57, MIDAS_58, MIDAS_59, MIDAS_60, MIDAS_61, MIDAS_62, MIDAS_63, MIDAS_64, MIDAS_65, MIDAS_66, MIDAS_67, MIDAS_68, MIDAS_69, MIDAS_70, MIDAS_71, MIDAS_72, MIDAS_73, MIDAS_74, MIDAS_75, MIDAS_76, MIDAS_77, MIDAS_78, MIDAS_79, MIDAS_80, MIDAS_81, MIDAS_82, MIDAS_83, MIDAS_84, MIDAS_85, MIDAS_86, MIDAS_87, MIDAS_88, MIDAS_89]


midasr_array = [MIDASR_1, MIDASR_2, MIDASR_3, MIDASR_4, MIDASR_5, MIDASR_6, MIDASR_7, MIDASR_8, MIDASR_9, MIDASR_10, MIDASR_11, MIDASR_12, MIDASR_13, MIDASR_14, MIDASR_15, MIDASR_16, MIDASR_17, MIDASR_18, MIDASR_19, MIDASR_20, MIDASR_21, MIDASR_22, MIDASR_23, MIDASR_24, MIDASR_25, MIDASR_26, MIDASR_27, MIDASR_28, MIDASR_29, MIDASR_30, MIDASR_31, MIDASR_32, MIDASR_33, MIDASR_34, MIDASR_35, MIDASR_36, MIDASR_37, MIDASR_38, MIDASR_39, MIDASR_40, MIDASR_41, MIDASR_42, MIDASR_43, MIDASR_44, MIDASR_45, MIDASR_46, MIDASR_47, MIDASR_48, MIDASR_49, MIDASR_50, MIDASR_51, MIDASR_52, MIDASR_53, MIDASR_54, MIDASR_55, MIDASR_56, MIDASR_57, MIDASR_58, MIDASR_59, MIDASR_60, MIDASR_61, MIDASR_62, MIDASR_63, MIDASR_64, MIDASR_65, MIDASR_66, MIDASR_67, MIDASR_68, MIDASR_69, MIDASR_70, MIDASR_71, MIDASR_72, MIDASR_73, MIDASR_74, MIDASR_75, MIDASR_76, MIDASR_77, MIDASR_78, MIDASR_79, MIDASR_80, MIDASR_81, MIDASR_82, MIDASR_83, MIDASR_84, MIDASR_85, MIDASR_86, MIDASR_87, MIDASR_88, MIDASR_89]

midasf_array = [MIDASF_1, MIDASF_2, MIDASF_3, MIDASF_4, MIDASF_5, MIDASF_6, MIDASF_7, MIDASF_8, MIDASF_9, MIDASF_10, MIDASF_11, MIDASF_12, MIDASF_13, MIDASF_14, MIDASF_15, MIDASF_16, MIDASF_17, MIDASF_18, MIDASF_19, MIDASF_20, MIDASF_21, MIDASF_22, MIDASF_23, MIDASF_24, MIDASF_25, MIDASF_26, MIDASF_27, MIDASF_28, MIDASF_29, MIDASF_30, MIDASF_31, MIDASF_32, MIDASF_33, MIDASF_34, MIDASF_35, MIDASF_36, MIDASF_37, MIDASF_38, MIDASF_39, MIDASF_40, MIDASF_41, MIDASF_42, MIDASF_43, MIDASF_44, MIDASF_45, MIDASF_46, MIDASF_47, MIDASF_48, MIDASF_49, MIDASF_50, MIDASF_51, MIDASF_52, MIDASF_53, MIDASF_54, MIDASF_55, MIDASF_56, MIDASF_57, MIDASF_58, MIDASF_59, MIDASF_60, MIDASF_61, MIDASF_62, MIDASF_63, MIDASF_64, MIDASF_65, MIDASF_66, MIDASF_67, MIDASF_68, MIDASF_69, MIDASF_70, MIDASF_71, MIDASF_72, MIDASF_73, MIDASF_74, MIDASF_75, MIDASF_76, MIDASF_77, MIDASF_78, MIDASF_79, MIDASF_80, MIDASF_81, MIDASF_82, MIDASF_83, MIDASF_84, MIDASF_85, MIDASF_86, MIDASF_87, MIDASF_88, MIDASF_89]

sedan_array = [Sedan_1, Sedan_2, Sedan_3, Sedan_4, Sedan_5, Sedan_6, Sedan_7, Sedan_8, Sedan_9, Sedan_10, Sedan_11, Sedan_12, Sedan_13, Sedan_14, Sedan_15, Sedan_16, Sedan_17, Sedan_18, Sedan_19, Sedan_20, Sedan_21, Sedan_22, Sedan_23, Sedan_24, Sedan_25, Sedan_26, Sedan_27, Sedan_28, Sedan_29, Sedan_30, Sedan_31, Sedan_32, Sedan_33, Sedan_34, Sedan_35, Sedan_36, Sedan_37, Sedan_38, Sedan_39, Sedan_40, Sedan_41, Sedan_42, Sedan_43, Sedan_44, Sedan_45, Sedan_46, Sedan_47, Sedan_48, Sedan_49, Sedan_50, Sedan_51, Sedan_52, Sedan_53, Sedan_54, Sedan_55, Sedan_56, Sedan_57, Sedan_58, Sedan_59, Sedan_60, Sedan_61, Sedan_62, Sedan_63, Sedan_64, Sedan_65, Sedan_66, Sedan_67, Sedan_68, Sedan_69, Sedan_70, Sedan_71, Sedan_72, Sedan_73, Sedan_74, Sedan_75, Sedan_76, Sedan_77, Sedan_78, Sedan_79, Sedan_80, Sedan_81, Sedan_82, Sedan_83, Sedan_84, Sedan_85, Sedan_86, Sedan_87, Sedan_88, Sedan_89]

count_array = [count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9, count_10, count_11, count_12, count_13, count_14, count_15, count_16, count_17, count_18, count_19, count_20, count_21, count_22, count_23, count_24, count_25, count_26, count_27, count_28, count_29, count_30, count_31, count_32, count_33, count_34, count_35, count_36, count_37, count_38, count_39, count_40, count_41, count_42, count_43, count_44, count_45, count_46, count_47, count_48, count_49, count_50, count_51, count_52, count_53, count_54, count_55, count_56, count_57, count_58, count_59, count_60, count_61, count_62, count_63, count_64, count_65, count_66, count_67, count_68, count_69, count_70, count_71, count_72, count_73, count_74, count_75, count_76, count_77, count_78, count_79, count_80, count_81, count_82, count_83, count_84, count_85, count_86, count_87, count_88, count_89]

column_names = ['-', 'format_clear', 'ffb_clear', 'load_clear', 'perl_clear', 'smurf',
'neptune', 'pod', 'dict_simple', 'teardrop', 'guest', 'portsweep', 'ipsweep', 'land', 'ftp-write',
 'imap', 'back', 'syslog', 'satan', 'phf', 'ffb', 'nmap', 'multihop', 'warez',
'warezmaster', 'warezclient', 'rootkit', 'spy', 'warzclient', 'format', 'loadmodule',
'eject', 'perlmagic', 'format-fail', 'anomaly', 'dict', 'eject-fail', 'multihop-s',
'ps-s', 'ps-b', 'apache2', 'worm', 'sqlattack', 'httptunnel-s', 'sendmail-e', 'sendmail-b',
'xterm', 'snmpguess', 'named-e', 'named-a', 'named-b', 'snmpgetattack', 'anomaly-time',
'anomaly-source', 'anomaly-commands', 'processtable', 'xlock-b', 'xlock-a', 'multihop-b',
'multihop-e', 'xsnoop-b', 'xsnoop-a', 'sendmail-a', 'saint', 'u2r1', 'udpstorm', 'smurfttl',
 'anomaly-identity', 'multihop-a', 'format-s', 'u2r2', 'mscan', 'format-b', 'u2r3', 'ps-e',
'xterm-b', 'xterm-s', 'rootkit-b', 'rootkit-a', 'neptunettl', 'xlock', 'eject-s', 'httptunnel-e',
'httptunnel-a', 'mailbomb', 'ignore', 'xterm-e', 'ftp-write-b', 'ftp-write-a', 'rootkit-s']


#dos_categories = [40,5,6,13,7,16]
#probe_categories = [11,12,18]
dos_cat = []
u2r_cat = []
probe_cat = []
r2l_cat = []
misc_cat = []

for i in column_names:
    if i.__contains__("u2r") or i.__contains__("format") or i.__contains__("ffb") or i.__contains__("xterm") or i.__contains__("ps")\
           or i.__contains__("eject") or i.__contains__("perl") or i.__contains__("load") or i.__contains__("sqlattack") \
            or i.__contains__("rootkit"):
        u2r_cat.append(column_names.index(i))

    elif i.__contains__("neptune") or i.__contains__("warez") or i.__contains__("mailbomb") or i.__contains__("apache2") or i.__contains__("smurf") or \
            i.__contains__("land") or i.__contains__("warz") or i.__contains__("processtable") or i.__contains__("udpstorm") or i.__contains__("syslog") \
            or i.__contains__("snmpgetattack") or i.__contains__("pod") or i.__contains__("teardrop") or i.__contains__("back"):
        dos_cat.append(column_names.index(i))

    elif i.__contains__("ftp-write") or i.__contains__("httptunnel") or i.__contains__("phf") or i.__contains__("sendmail") or \
       i.__contains__("xsnoop") or i.__contains__("named") or i.__contains__("xlock") or i.__contains__("guest") or i.__contains__("dict") or \
            i.__contains__("snmp") or i.__contains__("imap") or i.__contains__("spy") or i.__contains__("multihop") or i.__contains__("worm"):
        r2l_cat.append(column_names.index(i))

    elif i.__contains__("sweep") or i.__contains__("satan") or i.__contains__("saint") or i.__contains__("mscan") or i.__contains__("nmap"):
        probe_cat.append(column_names.index(i))

    else:
        misc_cat.append(column_names.index(i))








print("\t\t\t\t\t\t\tDARPA DATASET RESULTS AT OPTIMUM THRESHOLD\n")
with open(filename, newline='', encoding='latin1') as rows:
    row_reader = csv.DictReader(rows, delimiter=',')
    for row in row_reader:
        if (row['Attack'] in column_names):
            value = column_names.index(row['Attack'])
            #print(value)
            array.append([value,int(row['MIDAS']), int(row['MIDASR']), int(row['MIDASF']), int(row['SedanSpot'])])


for i in range(0, len(array)):
    counter += 1
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
                q = array[i][0] - 1
                count_array[q] += 1
                anom_count += 1
                if (array[i][1] == 1):
                    midas_array[q] += 1
                if (array[i][2] == 1):
                    midasr_array[q] += 1
                if (array[i][3] == 1):
                    midasf_array[q] += 1
                if (array[i][4] == 1):
                    sedan_array[q] += 1


def percentage_of_attack(M, R, F, S, T):
    if (int(T) == 0):
        print("None")
        return
    M_percent = float(M) / float(T)
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

    print("MIDAS: " + str(M_percent) + "% correctly classified as anomalies while missing " + str(
        (T - M)) + " of the " + str(T) + " total anomalous packets")
    print("MIDASR: " + str(R_percent) + "% correctly classified as anomalies while missing " + str(
        (T - R)) + " of the " + str(T) + " total anomalous packets")
    print("MIDASF: " + str(F_percent) + "% correctly classified as anomalies while missing " + str(
        (T - F)) + " of the " + str(T) + " total anomalous packets")
    print("SedanSpot: " + str(S_percent) + "% correctly classified as anomalies while missing " + str(
        (T - S)) + " of the " + str(T) + " total anomalous packets" + "\n")


def percentage_total(EC, NC, T, method):
    N_percent = (float(NC) + float(EC)) / float(T)
    TC = NC + EC
    N_percent = N_percent * 100
    N_percent = round(N_percent, 2)

    if (method == 1):
        print("Total: " + str(N_percent) + "% correctly classified as anomalous while missing " + str(
            (T - TC)) + " of the " + str(T) + " total anomalous packets")
    if method == 2:
        print("Total: " + str(N_percent) + "% of the data are false negatives with " + str(
            (TC)) + " falsely classified out of the " + str(
            T) + " total benign packets")
    if method == 3:
        print("Total: " + str(N_percent) + "% of the data are correctly classified with " + str(
            (TC)) + " correctly classified packets out of the " + str(
            T) + " total packets")

MIDAS_correct, MIDASR_correct, MIDASF_correct, SEDAN_correct,COUNT_correct = (0,0,0,0,0)


for i in range(0, len(midas_array)):
        #print("\n\n\t\t\t\t" + column_names[i+1] + "\n")
        #print("---------------------------------------------------------------------------")
        #percentage_of_attack(midas_array[i], midasr_array[i], midasf_array[i], sedan_array[i], count_array[i])

        MIDAS_correct += midas_array[i]
        MIDASR_correct += midasr_array[i]
        MIDASF_correct += midasf_array[i]
        SEDAN_correct += sedan_array[i]
        COUNT_correct += count_array[i]

        if i in dos_cat:
            dos_array[0] += midas_array[i]
            dos_array[1] += midasr_array[i]
            dos_array[2] += midasf_array[i]
            dos_array[3] += sedan_array[i]
            dos_array[4] += count_array[i]

        if i in probe_cat:
            probe_array[0] += midas_array[i]
            probe_array[1] += midasr_array[i]
            probe_array[2] += midasf_array[i]
            probe_array[3] += sedan_array[i]
            probe_array[4] += count_array[i]

        if i in r2l_cat:
            r2l_array[0] += midas_array[i]
            r2l_array[1] += midasr_array[i]
            r2l_array[2] += midasf_array[i]
            r2l_array[3] += sedan_array[i]
            r2l_array[4] += count_array[i]

        if i in u2r_cat:
            u2r_array[0] += midas_array[i]
            u2r_array[1] += midasr_array[i]
            u2r_array[2] += midasf_array[i]
            u2r_array[3] += sedan_array[i]
            u2r_array[4] += count_array[i]

        if i in misc_cat:
            misc_array[0] += midas_array[i]
            misc_array[1] += midasr_array[i]
            misc_array[2] += midasf_array[i]
            misc_array[3] += sedan_array[i]
            misc_array[4] += count_array[i]


total_cats = [dos_cat, probe_cat, r2l_cat, u2r_cat, misc_cat]

for i in range(0, len(total_cats)):
    if i == 0:
        print("Attacks Categorized as Denial of Service Attack")
        print("------------------------------------------------")
        for i in total_cats[i]:
            print(column_names[i])
    if i == 1:
        print("\nAttacks Categorized as Probe Attack")
        print("------------------------------------------------")
        for i in total_cats[i]:
            print(column_names[i])
    if i == 2:
        print("\nAttacks Categorized as R2L Attack")
        print("------------------------------------------------")
        for i in total_cats[i]:
            print(column_names[i])
    if i == 3:
        print("\nAttacks Categorized as U2R Attack")
        print("------------------------------------------------")
        for i in total_cats[i]:
            print(column_names[i])
    if i == 4:
        print("\nAttacks Categorized as Unable able to Categorize")
        print("------------------------------------------------")
        for i in total_cats[i]:
            print(column_names[i])


print_cats = ["\t\t\t\t\t\tDenial of Service\n", "\t\t\t\t\t\tProbe\n", "\t\t\t\t\t\tRoot to Local\n","\t\t\t\t\t\tUser to Root\n", "\t\t\t\t\t\tCouldn't Classify\n"]
print_arrays = [dos_array, probe_array, r2l_array, u2r_array, misc_array]
for i in range(0, len(print_cats)):
    print(print_cats[i])
    print("---------------------------------------------------------------------------")
    percentage_of_attack(print_arrays[i][0], print_arrays[i][1], print_arrays[i][2], print_arrays[i][3], print_arrays[i][4])


print("\n\n\n\t\t\t\tTotals per Device\n")
print("---------------------------------------------------------------------------")
percentage_of_attack(MIDAS_correct, MIDASR_correct, MIDASF_correct, SEDAN_correct, anom_count)


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
percentage_total(Sedan_tn, (SEDAN_correct), counter, 3)

f.close