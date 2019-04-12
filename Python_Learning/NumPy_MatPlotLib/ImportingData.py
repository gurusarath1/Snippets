import csv
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
z = []

# Using Built in csv module
with open('SampleCSV.csv', 'r') as fileObj:
    Allrows = csv.reader(fileObj, delimiter = ',')
    for row in Allrows :
        x.append(row[0])
        y.append(int(row[1]))
        z.append(float(row[2]))

plt.bar(x,y)
plt.show()
# ----------------------------------

CSVFileArray = np.loadtxt('SampleCSV2.csv', delimiter = ',', unpack = True, dtype = str)
print(CSVFileArray)