import discord
import os
from dotenv import load_dotenv

# Other .py files
import responses

load_dotenv()

async def send_message(msg, content, is_private):
    try:
        response = responses.handle_response(content)
        await msg.author.send(response) if is_private else await msg.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = os.getenv("TOKEN")


    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


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


    client.run(TOKEN)
