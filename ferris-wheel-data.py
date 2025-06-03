import math
import random
import csv

# Set random seed for reproducibility
random.seed(42)

# Ferris wheel parameters
radius = 30
midline = 30
period = 180
omega = 2 * math.pi / period
interval = 5
total_time = 30 * 60
std_dev = 0.05 * (radius + midline)

with open("ferris_wheel_data.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time (s)", "Height (m)"])

    for t in range(0, total_time + 1, interval):
        height = radius * math.cos(omega * t) + midline
        noisy = height + random.gauss(0, std_dev)
        writer.writerow([t, round(noisy, 2)])

print("ferris_wheel_data.csv generated with seeded Gaussian noise.")
