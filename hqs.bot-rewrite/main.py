# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import discord
from discord.ext import commands
import botsetup
import asyncio
import bs_def


bot = commands.Bot(command_prefix=botsetup.prefix)



@bot.event
async def on_ready():
    print(f'----------------------------------------------------------------\n'
          f' ▄ .▄.▄▄▄  .▄▄ ·  ▄▄▄· ▄▄▄  ▄▄▄▄▄▄▄▌ ▐ ▄▌      ▄▄▄  ▄ •▄ .▄▄ · \n'
          f'██▪▐█▐▀•▀█ ▐█ ▀. ▐█ ▀█ ▀▄ █·•██  ██· █▌▐█▪     ▀▄ █·█▌▄▌▪▐█ ▀. \n'
          f'██▀▐██▌·.█▌▄▀▀▀█▄▄█▀▀█ ▐▀▀▄  ▐█.▪██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐▀▀▄·▄▀▀▀█▄\n'
          f'██▌▐▀▐█▪▄█·▐█▄▪▐█▐█ ▪▐▌▐█•█▌ ▐█▌·▐█▌██▐█▌▐█▌.▐▌▐█•█▌▐█.█▌▐█▄▪▐█\n'
          f'▀▀▀ ··▀▀█.  ▀▀▀▀  ▀  ▀ .▀  ▀ ▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀·▀  ▀ ▀▀▀▀ \n'
          f'---Info---------------------------------------------------------\n'
          f'Name: {bot.user.name}#{bot.user.discriminator}\n'
          f'ID: {bot.user.id}\n'
          f'ServerCount: {len(bot.guilds)}\n'
          f'Commands: {len(bot.commands)}\n'
          f'Activity: {bot.activity}\n'
          f'Prefix: {bot.command_prefix}\n'
          f'Cogs: {cogs}\n'
          f'---Logs---------------------------------------------------------\n ')
    if botsetup.default == True:
        while True:
            invite = discord.Game(name=botsetup.activity1)
            vote = discord.Game(name=botsetup.activity2)
            beta = discord.Game(name=botsetup.activity3)
            update = discord.Game(name=botsetup.activity4)
            help = discord.Game(name=f'in {len(bot.guilds)} Servers | hqsartworks.me')
            await bot.change_presence(activity=invite)
            await asyncio.sleep(5)
            await bot.change_presence(activity=vote)
            await asyncio.sleep(5)
            await bot.change_presence(activity=beta)
            await asyncio.sleep(5)
            await bot.change_presence(activity=update)
            await asyncio.sleep(5)
            await bot.change_presence(activity=help)
    if botsetup.developing == True:
        custom = discord.Game(name='/invite | working on v2.8',)
        await bot.change_presence(activity=custom)

bs_def.discord_info()
bot.owner_id = botsetup.ownerid

bot.remove_command('help')

cogs = [
    'command', 'about', 'fun', 'general', 'moderation', 'music', 'owner', 'tools', 'help', 'changelogs', 'servercommands', 'games'
]

"""Load Cogs"""
for cog in cogs:
    bot.load_extension(f'cogs.{cog}')

botsetup.run(bot)