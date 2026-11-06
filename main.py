import pandas as pd

# Loads the restaurant reviews dataset
reviews = pd.read_csv("data/yelp_sentiment_master_dataset.csv")

# Displays the first five records
print(reviews.head())

# Displays the number of rows and columns
print(reviews.shape)

# Displays the column names
print(reviews.columns)

# Displays information about the dataset
reviews.info()




# Counts how many reviews received each star rating
print("\nDistribution of Star Ratings:")
print(reviews["stars_review"].value_counts().sort_index())

# Counts how many reviews fall into each sentiment category
print("\nDistribution of Review Sentiment:")
print(reviews["rating_review"].value_counts())

# Calculates the overall average customer rating
average_rating = reviews["stars_review"].mean()

print("\nOverall Average Customer Rating:")
print(round(average_rating, 2))






# Groups reviews by restaurant and calculate average ratings
restaurant_summary = reviews.groupby(
    ["name", "city", "state"]
).agg(
    average_rating=("stars_review", "mean"),
    reviews_in_dataset=("stars_review", "count")
).reset_index()

# Only includes restaurants with at least 10 reviews in the dataset
well_reviewed = restaurant_summary[
    restaurant_summary["reviews_in_dataset"] >= 10
]

# Sorts restaurants from highest to lowest average rating
top_restaurants = well_reviewed.sort_values(
    by="average_rating",
    ascending=False
).head(10)

# Displays the top 10 restaurants
print("\nTop 10 Restaurants by Average Customer Rating:")
print(top_restaurants)