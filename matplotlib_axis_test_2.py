import matplotlib.pyplot as plt
import numpy as np

# Generate some example independent data for x and y
x = np.array([1, 3, 5, 7, 9])  # Lengths in feet
y = np.array([14, 27, 35, 42, 51])  # Corresponding lengths in inches

fig, ax = plt.subplots()
ax.plot(x, y, 'bo')  # Plot data as blue dots

# Customize the tick labels on the x-axis to show feet and inches
x_ticks_labels = [f"{val} ft\n{int(val)*12} in" for val in x]
ax.set_xticks(x)
ax.set_xticklabels(x_ticks_labels)

# Customize the tick labels on the y-axis to show inches
y_ticks_labels = [f"{val} in" for val in y]
ax.set_yticks(y)
ax.set_yticklabels(y_ticks_labels)

# Set the labels for the axes
ax.set_xlabel('Length')
ax.set_ylabel('Length')

plt.show()
