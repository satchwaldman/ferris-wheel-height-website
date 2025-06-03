import math
import csv

# Parameters
radius = 30  # meters
midline = 30  # meters above ground
period = 180  # seconds per revolution
omega = 2 * math.pi / period  # angular frequency
sample_interval = 5  # seconds
total_time = 30 * 60  # 30 minutes in seconds

# CSV output file
filename = "ferris_wheel_data.csv"

# Generate data
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time (s)", "Height (m)"])

    for t in range(0, total_time + 1, sample_interval):
        height = radius * math.cos(omega * t) + midline
        writer.writerow([t, round(height, 2)])

print(f"Data saved to {filename}")
