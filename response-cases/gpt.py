import openai
import json


def handle_gpt(message, name, id) -> str:
    with open("user_keys.json", "r") as file:
        data = json.load(file)
        for item in data["openai"]:
            if item["user"] == id:
                prompt = remove_first_word(message)
                key = item["key"]
                return prompt_gpt(prompt, key)

    return f"I can't find an OpenAI API key for you, {name}. To add your key to my super secret JSON file, use `!add openai <key>` \n \n (*Pro tip: Send me a direct message in order to prevent your key from being stolen.*)"


def prompt_gpt(prompt, key):
    print(prompt)
    openai.api_key = key
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Answer to the following as if you were Deckard Cain from Diablo: \n {prompt}",
            }
        ],
    )
    return completion.choices[0].message.content


def remove_first_word(string):
    words = string.split()
    if len(words) > 1:
        return " ".join(words[1:])
    else:
        return ""
