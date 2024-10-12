import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


import pandas as pd
import matplotlib.pyplot as plt



# Read the file, skipping unnecessary rows
df = pd.read_csv('impulse rubber.txt', sep='\t', skiprows=1)

# Drop NaN values to avoid plotting issues
df.dropna(subset=['Time (s)', 'Velocity (m/s)', 'Force (N)'], inplace=True)

# Create a figure with two subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Plot Velocity vs Time
axs[0].plot(df['Time (s)'], df['Velocity (m/s)'], marker='o', color='b', label='Velocity')
axs[0].set_title('Velocity vs Time')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Velocity (m/s)')
axs[0].grid(True)
axs[0].legend()

# Plot Force vs Time
axs[1].plot(df['Time (s)'], df['Force (N)'], marker='s', color='r', label='Force')
axs[1].set_title('Force vs Time')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Force (N)')
axs[1].grid(True)
axs[1].legend()

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plots
plt.show()