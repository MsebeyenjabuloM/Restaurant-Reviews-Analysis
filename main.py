import pandas as pd

# Load the restaurant reviews dataset
reviews = pd.read_csv("data/yelp_sentiment_master_dataset.csv")

# Display the first five records
print(reviews.head())

# Display the number of rows and columns
print(reviews.shape)

# Display the column names
print(reviews.columns)

# Display information about the dataset
reviews.info()