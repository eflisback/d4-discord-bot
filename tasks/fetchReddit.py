import requests
from bs4 import BeautifulSoup

url = "https://www.reddit.com/r/diablo4/top/?t=day"
html = requests.get(url)


s = BeautifulSoup(html.content, "html.parser")

print(s)

results = s.find(class_="y8HYJ-y_lTUHkQIc1mdCq _2INHSNB8V5eaWp4P0rY_mE")
titles = results.find_all("h3")

print(titles[0].text)

# id t3_13e8cjf
# class _eYtD2XCVieq6emjKBH3m
