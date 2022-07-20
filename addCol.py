import sys

import pandas as pd

#This Python file is used to add Label to the CSV files to show if an entry is anomalous or not


args = sys.argv[1:]

for filename in args:
    df = pd.read_csv(filename)
    # df2 = pd.read_csv("/home/kali/Research/HRCL/CSV/dos2.csv")
    # df3 = pd.read_csv("/home/kali/Research/HRCL/CSV/dos3.csv")
    # df4 = pd.read_csv("/home/kali/Research/HRCL/CSV/benign.csv")
    # df5 = pd.read_csv("/home/kali/Research/HRCL/CSV/benign_dos1.csv")
    # df6 = pd.read_csv("/home/kali/Research/HRCL/CSV/benign_dos2.csv")
    # df7 = pd.read_csv("/home/kali/Research/HRCL/CSV/benign_dos3.csv")

    df["Label"] = "0"
    df["Attack"] = "Benign"
    # df2["Label"] = "1"
    # df3["Label"] = "1"
    # df4["Label"] = "0"
    # df5["Label"] = "0"
    # df6["Label"] = "0"
    # df7["Label"] = "0"

    df.to_csv(filename, index=False)
    # df2.to_csv("/home/kali/Research/HRCL/CSV/Processed/dos2.csv", index=False)
    # df3.to_csv("/home/kali/Research/HRCL/CSV/Processed/dos3.csv", index=False)
    # df4.to_csv("/home/kali/Research/HRCL/CSV/Processed/benign.csv", index=False)
    # df5.to_csv("/home/kali/Research/HRCL/CSV/Processed/benign_dos1.csv", index=False)
    # df6.to_csv("/home/kali/Research/HRCL/CSV/Processed/benign_dos2.csv", index=False)
    # df7.to_csv("/home/kali/Research/HRCL/CSV/Processed/benign_dos3.csv", index=False)
