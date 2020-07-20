# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
import discord
from discord.ext import commands
import setup
import asyncio
import logging

if setup.developing == True:
    bot = commands.Bot(command_prefix=setup.test_prefix)

if setup.developing == False:
    bot = commands.Bot(command_prefix=setup.prefix)

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
    if setup.default == True:
        while True:
            invite = discord.Game(name=setup.activity1)
            vote = discord.Game(name=setup.activity2)
            beta = discord.Game(name=setup.activity3)
            update = discord.Game(name=setup.activity4)
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
            await asyncio.sleep(5)
    if setup.developing == True:
        custom = discord.Game(name='/invite | working on v3.0',)
        await bot.change_presence(activity=custom)



if setup.discord_info == True:
    logging.basicConfig(level=logging.INFO)
if setup.discord_info == False:
    pass

bot.owner_id = setup.ownerid
bot.remove_command('help')

cogs = [
    'about', 'fun', 'moderation', 'music',
    'owner', 'tools', 'games', 'addons', 'help'
]

for cog in cogs:
    bot.load_extension(f'cogs.{cog}')

setup.run(bot)