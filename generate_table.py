import math
import random

# Set same seed to match CSV output
random.seed(42)

# Ferris wheel parameters
radius = 30
midline = 30
period = 180
omega = 2 * math.pi / period
interval = 5
total_time = 30 * 60
std_dev = 0.05 * (radius + midline)

with open("table.html", "w") as f:
    for t in range(0, total_time + 1, interval):
        height = radius * math.cos(omega * t) + midline
        noisy = height + random.gauss(0, std_dev)
        f.write(f"<tr><td>{t}</td><td>{round(noisy, 2)}</td></tr>\n")

print("table.html generated with seeded Gaussian noise.")
