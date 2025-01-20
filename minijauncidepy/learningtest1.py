import learningtest
import matplotlib.pyplot as plt

# Output the coordinates of the learned graph
learned_graph_coordinates = list(zip(learningtest.x1, learningtest.y1_learned))
for i, (x, y) in enumerate(learned_graph_coordinates):
    print(f"Point {i+1}: x = {x}, y = {y:.4f}")

# Update Graph 1 coordinates with the learned graph
x1 = learningtest.x1  # x1 remains the same
y1 = learningtest.y1_learned  # Update y1 to the learned y-values

# Print the updated coordinates
updated_graph_coordinates = list(zip(x1, y1))
for i, (x, y) in enumerate(updated_graph_coordinates):
    print(f"Updated Point {i+1}: x = {x}, y = {y:.4f}")

# Plot the updated Graph 1
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label="Updated Graph 1 (Learned)", color='blue', marker='o')
plt.title("Updated Graph 1")
plt.xlabel("No. of Days")
plt.ylabel("Bilirubin levels (mg/dl)")
plt.legend()
plt.grid()
plt.show()