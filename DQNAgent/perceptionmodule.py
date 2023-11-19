import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import Sequential
from sklearn.feature_extraction.text import CountVectorizer

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

def text_processing(corpus):
    # Tokenize the text data
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(corpus)

    # Convert text to sequences of integers
    sequences = tokenizer.texts_to_sequences(corpus)

    # Pad sequences to have consistent length
    padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences)

    # Print the processed data
    print("Processed Text Data:")
    print(padded_sequences)

# Sample text data
corpus = ["This is a simple text.", "Text processing example.", "Natural Language Processing is interesting."]

# Call the text_processing function
text_processing(corpus)

def image_recognition():
    # Build a simple CNN model for image recognition
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Your image recognition logic goes here
    pass

def perception_module(input_shape):
    model = tf.keras.models.Sequential([
        layers.Flatten(input_shape=input_shape),  # Flatten the input
        layers.Dense(64, activation='relu'),       # Dense layer with ReLU activation
        layers.Dense(32, activation='relu'),       # Additional Dense layer
        layers.Dense(1, activation='sigmoid')      # Output layer with Sigmoid activation for binary classification
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model

# Example usage:
input_shape = (64, 64, 3)  # Adjust the input shape based on your data
perception_model = perception_module(input_shape)

# Display the model summary
perception_model.summary()

# Example usage:
input_shape = (64, 64, 3)  # Adjust the input shape based on your data
perception_model = perception_module(input_shape)

# Display the model summary
perception_model.summary()
# Sample text data
corpus = ["This is a simple text.", "Text processing example.", "Natural Language Processing is interesting."]

# Create a bag-of-words model using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# Call the respective functions based on your workflow
text_processing(corpus)
image_recognition()
perception_module(input_shape)