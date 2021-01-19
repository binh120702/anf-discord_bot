import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

hello_words = ['hello', 'ohyo', 'd2o2']
hello_responses = ['lo cc', 'ohyo', 'O2O', 'O3O', 'oh hello']

stop_words = ['dodo', 'uit', 'idol', 'xinh', 'mlem']
stop_responses = ['stop it', 'pls']

invite_words = ['uoc', 'vo', 'vao', 'coming']
invite_responses = ['uoc too', 'uoc +1']

twit_words = ['cc', 'cut', 'wtf']
twit_responses = [':<', 'hjx', 'haiz', 'pici dep trai siu cap vu tru']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if any(word in msg for word in hello_words):
        await message.channel.send(random.choice(hello_responses))
    if any(word in msg for word in stop_words):
        await message.channel.send(random.choice(stop_responses))
    if any(word in msg for word in invite_words):
        await message.channel.send(random.choice(invite_responses))
    if any(word in msg for word in twit_words):
        await message.channel.send(random.choice(twit_responses))

keep_alive()
client.run(os.getenv('TOKEN'))