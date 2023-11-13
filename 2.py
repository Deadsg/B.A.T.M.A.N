#model sandbox
#this is gonna be your giant ass sandbox for testing several model architectures with a bunch of data from your dataset
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
import pickle
import os
from sklearn.model_selection import train_test_split
from PIL import Image
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from time import time
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping

policy = tf.keras.mixed_precision.Policy('mixed_float16')
tf.keras.mixed_precision.set_global_policy(policy)

def save_pickle(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)

def load_pickle(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data

def normalize_aspect_ratio(aspect_ratio:float):
    if aspect_ratio > 1: return 1-0.5/aspect_ratio
    else: return 0.5*aspect_ratio

#declare the paths to the data
imagepath = r'.\assets\2\thumbnails'
userpath = r'.\assets\2\users\seraph1.prefs'
postspath = r'.\assets\2\lotsofposts'
#grab the raw data
all_images = os.listdir(imagepath)
all_posts = load_pickle(postspath)
user_prefs = load_pickle(userpath)
#grab the entire raw dataset
posts = np.array(list(user_prefs.keys()))
all_tags = [all_posts[post]['tags'].split(' ') for post in posts]
images = [Image.open(os.path.join(imagepath, f'{post}.jpg')).convert('RGB') for post in posts]
#begin preprocessing the data
tags_index = np.array(sorted({tag for tags in all_tags for tag in tags}))
mlb = MultiLabelBinarizer(classes=tags_index)
tags = mlb.fit_transform(all_tags)
ar = np.array([normalize_aspect_ratio(image.size[1]/image.size[0]) for image in images])
images = np.array([np.array(image.resize((256,256))) for image in images])
prefs = np.array([user_prefs[post] for post in posts])
scores = np.array([all_posts[post]['score'] for post in posts])
#split the dataset between training and validation
training_posts, testing_posts, training_tags, testing_tags, training_images, testing_images, training_ars, testing_ars, training_scores, testing_scores, training_prefs, testing_prefs = train_test_split(posts, tags, images, ar, scores, prefs,test_size=0.1)

testing_prefs = np.array([np.array([int(not pref),pref]) for pref in testing_prefs])
training_prefs = np.array([np.array([int(not pref),pref]) for pref in training_prefs])

#compile the model
#simple conv regression
model = Sequential()
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(256, 256, 3)))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(512, (3, 3), activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Conv2D(512, (3, 3), activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Conv2D(512, (3, 3), activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Conv2D(512, (3, 3), activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Dense(256, activation='relu'))
model.add(BatchNormalization()) 
model.add(Dropout(0.2))
model.add(Dense(2, activation='softmax'))
custom_optimizer = Adam(learning_rate=0.0001)
model.compile(optimizer=custom_optimizer, loss='binary_crossentropy', metrics=['accuracy'])

#fit the model
early_stopping = EarlyStopping(monitor='val_accuracy',patience=50,verbose=1,restore_best_weights=True) 
model.fit(training_images, training_prefs, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stopping])

#evaluate the model
loss, accuracy = model.evaluate(testing_images, testing_prefs)
print(f'Accuracy: {accuracy * 100:.2f}%')

model.save(rf'.\assets\2\seraph{round(time())}a{int(accuracy*1000)}l{int(loss*1000)}.keras')

predictions = model.predict(training_images)
for prediction, pref, post in zip(predictions,testing_prefs,testing_posts):
    print(np.array([round(p) for p in prediction]), pref, post)




while True:
    x=input('>')
    try: exec(x)
    except: print('err')


#graveyard
#tags = MultiLabelBinarizer(classes=np.array(sorted({tag for tags in all_tags for tag in tags}))).fit_transform(all_tags)
#model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#model.add(Dense(2, activation='softmax'))  # Output layer with 2 classes
#custom_optimizer = Adam(learning_rate=1.0)

