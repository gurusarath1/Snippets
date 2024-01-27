from sklearn import linear_model
import numpy as np

# Load a csv dataset
X_Y_dataset = np.genfromtxt("small_dataset.csv", delimiter=",", skip_header=True) # Remove the first row as it containes column header text
print(X_Y_dataset)
X = X_Y_dataset[:,:-1] # All rows, discard last column
Y = X_Y_dataset[:,-1] # All rows, only last column
# Create the model object
lin_reg_model = linear_model.LinearRegression()
# Fit the model
lin_reg_model.fit(X,Y)
# Print the coeffs
print(lin_reg_model.coef_)
# Pint the intercept
print(lin_reg_model.intercept_)
