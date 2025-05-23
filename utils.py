import requests
import os
import logging
from colorama import Fore, Style, init
import configparser

init(autoreset=True)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Read config.ini for NASA API key if available
config = configparser.ConfigParser()
config.read('config.ini')
def get_nasa_api_key():
    return os.getenv('NASA_API_KEY') or config.get('NASA', 'API_KEY', fallback='DEMO_KEY')

def get_random_quote():
    """Fetches a random quote from ZenQuotes API."""
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data and isinstance(data, list) and data[0]:
            quote_data = data[0]
            quote = quote_data.get("q", "No quote found")
            author = quote_data.get("a", "Unknown author")
            return f"{Fore.GREEN}\"{quote}\"{Style.RESET_ALL} - {Fore.CYAN}{author}{Style.RESET_ALL}"
        else:
            return f"{Fore.RED}Could not fetch quote. Invalid response format.{Style.RESET_ALL}"
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching quote: {e}")
        return f"{Fore.RED}Error fetching quote: {e}{Style.RESET_ALL}"
    except (ValueError, IndexError) as e:
        logging.error(f"Error parsing quote response: {e}")
        return f"{Fore.RED}Error parsing quote response: {e}{Style.RESET_ALL}"

def get_nasa_apod():
    """Fetches the Astronomy Picture of the Day from NASA APOD API."""
    api_key = get_nasa_api_key()
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        title = data.get("title", "No title available")
        explanation = data.get("explanation", "No explanation available")
        image_url = data.get("hdurl") or data.get("url", "No image URL available")
        return (f"{Fore.YELLOW}NASA Astronomy Picture of the Day:{Style.RESET_ALL}\n"
                f"{Fore.GREEN}Title:{Style.RESET_ALL} {title}\n"
                f"{Fore.GREEN}Explanation:{Style.RESET_ALL} {explanation}\n"
                f"{Fore.BLUE}Image URL:{Style.RESET_ALL} {image_url}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching NASA APOD: {e}")
        return f"{Fore.RED}Error fetching NASA APOD: {e}{Style.RESET_ALL}"

def get_github_user_info(username):
    """Fetches public information for a given GitHub user."""
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return f"{Fore.RED}GitHub user '{username}' not found.{Style.RESET_ALL}"
        response.raise_for_status()
        data = response.json()
        name = data.get("name", "N/A")
        bio = data.get("bio", "N/A")
        public_repos = data.get("public_repos", 0)
        followers = data.get("followers", 0)
        following = data.get("following", 0)
        profile_url = data.get("html_url", "N/A")
        return (f"{Fore.MAGENTA}GitHub User Information for {username}:{Style.RESET_ALL}\n"
                f"{Fore.GREEN}Name:{Style.RESET_ALL} {name}\n"
                f"{Fore.GREEN}Bio:{Style.RESET_ALL} {bio}\n"
                f"{Fore.GREEN}Public Repos:{Style.RESET_ALL} {public_repos}\n"
                f"{Fore.GREEN}Followers:{Style.RESET_ALL} {followers}\n"
                f"{Fore.GREEN}Following:{Style.RESET_ALL} {following}\n"
                f"{Fore.BLUE}Profile URL:{Style.RESET_ALL} {profile_url}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching GitHub user info: {e}")
        return f"{Fore.RED}Error fetching GitHub user info: {e}{Style.RESET_ALL}"
