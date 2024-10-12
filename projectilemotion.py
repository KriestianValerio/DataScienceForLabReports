import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file to check its contents
file_path = '60 degree.csv'
data = pd.read_csv(file_path)

# Display the first few rows to understand its structure
data.head()


# Extract the correct columns based on their exact names
time = data['Time (s) Run #1']
x_position = data['x-Position, Object #5 (m) Run #1']
y_position = data['y-Position, Object #5 (m) Run #1']
x_velocity = data['x-Velocity, Object #5 (m/s) Run #1']
y_velocity = data['y-Velocity, Object #5 (m/s) Run #1']

# Create subplots for each graph
fig, axs = plt.subplots(5, 1, figsize=(8, 20))

# a. y-position vs x-position
axs[0].plot(x_position, y_position, label="y-position vs x-position")
axs[0].set_xlabel("x-position (m)")
axs[0].set_ylabel("y-position (m)")
axs[0].set_title("y-position vs x-position")
axs[0].grid(True)

# b. x-position vs Time
axs[1].plot(time, x_position, label="x-position vs Time", color='g')
axs[1].set_xlabel("Time (s)")
axs[1].set_ylabel("x-position (m)")
axs[1].set_title("x-position vs Time")
axs[1].grid(True)

# c. y-position vs Time
axs[2].plot(time, y_position, label="y-position vs Time", color='r')
axs[2].set_xlabel("Time (s)")
axs[2].set_ylabel("y-position (m)")
axs[2].set_title("y-position vs Time")
axs[2].grid(True)



# d. x-velocity vs Time
axs[3].plot(time, x_velocity, label="x-velocity vs Time", color='b')
axs[3].set_xlabel("Time (s)")
axs[3].set_ylabel("x-velocity (m/s)")
axs[3].set_title("x-velocity vs Time")
axs[3].grid(True)

# e. y-velocity vs Time
axs[4].plot(time, y_velocity, label="y-velocity vs Time", color='purple')
axs[4].set_xlabel("Time (s)")
axs[4].set_ylabel("y-velocity (m/s)")
axs[4].set_title("y-velocity vs Time")
axs[4].grid(True)
plt.subplots_adjust(hspace=0.5)
plt.show()
















import numpy as np
import matplotlib.pyplot as plt

# Extract the correct columns based on their exact names
time = data['Time (s) Run #1']
x_position = data['x-Position, Object #5 (m) Run #1']
y_position = data['y-Position, Object #5 (m) Run #1']
x_velocity = data['x-Velocity, Object #5 (m/s) Run #1']
y_velocity = data['y-Velocity, Object #5 (m/s) Run #1']

# Function to calculate best fit line (linear or quadratic)
def plot_best_fit(ax, x_data, y_data, xlabel, ylabel, title, color, degree=1):
    # Polynomial regression to find the coefficients
    coeffs = np.polyfit(x_data, y_data, degree)

    # Create a polynomial function from the coefficients
    poly_fit = np.poly1d(coeffs)

    # Create the label for the best fit equation based on the degree
    if degree == 2:
        equation_label = f'Best fit: y = {coeffs[0]:.2f}x² + {coeffs[1]:.2f}x + {coeffs[2]:.2f}'
    else:
        equation_label = f'Best fit: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}'

    # Plot the best fit line
    ax.plot(x_data, poly_fit(x_data), color=color, linestyle='--', label=equation_label)

    # Plot the original data
    ax.plot(x_data, y_data, label=f"{ylabel} vs {xlabel}", color=color)

    # Set labels and title
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

# Create subplots for each graph
fig, axs = plt.subplots(5, 1, figsize=(8, 20))

# a. y-position vs x-position (quadratic fit)
plot_best_fit(axs[0], x_position, y_position, "x-position (m)", "y-position (m)", "y-position vs x-position", 'blue', degree=2)

# b. x-position vs Time (linear fit)
plot_best_fit(axs[1], time, x_position, "Time (s)", "x-position (m)", "x-position vs Time", 'green', degree=1)

# c. y-position vs Time (quadratic fit)
plot_best_fit(axs[2], time, y_position, "Time (s)", "y-position (m)", "y-position vs Time", 'red', degree=2)

# d. x-velocity vs Time (linear fit)
plot_best_fit(axs[3], time, x_velocity, "Time (s)", "x-velocity (m/s)", "x-velocity vs Time", 'blue', degree=1)

# e. y-velocity vs Time (linear fit)
plot_best_fit(axs[4], time, y_velocity, "Time (s)", "y-velocity (m/s)", "y-velocity vs Time", 'purple', degree=1)

# Add extra spacing between subplots
plt.subplots_adjust(hspace=0.5)
plt.show()

