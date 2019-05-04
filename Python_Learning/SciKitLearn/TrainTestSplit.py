from sklearn.model_selection import train_test_split
from sklearn import datasets
import numpy as np


X = datasets.load_iris()

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X.data, X.target , test_size=0.33, random_state=42)

# -----------------------------------------------

Data = np.genfromtxt('DataSet.txt', delimiter = ',')

X_Train, X_Test, Y_Train, Y_Test = train_test_split(Data[:,:-1], Data[:,-1], test_size=0.33, random_state=42)

print(X_Train, X_Test, Y_Train, Y_Test )
