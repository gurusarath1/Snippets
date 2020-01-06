import numpy as np
import keras as k

#function to learn in this csv: OUT=sin(x)+3y+5z
data = np.loadtxt('DataSet_CSV.csv', dtype=float, delimiter=',', skiprows=1)


data_X_train = data[:1000,:3]
data_Y_train = data[:1000,3:]

data_X_test = data[1000:1500,:3]
data_Y_test = data[1000:1500,3:]

data_X_valid = data[1500:,:3]
data_Y_valid = data[1500:,3:]


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



m = generateModel()

m.fit(data_X_train, data_Y_train, epochs=300, batch_size=200, validation_data = (data_X_valid, data_Y_valid))

print(data_X_test[0:10,:])
print(m.predict(data_X_test[0:10,:]))