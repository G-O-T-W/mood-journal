import pandas as pd
import glob
import pathlib
from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer

FILEPATHS = sorted(glob.glob("*.txt", root_dir="entries"))
data = []
sentiment_analyzer = SentimentIntensityAnalyzer()


def get_data():
    # Clear data list to avoid appending duplicates on multiple calls
    data.clear()
    for filepath in FILEPATHS:
        # Get date as string in format Oct 21 2024
        date = datetime.strptime(filepath.split(".")[0], "%Y-%m-%d")
        date = date.strftime("%b %d %Y")

        # Get sentiment score
        filepath = pathlib.Path("entries", filepath)
        with open(filepath) as file:
            if filepath.is_file():
                entry = file.read()
                pos_score = sentiment_analyzer.polarity_scores(entry)["pos"]
                neg_score = sentiment_analyzer.polarity_scores(entry)["neg"]

        data.append((date, pos_score, neg_score))

    # Converting to dataframe
    df = pd.DataFrame(data, columns=["Date", "Positivity Score", "Negativity Score"])
    return df




if __name__ == "__main__":
    print(get_data())

