# Restaurant Reviews Analysis
# This project explores restaurant customer reviews using Python and Pandas.
# It analyses customer ratings, restaurant performance, sentiment and categories.

import pandas as pd

# ==========================================
# 1. LOADING AND EXPLORING THE DATASET
# ==========================================

# Loading the restaurant reviews dataset
reviews = pd.read_csv("data/yelp_sentiment_master_dataset.csv")

# Displaying the first five records
print("\nFirst Five Records:")
print(reviews.head())

# Displaying the number of rows and columns
print("\nDataset Dimensions:")
print(reviews.shape)

# Displaying the column names
print("\nDataset Columns:")
print(reviews.columns)

# Displaying information about the dataset
print("\nDataset Information:")
reviews.info()

# ==========================================
# 2. ANALYZING THE CUSTOMER RATINGS
# ==========================================

# Counting how many reviews received each star rating
print("\nDistribution of Star Ratings:")
print(reviews["stars_review"].value_counts().sort_index())

# Counting how many reviews fall into each sentiment category
print("\nDistribution of Review Sentiment:")
print(reviews["rating_review"].value_counts())

# Calculating the overall average customer rating
average_rating = reviews["stars_review"].mean()

# Displaying the overall average rating rounded to two decimal places
print("\nOverall Average Customer Rating:")
print(round(average_rating, 2))

# ==========================================
# 3. ANALYZING THE RESTAURANT PERFORMANCE
# ==========================================

# Grouping the reviews by restaurant and calculate average ratings
# The restaurant name, city and state identify each restaurant
restaurant_summary = reviews.groupby(
    ["name", "city", "state"]
).agg(
    average_rating=("stars_review", "mean"),
    reviews_in_dataset=("stars_review", "count")
).reset_index()

# Only including restaurants with at least 10 reviews in the dataset
well_reviewed = restaurant_summary[
    restaurant_summary["reviews_in_dataset"] >= 10
]

# Sorting restaurants from highest to lowest average rating
top_restaurants = well_reviewed.sort_values(
    by="average_rating",
    ascending=False
).head(10)

# Displaying the top 10 restaurants by average customer rating
print("\nTop 10 Restaurants by Average Customer Rating:")
print(top_restaurants)

# Finding the 10 restaurants with the most reviews in the dataset
most_reviewed = restaurant_summary.sort_values(
    by="reviews_in_dataset",
    ascending=False
).head(10)

# Displaying the top 10 most-reviewed restaurants
print("\nTop 10 Most Reviewed Restaurants:")
print(most_reviewed)

# ==========================================
# 4. COMPARING STAR RATINGS AND SENTIMENT
# ==========================================

# Comparing star ratings with sentiment classifications
sentiment_comparison = pd.crosstab(
    reviews["stars_review"],
    reviews["rating_review"]
)

# Displaying the comparison between star ratings and sentiment
print("\nStar Ratings Compared with Review Sentiment:")
print(sentiment_comparison)

# ==========================================
# 5. EXPLORING THE RESTAURANT CATEGORIES
# ==========================================

# Displaying examples of restaurant categories
print("\nRestaurant Categories:")
print(reviews["categories"].head(10))

# Separating individual categories wherever a comma appears
categories = reviews["categories"].str.split(",").explode()

# Removing unnecessary spaces from category names
categories = categories.str.strip()

# Counting the most common restaurant categories
category_counts = categories.value_counts().head(10)

# Displaying the top 10 most frequent restaurant categories
print("\nTop 10 Restaurant Categories:")
print(category_counts)