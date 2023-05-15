import os
import json
import openai
import discord
import requests
from io import BytesIO
from PIL import Image


def handle_image(message, name, id) -> discord.File:
    with open("user_keys.json", "r") as file:
        data = json.load(file)
        for item in data["openai"]:
            if item["user"] == id:
                prompt = remove_first_word(message)
                key = item["key"]
                return prompt_dalle(prompt, key)

    return f"I can't find an OpenAI API key for you, {name}. To add your key to my super secret JSON file, use `!add openai <key>` \n \n (*Pro tip: Send it as a direct message in order to prevent your key from being stolen.*)"


def prompt_dalle(prompt, key):
    openai.api_key = key
    response = openai.Image.create(
        prompt=f"{prompt} dark medieval fantasy style, diablo game series",
        n=1,
        size="1024x1024",
    )
    image_url = response["data"][0]["url"]
    req_res = requests.get(image_url)
    img = Image.open(BytesIO(req_res.content))
    img.save("image.png")

    with open("image.png", "rb") as f:
        return discord.File(f)


def remove_first_word(string):
    words = string.split()
    if len(words) > 1:
        return " ".join(words[1:])
    else:
        return ""
