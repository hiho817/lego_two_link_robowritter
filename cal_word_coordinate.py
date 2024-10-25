import matplotlib.pyplot as plt
import numpy as np
word_data = []
filename = 'RoboWriter\春.txt'
with open(filename, 'r') as file:
    for line in file:
        # Remove any leading/trailing whitespace and split the line by commas
        coordinates = line.strip().split(',')
        # Convert each string to a float
        coordinate = [float(angle) for angle in coordinates]
        # Append the motor angles to the list
        word_data.append(coordinate)

word_data = np.array(word_data)
word_data = word_data.T
word_data = word_data[:, word_data[0] != -1]
# print(word_data)

min_values = np.min(word_data, axis=1)
max_values = np.max(word_data, axis=1)

# print(min_values,max_values)

# Define the target ranges for x and y
x_target_min, x_target_max = 0.10, 0.16
y_target_min, y_target_max = 0.08, 0.18

# Extract x and y data
x_data = word_data[0]
y_data = word_data[1]

# Normalize the data to range [0, 1]
x_normalized = (x_data - min_values[0]) / (max_values[0] - min_values[0])
y_normalized = (y_data - min_values[1]) / (max_values[1] - min_values[1])

# Map the normalized data to the target ranges
x_mapped = x_normalized * (x_target_max - x_target_min) + x_target_min
y_mapped = y_normalized * (y_target_max - y_target_min) + y_target_min
y_mapped = 0.26 - y_mapped

# Combine x_mapped and y_mapped into one array
mapped_data = np.vstack((x_mapped, y_mapped)).T

# Write the mapped data to a text file
output_filename = '春_mapped_data.txt'
np.savetxt(output_filename, mapped_data, delimiter=',', fmt='%.3f')

plt.plot(x_mapped, y_mapped, marker='o', linestyle='-', color='r')
plt.grid(True)
plt.show()
