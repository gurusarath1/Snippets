from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


(train_imgs, train_labels),(test_imgs, test_labels) = mnist.load_data()

network = models.Sequential()
network.add(layers.Dense(512,activation='relu',input_shape=(28*28,)))
network.add(layers.Dense(10,activation='softmax'))
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

train_imgs = train_imgs.reshape((60000 , 28*28))
train_imgs = train_imgs.astype('float32') / 255

test_imgs = test_imgs.reshape((10000 , 28*28))
test_imgs = test_imgs.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_imgs, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = network.evaluate(test_imgs, test_labels)
print('test_acc: ', test_acc)
