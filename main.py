#!/usr/bin/env python3

import discord
import json
import asyncio

from discord.ext import commands

file = open('config.json', 'r')
config = json.load(file)

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': 'vn'}
YDL_OPTIONS = {'format': 'bestaudio', 'extractaudio': True, 'audioformat' : 'mp3'}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(config['prefix'], intents=intents)
bot.remove_command('help')

async def start_bot():
    bot = commands.Bot(command_prefix='-', intents=discord.Intents.all(), help_command=None)
    await bot.load_extension('help_cog')
    await bot.load_extension('music_cog')
    return bot

if __name__ == '__main__':
    bot = asyncio.run(start_bot())
    bot.run(config['token'])