import json


def handle_add(message, id) -> str:
    substrings = message.split()

    if len(substrings) != 3:
        return "That's not quite right. Write your command like this: `!add <API type> <API key>`"

    api_type = substrings[1]
    api_key = substrings[2]

    with open("user_keys.json", "r") as file:
        data = json.load(file)

    data[api_type].append({"user": id, "key": api_key})

    with open("user_keys.json", "w") as file:
        json.dump(data, file, indent=4)

    return "Successfully added your API key to my secret JSON file!"
