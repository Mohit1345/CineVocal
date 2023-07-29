import requests
import os
from dotenv import load_dotenv
load_dotenv()




def fetch_movie_data(movie_title):
    base_url = "http://www.omdbapi.com/"
    api_key = os.environ['omdb_api'] # If you have one. Not required for basic usage.

    params = {
        "t": movie_title,
        "apikey": api_key,  # Not required if you don't have an API key.
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# # Example usage
# movie_title = "Inception"
# movie_data = fetch_movie_data(movie_title)

# if movie_data is not None:
#     print(f"Title: {movie_data['Title']}")
#     print(f"Year: {movie_data['Year']}")
#     print(f"Genre: {movie_data['Genre']}")
#     print(f"Director: {movie_data['Director']}")
#     print(f"Actors: {movie_data['Actors']}")
#     print(f"Plot: {movie_data['Plot']}")
# else:
#     print(f"Failed to fetch data for {movie_title}.")
# print(fetch_movie_data("Bhagam Bhag")['Genre']) 
