import requests
from bs4 import BeautifulSoup

def extract_movie_plot(movie_title):
    # Format the movie title for the Wikipedia URL
    formatted_title = movie_title.replace(' ', '_')
    url = f'https://en.wikipedia.org/wiki/{formatted_title}'

    # Send a GET request to the Wikipedia page
    response = requests.get(url)
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the section of the Wikipedia page that contains the movie plot
    plot_section = soup.find('span', id='Plot')

    if plot_section:
        # Extract the movie plot text from the plot section
        plot = plot_section.find_next('p').get_text().strip()
        return plot
    else:
        return None

# Example usage
movie_title = 'Sairat'
plot = extract_movie_plot(movie_title)

if plot:
    print(f"Plot of '{movie_title}':")
    print(plot)
else:
    print(f"Plot of '{movie_title}' not found on Wikipedia.")
# print