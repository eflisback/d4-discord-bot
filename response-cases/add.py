import json


def handle_add(message, id) -> str:
    substrings = message.split()

    if len(substrings) != 3:
        return "That's not quite right. Write your command like this: `!add <API type> <API key>`"

    api_type = substrings[1].lower()
    api_key = substrings[2]

    with open("user_keys.json", "r") as file:
        data = json.load(file)

    if api_type in data:
        for entry in data[api_type]:
            if entry["user"] == id:
                entry["key"] = api_key
                response = f"It seems like you already had a key registered for {api_type}. Worry not! It has now been overwritten."
                break
        else:
            data[api_type].append({"user": id, "key": api_key})
            response = (
                f"Successfully added your {api_type} API key to my secret JSON file!"
            )
    else:
        data[api_type] = [{"user": id, "key": api_key}]
        response = f"Successfully added your {api_type} API key to my secret JSON file!"

    with open("user_keys.json", "w") as file:
        json.dump(data, file, indent=4)

    return response
