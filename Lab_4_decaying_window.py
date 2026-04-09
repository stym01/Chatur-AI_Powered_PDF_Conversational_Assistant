import pandas as pd
import math
from collections import defaultdict
import kagglehub
import os


class DecayingWindowTrend:

    def __init__(self, decay_rate):
        self.lambda_decay = decay_rate
        self.movie_scores = defaultdict(float)
        self.current_time = None


    def load_stream(self, file_path):
        """
        Load dataset and sort by timestamp to simulate stream
        """
        data = pd.read_csv(file_path)
        data = data.sort_values("timestamp")

        # latest time in dataset
        self.current_time = data["timestamp"].max()

        return data


    def process_stream(self, data):

        for _, row in data.iterrows():

            movie_id = row["movieId"]
            rating = row["rating"]
            timestamp = row["timestamp"]

            delta_t = self.current_time - timestamp

            weight = math.exp(-self.lambda_decay * delta_t)

            self.movie_scores[movie_id] += rating * weight


    def get_top_movies(self, k=10):

        sorted_movies = sorted(
            self.movie_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_movies[:k]


# ---------------- MAIN PROGRAM ---------------- #

# Download dataset from Kaggle
path = kagglehub.dataset_download("luisreimberg/ratingscsv")

print("Dataset downloaded at:", path)

# Find ratings.csv inside folder
ratings_file = os.path.join(path, "ratings.csv")

# Create object
trend_detector = DecayingWindowTrend(decay_rate=0.000001)

# Load stream
ratings_stream = trend_detector.load_stream(ratings_file)

# Process ratings
trend_detector.process_stream(ratings_stream)

# Get top trending movies
top_movies = trend_detector.get_top_movies(10)

print("\nTop Trending Movies (Decaying Window):")

for movie, score in top_movies:
    print("MovieID:", movie, "Score:", round(score, 3))