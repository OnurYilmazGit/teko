import requests
from bs4 import BeautifulSoup

def receive_court(plz, court_type, url="https://gerichtsstand.net/suche/"):
    """
    Fetches the name of the court starting with the specified court type for the given PLZ.

    Parameters:
    plz (str): The postal code to search for.
    court_type (str): The type of the court (e.g., "Amtsgericht").

    Returns:
    str: The name of the court starting with the specified court_type for the given PLZ.

    Raises:
    Exception: If there was an error making the HTTP request or parsing the response.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    params = {
        'plz': plz,
        'ort': ''
    }

    response = requests.get(url, params=params, headers=headers)

    # Check if request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    court_section = soup.find('div', class_='row')

    # Check if court section was found
    if not court_section:
        raise Exception("Failed to find court section in page")

    courts = court_section.find_all('a')

    for court in courts:
        if court.get_text().startswith(court_type):
            return court.get_text()

    # No court found that starts with court_type
    return None