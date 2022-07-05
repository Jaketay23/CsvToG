import pandas as pd



#df = pd.read_csv("/home/jaketay/Research/Possible_Dataset/dos2.csv")
df = pd.read_csv("/home/jaketay/Research/Possible_Dataset/copies/mirai.csv")
df2 = pd.read_csv("/home/jaketay/Research/Possible_Dataset/dos_b.csv")
# df3 = pd.read_csv("/home/jaketay/Research/Possible_Dataset/dos_attack2.csv")
# df4 = pd.read_csv("/home/jaketay/Research/Possible_Dataset/dos_benign2.csv")

# value = df3['Time'] + 31
# value = df4['Time'] + 31

df["Label"] = "1"
#df2["Label"] = "0"
# df3["Time"] = value
# df3["Label"] = "1"
# df4["Label"] = "0"

#df.to_csv("/home/jaketay/Research/Possible_Dataset/dos.csv", index=False)
#df2.to_csv("/home/jaketay/Research/Possible_Dataset/dos_b.csv", index=False)
df.to_csv("/home/jaketay/Research/Possible_Dataset/mirai.csv", index=False)
# df3.to_csv("/home/jaketay/Research/Possible_Dataset/dos_attack2.csv", index=False)
# df4.to_csv("/home/jaketay/Research/Possible_Dataset/dos_benign2.csv", index=False)