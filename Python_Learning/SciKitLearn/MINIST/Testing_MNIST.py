#May 5 2019
#Written by Guru Sarath

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
import random as rnd
import numpy as np
import math


Dataset = pd.read_csv('train.csv')

print(Dataset.head(5))

y = Dataset['label']
X = Dataset.drop('label', axis = 1)

showData = math.ceil(rnd.random()*1000) #Generate a random number
grid_data = X.iloc[showData].as_matrix().reshape(28,28) #Get the pixel data of that random number in a matrix format
plt.imshow(grid_data, interpolation = 'none', cmap='gray') #Output the image
print('Data Label - ', y[showData]) # Do a sanity check to see if the output image is same as the label corresponding to that image
plt.show()



clf = SGDClassifier(random_state = 42) #Create a Stochastic gradient descent classifier
clf.fit(X, y) #Train the classifier


# Check the classifier on the test set data
TestSet = pd.read_csv('test.csv')
X_test = TestSet #Test set has no lables

print('Shape of Test set  - ', X_test.shape)
print('Test set - ', X_test.head(5))

for i in range(15):

	random_digit = math.ceil(rnd.random()*1000)
	print(random_digit, ' data picked')
	print('\n\n\nPredicted value -------- ')
	print(	clf.predict(	np.array(	[	X_test.iloc[random_digit]	]	)	)	)
	print('\n\n\n')

	grid_data = X_test.iloc[random_digit].as_matrix().reshape(28,28)
	plt.imshow(grid_data, interpolation = 'none', cmap='gray')
	plt.show()