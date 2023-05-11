import discord
import os
import responses
import sys
from dotenv import load_dotenv
from discord.ext import tasks

current_directory = os.path.dirname(os.path.realpath(__file__))
responses_directory = os.path.join(current_directory, "tasks")

sys.path.append(responses_directory)

# Other .py files
from fetchReddit import fetch_reddit_data

load_dotenv()


async def send_message(msg, content, is_private):
    try:
        response = responses.handle_response(content)
        await msg.author.send(response) if is_private else await msg.channel.send(
            response
        )
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = os.getenv("TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")
        fetch_data.start()  # Start the task as soon as the bot is ready

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return

        user = str(msg.author)
        content = str(msg.content)
        channel = str(msg.channel)

        print(f"{user} said {content} in {channel}.")

        if not content.startswith("!"):
            return

        content = content[1:]

        if content.startswith("dm "):
            content = content[3:]
            await send_message(msg, content, is_private=True)
        else:
            await send_message(msg, content, is_private=False)

    @tasks.loop(minutes=1)
    async def fetch_data():
        print("Fetching Reddit data...")
        title, selftext = fetch_reddit_data()
        if title is not None and selftext is not None:
            message = f"New post on r/Diablo4:\n\n**{title}**\n```{selftext}```"
            for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).send_messages:
                        await channel.send(message)
                        break  # Only send message to the first channel where the bot can send messages
        else:
            print("No new posts found.")

    client.run(TOKEN)
