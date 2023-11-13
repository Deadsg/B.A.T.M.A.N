import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np 

# Define the parameters
num_samples = 1000
input_shape = 10
num_classes = 5
num_epochs = 10

# Generate random data
X_train = np.random.rand(num_samples, input_shape)
y_train = np.random.randint(0, num_classes, num_samples)

X_val = np.random.rand(num_samples // 5, input_shape)
y_val = np.random.randint(0, num_classes, num_samples // 5)

X_test = np.random.rand(num_samples // 5, input_shape)
y_test = np.random.randint(0, num_classes, num_samples // 5)

# Create and train the model
model = Sequential([
    Dense(units=64, activation='relu', input_shape=(input_shape,)),
    Dense(units=32, activation='relu'),
    Dense(units=num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=num_epochs, validation_data=(X_val, y_val))

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {test_accuracy}')

model.save('Batman_Keras.h5')