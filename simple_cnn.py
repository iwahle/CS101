
# imports

from keras.models import Sequential
from keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from keras.losses import sparse_categorical_crossentropy
from keras.optimizers import SGD
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np

# load data 

path = "/Users/imanwahle/Desktop/CS101/"
tmp = np.load(path + "X.npy")
X = np.zeros((tmp.shape[0], tmp.shape[1], tmp.shape[2], 1))
X[:,:,:,0] = np.load(path + "X.npy")
y = np.load(path + "y.npy").astype(int)
n_classes = len(np.unique(y))

# define training and validation sets
x_train, x_test, y_train, y_test = train_test_split(X, 
													y, 
													test_size=0.25, 
													random_state=42)

# model definition

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(100,100,1)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dense(n_classes, activation='softmax'))



# training

model.compile(loss=sparse_categorical_crossentropy,
              optimizer=SGD(lr=0.01),
              metrics=['sparse_categorical_accuracy'])

model.summary()
batch_size = 32
epochs = 10
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

