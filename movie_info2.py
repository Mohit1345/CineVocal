import requests
import os
from dotenv import load_dotenv
load_dotenv()



api_key = os.environ['omdb_api']

def plot(movie_title):
    url = f'http://www.omdbapi.com/?apikey={api_key}&t={movie_title}&plot=full'

    response = requests.get(url)
    data = response.json()

    plot = data['Plot']
    print(plot)
    return plot

