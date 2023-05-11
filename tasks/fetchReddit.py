import requests
import json

upvote_threshold = 250
post_history_limit = 100


def fetch_reddit_data():
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
