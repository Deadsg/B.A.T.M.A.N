import agi
import cagi
import CAGI

class SelfLearningDataLoader:
    def __init__(self):
        self.data = []

    def add_data_point(self, x, y):
        self.data.append((x, y))

    def get_data(self):
        return self.data

# Example usage:
data_loader = SelfLearningDataLoader()

# Add some data points
data_loader.add_data_point(2, 70)
data_loader.add_data_point(3, 85)
data_loader.add_data_point(1, 50)
data_loader.add_data_point(5, 90)

# Get the data
data = data_loader.get_data()

# Print the data
for point in data:
    print(f"Study Hours: {point[0]}, Exam Score: {point[1]}")