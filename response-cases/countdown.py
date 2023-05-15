import datetime


def format_time_units(value, unit):
    if value == 1:
        unit = unit[:-1]
    return f"{value} {unit}"


def handle_countdown(message) -> str:
    substrings = message.lower().split()
    if len(substrings) != 2:
        return "I'm afraid that's not right. Write your command like this: `!countdown <event>`. Currently, the events available are `launch` and `lan`."

    event = substrings[1]

    match event:
        case "lan":
            target_time = datetime.datetime(2023, 6, 6, 18, 0, 0)  # June 6, 6pm

        case "launch":
            target_time = datetime.datetime(2023, 6, 6, 1, 0, 0)  # June 6, 1am

        case _:
            return f"I'm not sure I know when the {event} will take place... Sorry."

    current_time = datetime.datetime.now()
    time_remaining = target_time - current_time

    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    formatted_time = ", ".join(
        filter(
            None,
            [
                format_time_units(days, "days"),
                format_time_units(hours, "hours"),
                format_time_units(minutes, "minutes"),
                format_time_units(seconds, "seconds") if days == 0 else None,
            ],
        )
    )

    return f"{formatted_time}."
