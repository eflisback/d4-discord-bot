import requests
import json

url = "https://www.reddit.com/r/diablo4.json"

response = requests.get(url, headers={"User-agent": "D4-discord-bot"})
data = response.json()

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

posts = data["data"]["children"]

relevant_posts = []

for post in posts[:5]:
    title = post["data"]["title"]
    ups = post["data"]["ups"]
    selftext = post["data"]["selftext"]

    if ups > 100:
        relevant_post = {"title": title, "ups": ups, "selftext": selftext}
        relevant_posts.append(relevant_post)

# Save relevant posts in a JSON file
with open("relevant_posts.json", "w") as file:
    json.dump(relevant_posts, file, indent=4)
