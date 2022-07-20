from pandas import read_csv
import numpy as np
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt


anoms = '/home/kali/Research/MIDAS/data/DARPA/darpa_ground_truth.csv'
test_option = input("Testing Options\n--------------\n1 for MIDAS\n2 for SedanSpot\n\nInput Option: ")
probas = ''
if (test_option == '1'):
    probas = '/home/kali/Research/MIDAS/temp/Score.txt'
else:
    probas = '/home/kali/Research/sedanspot/example/output.csv'
classifier = '/home/kali/Research/MIDAS/temp/Class.txt'

y = read_csv(anoms, header=None) #anoms
z = read_csv(probas, header=None) #Probabilities

class_out = open(classifier, "w")

# calculate roc curve
fpr, tpr, thresholds = metrics.roc_curve(y, z)

# calculate AUC
auc = metrics.roc_auc_score(y, z)



def compare(File1,File2):
    f1=open(File1,"r")
    f2=open(File2,"r")
    f3 = open("difference.txt", "w")
    linecounter = 0
    for line1 in f1:
        for line2 in f2:
                linecounter += 1
                # if line1==line2:
                #     assert True
                # else:
                #     if(line2 == "1\n"):
                f3.write("( " + str(linecounter) + " ) " + line2.strip() + " " + line1.strip() + "\n")
                break
    f1.close()
    f2.close()


#create ROC curve
plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()



print(tpr)
print(fpr)
print(thresholds)
optimal_idx = np.argmax(tpr - fpr)
optimal_threshold = thresholds[optimal_idx]
print("Threshold value is:", optimal_threshold)

with open(probas) as f:
   for line in f:
      if (float(line) >= optimal_threshold):
          class_out.write("1")
      else:
          class_out.write("0")
      class_out.write("\n")

class_out.close()

compare(classifier,anoms)


z = read_csv(classifier, header=None) #Probabilities

#print(metrics.confusion_matrix(z,y))
print('Precision: %.3f' % metrics.precision_score(z, y))
print('Recall: %.3f' % metrics.recall_score(z, y))
print('Accuracy: %.3f' % metrics.accuracy_score(z, y))
print('F1 Score: %.3f' % metrics.f1_score(z, y))
print('AUC: %.3f' % auc)

cf_matrix = metrics.confusion_matrix(z, y)
group_names = ['True Neg','False Pos','False Neg','True Pos']

group_counts = ["{0:0.0f}".format(value) for value in
                cf_matrix.flatten()]

group_percentages = ["{0:.2%}".format(value) for value in
                     cf_matrix.flatten()/np.sum(cf_matrix)]

labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in
          zip(group_names,group_counts,group_percentages)]

labels = np.asarray(labels).reshape(2,2)

ax = sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')

ax.set_title('Seaborn Confusion Matrix with labels\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])

## Display the visualization of the Confusion Matrix.
plt.show()
