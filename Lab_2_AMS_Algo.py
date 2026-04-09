import pandas as pd
import random
import hashlib
import math

import numpy as np
from collections import Counter

# Load Netflix Dataset
df = pd.read_csv("netflix_titles.csv")

print("Total rows:", len(df))


# Stream Column
stream = df["release_year"].dropna().astype(int).tolist()
n = len(stream)

print("Stream size:", n)


# AMS Algorithm Class

class AMS:
    def __init__(self, stream_size, k=40):
        self.n = stream_size
        self.k = k
        
        # Random sample positions
        self.sample_positions = [
            random.randint(0, self.n - 1)
            for _ in range(self.k)
        ]
        
        self.samples = [None] * self.k
        self.counts = [0] * self.k

    def process_stream(self, stream):
        for i, item in enumerate(stream):
            for j in range(self.k):
                if i == self.sample_positions[j]:
                    self.samples[j] = item
                    self.counts[j] = 1
                elif self.samples[j] == item:
                    self.counts[j] += 1

    def estimate_F2(self):
        estimates = []
        
        for c in self.counts:
            if c > 0:
                estimates.append(self.n * (2*c - 1))
        
        return np.mean(estimates)


# Run AMS Algorithm

ams = AMS(n, k=60)
ams.process_stream(stream)

estimate = ams.estimate_F2()

print("\nEstimated F2 (AMS):", int(estimate))


# Actual F2 (For Comparison)

freq = Counter(stream)
actual_F2 = sum(v*v for v in freq.values())

print("Actual F2:", actual_F2)

# Distortion Calculation

distortion = abs(estimate - actual_F2) / actual_F2 * 100

print("\nDistortion (%):", round(distortion, 2), "%")