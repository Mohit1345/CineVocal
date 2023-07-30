import movieposters
import requests
# Get the link to the poster for "Jackie Brown"

def get_poster(Title):
    poster_url = movieposters.get_poster(Title)

    # Download the poster
    response = requests.get(poster_url)
    with open(f"posters\{Title}.jpg", "wb") as f:
        f.write(response.content)

get_poster("World War Z")