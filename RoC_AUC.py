import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from pathlib import Path
from sys import argv

from pandas import read_csv
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import linear_model as LR
from sklearn import metrics
import matplotlib.pyplot as plt
import csv
from sklearn.utils import column_or_1d

anoms = '/home/jaketay/Research/data/MIDAS_test/DDoS_anoms.csv'
probas = '/home/jaketay/Desktop/sedanspot-master/example/output.csv'
#probas = '/home/jaketay/Research/MIDAS/temp/Score.txt'

y = read_csv(anoms, header=None) #anoms
z = read_csv(probas, header=None) #Probabilities

# calculate roc curve
fpr, tpr, thresholds = metrics.roc_curve(y, z)

# calculate AUC
auc = metrics.roc_auc_score(y, z)
print('AUC: %.3f' % auc)


#
# #create ROC curve
# plt.plot(fpr,tpr)
# plt.ylabel('True Positive Rate')
# plt.xlabel('False Positive Rate')
# plt.show()
#
#
#create ROC curve
plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()
