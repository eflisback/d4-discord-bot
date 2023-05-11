import requests
import json


def fetch_reddit_data(server_id):
    # Load the settings from JSON file
    try:
        with open("config/server_variables.json", "r") as file:
            settings = json.load(file)
    except FileNotFoundError:
        print("Settings file not found.")
        return None, None

    # Use settings for the specific server if available, otherwise use default settings
    server_settings = settings.get(str(server_id), settings.get("default"))

    upvote_threshold = server_settings.get("upvote_threshold")
    post_history_limit = server_settings.get("post_history_limit")
    url = "https://www.reddit.com/r/diablo4.json"

    response = requests.get(url, headers={"User-agent": "D4-discord-bot"})
    data = response.json()

    posts = data["data"]["children"]

    try:
        with open("./used_titles.json", "r") as file:
            used_titles = json.load(file)
    except FileNotFoundError:
        used_titles = []

    for post in posts[:5]:
        title = post["data"]["title"]
        ups = post["data"]["ups"]
        selftext = post["data"]["selftext"]

        if ups > upvote_threshold and title not in used_titles:
            used_titles.append(title)

            if len(used_titles) > post_history_limit:
                used_titles.pop(0)

            with open("./used_titles.json", "w") as file:
                json.dump(used_titles, file)

            return title, selftext

    return None, None
