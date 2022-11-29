# This example requires the 'message_content' intent.
from api_key import *
import os
import openai
import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

def ask(question, chat_log):
    response = completion.create(
        prompt=f'{chat_log}Human: {question}\nAI:',
        engine='davinci',
        stop=['\nHuman'],
        temperature=0,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        best_of=1,
        max_tokens=150
    )
    return response.choices[0].text.strip()

openai.api_key = OPENAI_KEY
completion = openai.Completion()
chat_log = '''Human: Salut, comment tu vas ?
AI: Je vais bien. Comment je peux t'aider ?
'''

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global chat_log
    if message.author == client.user:
        return
    question = message.content
    chat_log = f'{chat_log}Human: {question}\n'
    answer = ask(f'Human:{question}', chat_log)
    await message.channel.send(answer)
    chat_log = f'{chat_log}AI: {answer}\n'

client.run(os.getenv("TOKEN"))