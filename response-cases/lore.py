from bs4 import BeautifulSoup
import requests
import random
import re


def handle_lore() -> str:
    article_urls = [
        "https://diablo.fandom.com/wiki/Dark_Exile",
        "https://diablo.fandom.com/wiki/Great_Conflict",
        "https://diablo.fandom.com/wiki/Bleaked_Years",
        "https://diablo.fandom.com/wiki/Mage_Clan_Wars",
    ]

    url = random.choice(article_urls)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    lore_snippets = soup.select(".mw-parser-output > p")
    random_snippet = random.choice(lore_snippets).text.strip()
    random_snippet = re.sub(r"\[\d+\]", "", random_snippet)

    response = random_snippet + f"\n \n  *--- Read more: <{url}> ---*"

    return response
