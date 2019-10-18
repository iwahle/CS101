
# imports

from keras.models import Sequential
from keras.layers import Conv2d, Dense, Flatten, MaxPooling2D
from keras.losses import cross_entropy
from keras.optimizers import SGD
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# load data 

# TODO
X = []
y = []

# define training and validation sets
x_train, y_train, x_test, y_test = train_test_split(X, 
													y, 
													test_size=0.25, 
													random_state=42)


# model definition

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), strides=(1, 1),
                 activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))


# training

model.compile(loss=cross_entropy,
              optimizer=SGD(lr=0.01),
              metrics=['accuracy'])

batch_size = ?
epochs = ?
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

