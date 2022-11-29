from api_key import *
import os
import openai

openai.api_key = OPENAI_KEY
completion = openai.Completion()
chat_log = '''Human: Salut, comment tu vas ?
AI: Je vais bien. Comment je peux t'aider ?
'''
def ask(question, chat_log):
    response = completion.create(
        prompt=f'{chat_log}Human: {question}\nAI:',
        engine='davinci',
        stop=['\nHuman'],
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        best_of=1,
        max_tokens=150
    )
    return response.choices[0].text.strip()
while True:
    question = input('Human:')
    chat_log = f'{chat_log}Human: {question}\n'
    answer = ask(f'Human:{question}', chat_log)
    print(answer)
    chat_log = f'{chat_log}AI: {answer}\n'