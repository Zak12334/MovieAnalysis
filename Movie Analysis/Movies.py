#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on a sunny day


Student Name: Zak Osman (Sekeriye)???

Student ID: R00237642

Cohort: SD3A???

"""
import pandas as pd
import matplotlib.pyplot as plt

def task1():
 
   # Load the dataset
    movies_df = pd.read_csv('Movies-1.csv')
    
    # Get the counts of each main genre
    Genre_counts = movies_df['Genre'].value_counts()
    
    # Get the total number of unique main genres
    total_unique_Genres = Genre_counts.shape[0]  # .shape[0] gives the number of rows/items
    
    # Get the most and least popular main genres
    most_popular_Genre = Genre_counts.idxmax()  # idxmax() gives the index of the max value
    least_popular_Genre = Genre_counts.idxmin()  # idxmin() gives the index of the min value
    
    # Print the required information with messages
    print(f"There are {total_unique_Genres} unique genres in the dataset.")
    print(f"The most popular genre is '{most_popular_Genre}'.")
    print(f"The least popular genre is '{least_popular_Genre}'.")
    
    # Visualization of the top 8 main genres
    top_8_genres = Genre_counts.head(8)  # Get the first 8 items
    top_8_genres.plot(kind='bar')  # Make a bar plot
    
    # Set the title and labels of the plot
    plt.title('Top 8 Main Genres')
    plt.xlabel('Main Genre')
    plt.ylabel('Number of Movies')
    
    # Show the plot
    plt.show()

# Call task1 to execute
task1()


def task2():

 # Load the dataset from the CSV file
    movies_df = pd.read_csv('Movies-1.csv')
    
    # Split the 'genre' column into individual genres and count each genre's occurrence
    # 'explode' is used to transform each element of a list-like to a row
    genre_counts = movies_df['Genre'].str.split(',').explode().value_counts()
    
    # Find the most common genre (the one with the maximum count)
    most_common_genre = genre_counts.idxmax()
    
    # Find the least common genre (the one with the minimum count)
    least_common_genre = genre_counts.idxmin()
    
    # Print the most and the least common genres
    print(f"The most common genre is: {most_common_genre}")
    print(f"The least common genre is: {least_common_genre}")

# Execute the function to see the results
task2()
    
    
    
def task3():
    
   # Load the dataset
    movies_df = pd.read_csv('Movies-1.csv')
    
    # Remove ' min' from the 'Runtime' column and convert to numeric, forcing errors to NaN
    movies_df['Runtime'] = pd.to_numeric(movies_df['Runtime'].str.replace(' min', ''), errors='coerce')
    
    # Drop rows with NaN values in 'Runtime'
    movies_df.dropna(subset=['Runtime'], inplace=True)
    
    # Convert 'Runtime' to integers
    movies_df['Runtime'] = movies_df['Runtime'].astype(int)
    
    # Create a boxplot to visualize outliers
    plt.figure(figsize=(10,6))
    plt.boxplot(movies_df['Runtime'], vert=False)  # 'vert=False' makes the boxplot horizontal
    plt.title('Boxplot of Movie Durations (Runtime)')
    plt.xlabel('Minutes')
    
    # Display the boxplot
    plt.show()

    # Calculate IQR to identify outliers
    Q1 = movies_df['Runtime'].quantile(0.25)
    Q3 = movies_df['Runtime'].quantile(0.75)
    IQR = Q3 - Q1

    # Define outliers using IQR
    outliers = movies_df[(movies_df['Runtime'] < (Q1 - 1.5 * IQR)) | (movies_df['Runtime'] > (Q3 + 1.5 * IQR))]

    # Print the titles of the movies that are outliers
    print("Titles of movies considered outliers based on runtime:")
    for title in outliers['Title']:
        print(title)

# Execute the function to visualize outliers and print their titles
task3()


    
def task4():
    
 # Load the dataset
    movies_df = pd.read_csv('Movies-1.csv')
    
    # Check for null values and replace them with the mean of their respective column
    if movies_df['Number of Votes'].isnull().any():
        movies_df['Number of Votes'].fillna(movies_df['Number of Votes'].mean(), inplace=True)
    
    if movies_df['Rating'].isnull().any():
        movies_df['Rating'].fillna(movies_df['Rating'].mean(), inplace=True)
    
    # Create a scatter plot to analyze the relationship
    plt.figure(figsize=(10,6))
    plt.scatter(movies_df['Number of Votes'], movies_df['Rating'], alpha=0.5)
    plt.title('Relationship between Number of Votes and Rating')
    plt.xlabel('Number of Votes')
    plt.ylabel('Rating')
    
    # Display the figure
    plt.show()

# Execute the function to analyze the relationship and handle null values
task4()

# In task 4, we're looking at two things about each movie: how many people voted for it, and its average score.
# Sometimes, some movies might not have this information, and we call it 'null values'.
# To fix this, we find the average number (mean) of votes and scores from all the movies that do have this info.
# We then fill in the missing spots with these averages.
# This way, every movie has a vote count and a score, which lets us compare them properly without any gaps.


    
def task5():
    
    """
    I dont fully undurstand this task the wording of the question is very hard for me to undurstand. 
    """
    
    # This function reads a CSV file and returns a pandas DataFrame.
    # It uses an encoding that can handle a wide range of characters.
    def load_csv(file_name):
        return pd.read_csv(file_name, encoding='ISO-8859-1')

    # This function takes a pandas Series object (column from a DataFrame)
    # and applies text cleaning: converting to lowercase and removing specified punctuation.
    def clean_text(column):
        return column.str.lower().str.replace(r"[,.'-]", '', regex=True)

    # This is the main function for genre analysis.
    # It takes the filenames of the main_genre and Movies-1 CSV files as arguments.
    def main_genre_analysis(main_genre_file, movies_file):
        # Load the genre terms and movies data into DataFrames.
        main_genres = load_csv(main_genre_file)
        movies = load_csv(movies_file)
        
        # Clean the 'Synopsis' column in the movies DataFrame.
        movies['Synopsis'] = clean_text(movies['Synopsis'])

        # Iterate through each genre column in the main_genres DataFrame.
        for genre in main_genres.columns:
            # Get the genre terms, clean them, and join them into a regex pattern.
            terms = main_genres[genre].dropna().str.lower()
            pattern = '|'.join(terms)
            
            # Filter movies where the synopsis contains any of the genre terms.
            filtered_movies = movies[movies['Synopsis'].str.contains(pattern, na=False, regex=True)]
            
            # Find the most frequent main_Genre in the filtered movies,
            # or print 'None' if there are no matches.
            most_frequent = filtered_movies['main_Genre'].value_counts().idxmax() if not filtered_movies.empty else "None"
            
            # Print the main genre and the most frequent related main_Genre from the movies.
            print(f"{genre}: {most_frequent}")

    # Execute the genre analysis with the specified file names.
    main_genre_analysis('main_genre.csv', 'Movies-1.csv')
    
# Run the task
task5()
    
def task6():

       # Load movies data from a CSV file
    movies_df = pd.read_csv('Movies-1.csv')
    
    # Change the 'Rating' column to numeric and fill missing ratings with the column's average
    # This helps us handle missing or bad data without losing too much information.
    movies_df['Rating'] = pd.to_numeric(movies_df['Rating'], errors='coerce').fillna(movies_df['Rating'].mean())
    
    # Create a histogram to see how movie ratings are distributed
    # This visual helps us see the most common ratings and the range of ratings.
    plt.figure(figsize=(10, 6))
    movies_df['Rating'].plot(kind='hist', bins=20, title='Distribution of Movie Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Number of Movies')
    plt.grid(True)
    plt.show()
    
    # Get a summary of statistics for the 'Rating' column
    # This gives us a quick overview of the ratings, like the average rating, without having to look through all the data.
    rating_stats = movies_df['Rating'].describe()
    print(rating_stats)
    
    # Running this code, we should see:
    # - A histogram of ratings, which can tell us which ratings are most common.
task6()
