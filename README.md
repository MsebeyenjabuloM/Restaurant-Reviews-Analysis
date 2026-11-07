# Restaurant-Reviews-Analysis

## Overview

My project explores restaurant customer reviews using Python and Pandas. My goal was to develop my practical data analysis skills by working with a real-world dataset, learning how to organise the information, identify patterns, and use code to answer questions about customer ratings and restaurant performance.

The dataset used in this project is the Yelp restaurant reviews sentiment dataset, downloaded from Zenodo. It contains 14,351 review records and 11 columns of information, including individual star ratings, review text, restaurant names, categories, locations, business ratings, and sentiment classifications.

Dataset source: [Yelp Restaurant Reviews Sentiment Dataset – Zenodo](https://zenodo.org/records/18723813)

I wrote this program to be able to explore the dataset and investigate customer ratings, restaurant performance, review sentiment, and restaurant categories. I used Python and Pandas to load, organise, filter, group, and analyse the data.

## Data Analysis Results

The analysis explored the following questions:

1. What is the distribution of customer star ratings, and what is the overall average rating?
   - The dataset contains 1,422 one-star reviews, 1,277 two-star reviews, 1,795 three-star reviews, 3,949 four-star reviews, and 5,908 five-star reviews.
   - The overall average customer rating is 3.81 out of 5.

2. Which restaurants have the highest average customer ratings?
   - I grouped the reviews by restaurant name and location, then calculated their average ratings.
   - To make the comparison more meaningful, I only included restaurants with at least 10 review records in this dataset.
   - Bangkokville Thai Cuisine in Nashville, Tennessee, had the highest average rating at approximately 4.92 out of 5, based on 13 records in the dataset.

3. Which restaurants have the most reviews in this dataset?
   - Luke in New Orleans, Louisiana, had the highest number of review records, with **187**.
   - Its average customer rating was approximately 4.15 out of 5.
   - This showed that the restaurants with the highest average ratings are not necessarily the same restaurants with the most reviews.

4. Which restaurant categories appear most frequently?
   - The most frequent categories were Restaurants, Food, Nightlife, Bars, and American (New).
   - The category Restaurants appeared in all 14,351 records.
   - Some records contain multiple categories, so category counts can overlap.

5. How do star ratings compare with the sentiment classifications?
   - One- and two-star reviews were classified as Negative.
   - Three-star reviews were classified as Neutral.
   - Four- and five-star reviews were classified as Positive.
   - The sentiment classifications matched the star ratings exactly in this dataset. This means they are not an independent measure of customer sentiment.

## Development Environment

The project was developed using:

- Visual Studio Code
- Python 3.14.10
- Pandas 3.1.1
- Windows PowerShell
- A Python virtual environment (`.venv`)

Programming language and libraries

I used Python as the programming language and Pandas as the main library for data analysis. Pandas helped me read the CSV file, inspect the dataset, count values, calculate averages, group records by restaurant, compare classifications, and analyse restaurant categories.

## Useful Websites
- [Data Analysis with Python Course](https://www.youtube.com/live/EsDFiZPljYo?si=gVX5uCCfz_RDDpfs)
- [What Is Data Analysis? An Expert Guide With Examples](https://www.datacamp.com/blog/what-is-data-analysis-expert-guide)
- [What Is Data Science? Definition, Skills, Applications & More](https://seas.harvard.edu/news/what-data-science-definition-skills-applications-more)
- [Python Documentation](https://docs.python.org/3/)
- [Pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/overview.html)
- [Pandas 10 Minute Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html#min)
- [Zenodo](https://zenodo.org/) – For datasets and research resources.
- [Yelp Restaurant Reviews Sentiment Dataset – Zenodo](https://zenodo.org/records/18723813)

## Future Work

- Explore how customer ratings change over time by analysing the review dates.
- Investigate differences in customer ratings across restaurant locations and categories.
- Explore ways to evaluate the accuracy of the sentiment classifications using the original review text.