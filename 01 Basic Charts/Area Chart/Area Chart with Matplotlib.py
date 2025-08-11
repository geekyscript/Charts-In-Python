import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 8, 12, 20]

# Create area chart using fill_between
plt.fill_between(x, y, color='skyblue', alpha=0.5)
plt.plot(x, y, color='blue', marker='o')

# Add titles and labels
plt.title('Area Chart with Matplotlib')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()
