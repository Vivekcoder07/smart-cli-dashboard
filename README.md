# Smart CLI Dashboard

## Project Description

Smart CLI Dashboard is a Python-based command-line interface tool that provides quick access to various pieces of information by fetching data from multiple free, publicly available APIs.

## Features

*   Get a random quote from ZenQuotes API.
*   Fetch the Astronomy Picture of the Day from NASA APOD API.
*   Retrieve public information for a given GitHub user.

## Prerequisites

*   Python 3.6 or higher
*   internet connection

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Vivekcoder07/smart-cli-dashboard.git
    cd smart_cli_dashboard
    ```

2.  **Initialize and activate the virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    # source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## NASA APOD API Key Configuration (Optional)

The NASA APOD function uses the `DEMO_KEY` by default, which has limitations. For higher rate limits, you can register for a free API key at [https://api.nasa.gov/](https://api.nasa.gov/) and potentially store it in a `config.ini` file or an environment variable.

## Usage Examples

Make sure your virtual environment is activated before running the commands.

*   **Get a random quote:**

    ```bash
    python main.py --quote
    ```

*   **Get NASA Astronomy Picture of the Day:**

    ```bash
    python main.py --apod
    ```

*   **Get GitHub user information (replace `<USERNAME>` with the actual GitHub username):**

    ```bash
    python main.py --github-user octocat
    ```

## Technologies Used

*   Python 3
*   `requests` library
*   `argparse` module

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developer

Vivek Patel ([Vivekcoder07](https://github.com/Vivekcoder07))