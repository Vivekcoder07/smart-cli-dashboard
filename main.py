import argparse
from utils import get_random_quote, get_nasa_apod, get_github_user_info
from colorama import Fore, Style, init
import logging

init(autoreset=True)
logging.basicConfig(level=logging.INFO)

__version__ = "1.0.0"

def main():
    """Main entry point for the Smart CLI Dashboard."""
    parser = argparse.ArgumentParser(description="Smart CLI Dashboard - Get quick info from various APIs.")
    
    # Define mutually exclusive arguments
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--quote", action="store_true", help="Get a random quote.")
    group.add_argument("--apod", action="store_true", help="Get NASA Astronomy Picture of the Day.")
    group.add_argument("--github-user", metavar="USERNAME", help="Get public information for a GitHub user.")
    group.add_argument("--dashboard", action="store_true", help="Show all dashboard info at once.")
    
    # (Optional) --version argument - requires setting up package metadata properly for a real distribution
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')

    args = parser.parse_args()

    if args.quote:
        print(get_random_quote())
    elif args.apod:
        # In a real application, you might read the API key from a config file or env var
        # For now, we use the demo key as specified.
        print(get_nasa_apod())
    elif args.github_user:
        print(get_github_user_info(args.github_user))
    elif args.dashboard:
        print(f"{Fore.CYAN}{Style.BRIGHT}--- Smart CLI Dashboard ---{Style.RESET_ALL}")
        print(get_random_quote())
        print()
        print(get_nasa_apod())
        print()
        print(get_github_user_info("Vivekcoder07"))

if __name__ == "__main__":
    main()
