import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the provided text file
data = pd.read_csv('4weight.txt', sep='\t', skiprows=1)

# Check if Position column is named correctly
print(data.columns)  # This will help us see if the Position column is named differently

# Extract relevant columns
time = data['Time (s)']
force = data['Force (N)']

# Check for Position column (may have a different name or missing values)
if 'Position (m)' in data.columns:
    position = data['Position (m)']
    # Remove rows where position is missing
    position = position.dropna()
else:
    print("Position column not found or may be named differently.")
    position = None

# Plot the graphs only if the position data is valid
plt.figure(figsize=(12, 6))

# Subplot 1: Position vs Time, plot only if position data exists
if position is not None and not position.empty:
    plt.subplot(1, 2, 1)
    plt.plot(time[:len(position)], position, color='b', label='Position (m)')
    plt.title('Position vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.grid(True)
    plt.legend()
else:
    print("No valid position data to plot.")

# Subplot 2: Force vs Time
plt.subplot(1, 2, 2)
plt.plot(time, force, color='r', label='Force (N)')
plt.title('Force vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Force (N)')
plt.grid(True)
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()


















