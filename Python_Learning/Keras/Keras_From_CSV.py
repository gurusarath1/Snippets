import numpy as np
import keras as k
import matplotlib.pyplot as plt

#function to learn in this csv: OUT=sin(x)+3y+5z
#Load the dataset
data = np.loadtxt('DataSet_CSV.csv', dtype=float, delimiter=',', skiprows=1)


#Split the dataset into training, validation and test data
data_X_train = data[:1000,:3]
data_Y_train = data[:1000,3:]

data_X_test = data[1000:1500,:3]
data_Y_test = data[1000:1500,3:]

data_X_valid = data[1500:,:3]
data_Y_valid = data[1500:,3:]

#This function generates the model
def generateModel():

	model = k.models.Sequential()

	model.add(k.layers.Dense(7, input_shape=(3,)))
	model.add(k.layers.Dense(7))
	model.add(k.layers.Dense(5))
	model.add(k.layers.Dense(5))
	model.add(k.layers.Dense(7))
	model.add(k.layers.Dense(1))

	model.compile(optimizer='rmsprop',
		loss = 'mean_squared_error',
		metrics=['accuracy'])

	return model


#Generate the model
m = generateModel()


#Fit the dataset
history = m.fit(data_X_train, data_Y_train, epochs=100, batch_size=200, validation_data = (data_X_valid, data_Y_valid))


# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()


#Check the predicted values for some values from the test set
print(data_X_test[0:10,:])
print(m.predict(data_X_test[0:10,:]))

