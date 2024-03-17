import os
from typing import Final
from discord import Intents, Client, Message
from dotenv import load_dotenv
from response import get_response

# STEP 0: Load Token From Secure Enviroment
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: Load Bot
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# STEP 2: Message Functionality
async def send_messsage(message: Message, user_message: str) -> None:
    if not user_message:
        print("(Message was empty because intent were not enabled)")
        return
    if is_private := user_message[0] == "?":
        user_message = user_message[1:]
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as error:
        print(error)

# STEP 3: Handling STARTUP for our bot.quit
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running")

# STEP 4: Handling Incoming Messages
@client.event
async def on_messsage(message: Message) -> None:
    if Message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    await send_messsage(message, user_message)

# STEP 5: Main Entry Point
def main() -> None:
    client.run(token=TOKEN)
    
if __name__ == '__main__':
    main()