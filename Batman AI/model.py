import random

class SelfLearningModel:
    def __init__(self):
        self.coefficient = random.random()  # Initialize with a random coefficient

    def predict(self, x):
        return self.coefficient * x

    def update(self, x, y_true):
        y_pred = self.predict(x)
        error = y_true - y_pred

        learning_rate = 0.01
        self.coefficient += learning_rate * error * x

# Example usage:
model = SelfLearningModel()

# Simulated learning loop
for _ in range(100):
    # Generate random data point
    x = random.uniform(0, 10)
    y_true = 2 * x  # Assuming the true coefficient is 2

    # Predict and update
    y_pred = model.predict(x)
    model.update(x, y_true)

    print(f"x: {x}, y_true: {y_true}, y_pred: {y_pred}, Coefficient: {model.coefficient}")