import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
DataSet = np.loadtxt('LinRegSampleDataSet.csv', delimiter = ',', unpack = True, dtype = float)
print(DataSet)

X = DataSet[:-1]
y = DataSet[-1]


X_rows, X_cols = X.shape
X = X.reshape((X_cols, X_rows))

reg = LinearRegression().fit(X, y)
score = reg.score(X, y)


#Get the learnt parameters
m = reg.coef_
c = reg.intercept_ 
print('\n\nCoefficients - ', reg.coef_)
print('Intercepts - ', reg.intercept_ )

#Making Predictions
x_forPrediction = 80
predictedValue = reg.predict(	np.array(	[[x_forPrediction]]	)	)


#To Draw the linear regression model
x_line = np.linspace(0,120,100) #(Start, End, Number of points)
y_line = (m * x_line) + c # Y=m*x + c

#Plot the linear regression output
plt.scatter(X,y, marker = '^', c = 'Black', alpha=0.2)
plt.plot(x_line, y_line, 'r--')
plt.scatter(x_forPrediction, predictedValue, marker = '*', s=300)
plt.show()

#----------------------------------------------------------------------------------------

# Load the dataset
DataSet = np.loadtxt('LinRegSampleDataSet_3D.csv', delimiter = ',', unpack = True, dtype = float)
print(DataSet)

x1 = np.array(	[DataSet[0]]	)	# Make it a 2D array
x2 = np.array(	[DataSet[1]]	)	# Make it a 2D array
y = DataSet[-1]


X_rows, X_cols = x1.shape
x1 = x1.reshape((X_cols, X_rows)) #Feature 1
X_rows, X_cols = x2.shape
x2 = x2.reshape((X_cols, X_rows)) #Feature 2

X = np.hstack(	(x1,x2)	) #Feature matrix

print('X', X)

reg = LinearRegression().fit(X, y)
score = reg.score(X, y)

theta = reg.coef_
c = reg.intercept_ 
print('\n\nCoefficients - ', reg.coef_)
print('Intercepts - ', reg.intercept_ )

x_forPrediction = [50,3.6]
predictedValue = reg.predict(	np.array(	[x_forPrediction]	)	)
print(predictedValue)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1,x2,y, marker = '*', alpha=1)
plt.show()