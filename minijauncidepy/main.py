import numpy as np
import matplotlib.pyplot as plt
from dtaidistance import dtw
import ask

# Input: average jaundice line graph
x1 = np.array([1, 3, 4, 6, 8, 13, 23])
y1 = np.array([5.2, 8.7, 8.8, 8.5, 6.3, 4.1, 2.3])

# Generate Graph 2 with random points

x2 = np.array(ask.x)
y2 = np.array(ask.y) # Graph 2 with larger y-values

# Normalize Graph 2's y-values to the range of Graph 1
y2_normalized = (y2 - np.min(y2)) / (np.max(y2) - np.min(y2)) * (np.max(y1) - np.min(y1)) + np.min(y1)

# Interpolation to a common x-axis for comparison
common_x = np.linspace(1, 13, 100)
y1_interpolated = np.interp(common_x, x1, y1)
y2_interpolated = np.interp(common_x, x2, y2_normalized)

# Compute DTW distance and similarity index
dtw_distance = dtw.distance(y1_interpolated, y2_interpolated)
similarity_index = 1 / (1 + dtw_distance)

# Plot both graphs
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label="Avg jaundice patient", color='blue', marker='o')
plt.plot(x2, y2_normalized, label="Your graph(Normalized)", color='orange', marker='x')
plt.title(f"Graph Comparison - Similarity Index: {similarity_index:.4f}")
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()
