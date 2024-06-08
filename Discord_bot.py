import discord
import os
import openai

load_dotenv()

token = os.getenv("TOKEN")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# chat = ""

with open("Chat1.txt","r") as f:
    chat = f.read()

# file = input("Enter 1, 2 or 3 for loading the chat:\n")

# match(file):
#     case "1":
#         file = "Chat1.txt"
#     case "2":
#         file = "chat2.txt"
#     case "3":
#         file = "chat3.txt"
#     case _:
#         print("Invalid...")


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        global chat
        
        chat += f"{message.author} : {message.content}\n"
        print(f"Message from {message.author} : {message.content}")
        
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            
        
        
            
        if self.user != message.author:
            if self.user in message.mentions:
                print(chat)
                channel = message.channel
                await channel.send('Hello, i am sira!')
            
                response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"{chat}\nSira: ",
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
                messageToSend = response.choices[0].text
                await channel.send(messageToSend)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)