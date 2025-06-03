import math
import random

# Ferris wheel parameters
radius = 30
midline = 30
period = 180  # seconds per revolution
omega = 2 * math.pi / period

# Sampling parameters
interval = 5
total_time = 30 * 60  # 30 minutes in seconds

# Noise parameters
max_height = radius + midline
std_dev = 0.05 * max_height  # 5% Gaussian noise

# Output file
output_file = "table.html"

with open(output_file, "w") as f:
    for t in range(0, total_time + 1, interval):
        ideal_height = radius * math.cos(omega * t) + midline
        noisy_height = ideal_height + random.gauss(0, std_dev)
        f.write(f"<tr><td>{t}</td><td>{round(noisy_height, 2)}</td></tr>\n")

print(f"{output_file} generated with Gaussian noise.")
