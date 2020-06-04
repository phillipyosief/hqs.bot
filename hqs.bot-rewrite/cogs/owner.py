# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import asyncio
import random
import unicodedata
import time
import random
import re
from urllib.request import urlopen
import discord
import lyricsgenius
import requests
# import tenorpy
import tweepy
import wikipedia
from discord.ext import commands
import botsetup

# colors
blue = 0x0062ff
black = 0x000000
yellow = 0xf5ff30
white = 0xffffff
green = 0x21ff55
grey = 0x636363
darkgrey = 0x1c1c1c
red = 0xff2121
purple = 0xb338ff
pink = 0xff47e0
lightblue = 0x4778ff
lightgreen = 0x73ffad
orange = 0xff9757

watermark = "hqs.bot / by phillip.hqs"

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def news(self, ctx, channel: discord.TextChannel, *, args):
        y = discord.Embed(title='Successful sending!', description=f'Your Message:\n'
                                                                   f'``{args}``\n'
                                                                   f'Channel: {channel}', color=green)
        y.add_field(name='Your message', value=f'``{args}``')
        y.add_field(name='TextChannel', value=f'Name: {channel}\n'
                                              f'Category: {channel.category}\n'
                                              f'Position: {channel.position}\n'
                                              f'ID: {channel.id}\n'
                                              f'CategoryID: {channel.category_id}\n')
        y.set_footer(text=watermark)
        await ctx.send(embed=y)
        await channel.send(f'{args}')

    @news.error
    async def news_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=botsetup.noperm)

def setup(bot):
    bot.add_cog(owner(bot))