# primitive_movie_service

You need a key api to be able to use this script. It's free. 
You can get it on this page: http://www.omdbapi.com

Once you have the key api, replace the <em>apikey</em> variable in line 5 of the script.

You can change the value of the </em>movie_list</em> variable (line 25) and put the movies you are interested in there. 

You have 5 functions to choose from:
- <em>download_data_about_movies</em> - to download data about selected movies
- <em>save_data_about_movies</em> - to save data about selected movies
- <em>display_a_list_of_titles_of_saved_movies</em> - to display a list of titles of **saved** movies in the terminal
- <em>display_the_best_rated_IMDB_movie</em> - to display the best rated IMDB movie
- <em>display_the_highest_grossing_movie</em> - to display the highest-grossing movie 
- <em>display_the_average_rating_of_saved_movies</em> - to view the average rating of **saved** movies


These functions accept a list of movie titles as an argument:
<em>display_the_best_rated_IMDB_movie</em> , <em>display_the_highest_grossing_movie</em>. 
You don't need to download data on selected movies beforehand to use them. (You don't need to use function <em>download_data_about_movies</em> before). 


These functions require reading data from a file:
<em>display_a_list_of_titles_of_saved_movies</em>, <em>display_the_average_rating_of_saved_movies</em>.
