import requests
from typing import List, Optional, Dict
import pandas as pd

apikey = "INSERT YOUR APIKEY"


#  Accept the list of movie titles and then download the data that we save.
def download_data_about_movies(movies: List[str]) -> List[Dict]:
    data_list = []
    for movie in movies:
        movie = movie.replace(" ", "+")
        query = f"http://www.omdbapi.com/?apikey={apikey}&t={movie}&type=movie"
        response = requests.get(query).json()
        data_list.append(response)
    return data_list


def save_data_about_movies(data_list: List[Dict], filename: Optional[str] = "file.csv") -> pd.DataFrame:
    to_write = pd.DataFrame(data_list)
    to_write.to_csv(filename, index=False)
    return to_write


movies_list = ["Skazany na bluesa", "Joker", "Monty Python and the Holy Grail", "Howl's Moving Castle",
               "Harry Potter and the Sorcerer's Stone", "C.H.U.D."]
downloaded_data = download_data_about_movies(movies_list)
save_data_about_movies(downloaded_data)


# Display a list of titles of saved movies in the terminal.
def display_a_list_of_titles_of_saved_movies(filename: str) -> List[int]:
    saved_data_df = pd.read_csv(filename)
    result = list(saved_data_df["Title"])
    print(result)
    return result


# Display the best rated IMDB movie in the terminal.
def display_the_best_rated_IMDB_movie(movies: List[str]) -> List[str]:
    downloaded_data = download_data_about_movies(movies)
    downloaded_data_df = pd.DataFrame(downloaded_data).copy()
    downloaded_data_df["imdbRating"] = downloaded_data_df["imdbRating"].astype("float")
    result = downloaded_data_df[downloaded_data_df["imdbRating"] == downloaded_data_df["imdbRating"].max()]
    print(result)
    return result


# Display the highest-grossing movie in the terminal.
def display_the_highest_grossing_movie(movies: List[str]) -> List[str]:
    downloaded_data = download_data_about_movies(movies)
    downloaded_data_df = pd.DataFrame(downloaded_data).copy()
    downloaded_data_df["BoxOffice"] = downloaded_data_df["BoxOffice"].str.replace('$', '')
    downloaded_data_df["BoxOffice"] = downloaded_data_df["BoxOffice"].str.replace(',', '')
    downloaded_data_df["BoxOffice"] = downloaded_data_df["BoxOffice"].str.replace('N/A', '0')
    downloaded_data_df["BoxOffice"] = downloaded_data_df["BoxOffice"].astype("int")
    result = downloaded_data_df[downloaded_data_df["BoxOffice"] == downloaded_data_df["BoxOffice"].max()]
    print(result)
    return result


# View the average rating of saved movies.
def display_the_average_rating_of_saved_movies(filename: str) -> int:
    saved_data_df = pd.read_csv(filename)
    saved_data_df["imdbRating"] = saved_data_df["imdbRating"].astype("float")
    result = saved_data_df["imdbRating"].mean()
    print(result)
    return result


print("The a list of titles of saved movies:")
display_a_list_of_titles_of_saved_movies("file.csv")
print("\n")
print("The highest grossing movie:")
display_the_highest_grossing_movie(movies_list)
print("The best_rated_IMDV_movie:")
display_the_best_rated_IMDB_movie(movies_list)
print("Average rating of saved movies:")
display_the_average_rating_of_saved_movies("file.csv")
