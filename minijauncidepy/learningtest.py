import numpy as np
import matplotlib.pyplot as plt
from dtaidistance import dtw
import ask

# Graph 1
x1 = np.array([1, 3, 4, 6, 8, 13, 23])
y1 = np.array([5.2, 8.7, 8.8, 8.5, 6.3, 4.1, 2.3])

# Generate Graph 2 with random points
x2 = np.array(ask.x)
y2 = np.array(ask.y)  # Graph 2 with larger y-values

# Normalize Graph 2's y-values to the range of Graph 1
y2_normalized = (y2 - np.min(y2)) / (np.max(y2) - np.min(y2)) * (np.max(y1) - np.min(y1)) + np.min(y1)

# Interpolate Graph 2's y-values to align with Graph 1's x-values
y2_aligned = np.interp(x1, x2, y2_normalized)

# Graph 1 learns from Graph 2
learning_rate = 0.5  # Determines how much Graph 1 adapts to Graph 2
y1_learned = y1 + learning_rate * (y2_aligned - y1)

# Interpolation to a common x-axis for comparison
common_x = np.linspace(1, 23, 100)
y1_interpolated = np.interp(common_x, x1, y1)
y2_interpolated = np.interp(common_x, x2, y2_normalized)

# Compute DTW distance and similarity index
dtw_distance = dtw.distance(y1_interpolated, y2_interpolated)
similarity_index = 1 / (1 + dtw_distance)

# Plot both graphs and the learned graph
plt.figure(figsize=(12, 8))
plt.plot(x1, y1, label="avg jaundice recover time (Original)", color='blue', marker='o')
plt.plot(x2, y2_normalized, label="patient (Normalized)", color='orange', marker='x')
plt.plot(x1, y1_learned, label="learned graph (Learned)", color='green', linestyle='--', marker='s')
plt.title(f"Graph Comparison - Similarity Index: {similarity_index:.4f}")
plt.legend()
plt.xlabel("No. of Days")
plt.ylabel("Bilrubin levels (mg/dl)")
plt.grid()
plt.show()
