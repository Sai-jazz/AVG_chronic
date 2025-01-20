import numpy as np
import matplotlib.pyplot as plt
from dtaidistance import dtw

# Input: Graph 1 points
x1 = np.array([1, 3, 4, 6, 8, 13])
y1 = np.array([5.2, 8.7, 8.8, 8.5, 6.3, 4.1])

# Generate Graph 2 with random points
np.random.seed(42)
x2 = np.sort(np.random.uniform(1, 13, len(x1)))
y2 = np.random.uniform(4, 9, len(x1))

# Interpolation to a common x-axis for comparison
common_x = np.linspace(1, 13, 100)
y1_interpolated = np.interp(common_x, x1, y1)
y2_interpolated = np.interp(common_x, x2, y2)

# Compute DTW distance and similarity index
dtw_distance = dtw.distance(y1_interpolated, y2_interpolated)
similarity_index = 1 / (1 + dtw_distance)

# Plot both graphs
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label="Graph 1 (Original)", color='blue', marker='o')
plt.plot(x2, y2, label="Graph 2 (Random)", color='orange', marker='x')
plt.title(f"Graph Comparison - Similarity Index: {similarity_index:.4f}")
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()
