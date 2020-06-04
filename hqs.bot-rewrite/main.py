# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import logging
import discord
from discord.ext import commands
import botsetup
import asyncio

bot = commands.Bot(command_prefix=botsetup.prefix)
logging.basicConfig(level=logging.INFO)
bot.owner_id = botsetup.ownerid
if botsetup.help == True:
    pass
if botsetup.help == False:
    bot.remove_command('help')



@bot.event
async def on_ready():
    if botsetup.default == True:
        while True:
            invite = discord.Game(name='/invite | hqsartworks.me')
            vote = discord.Game(name='vote.hqsartworks.me')
            beta = discord.Game(name='get beta beta.hqsartworks.me')
            update = discord.Game(name='New update v2.3 | hqsartworks.me')
            help = discord.Game(name='/help | hqsartworks.me')
            await bot.change_presence(activity=invite)
            await asyncio.sleep(10)
            await bot.change_presence(activity=vote)
            await asyncio.sleep(10)
            await bot.change_presence(activity=beta)
            await asyncio.sleep(10)
            await bot.change_presence(activity=update)
            await asyncio.sleep(10)
            await bot.change_presence(activity=help)
    if botsetup.developing == True:
        custom = discord.Game(name='/invite | working on v2.3',)

        await bot.change_presence(activity=custom)


    if botsetup.newversion == True:
        invite = discord.Embed(description=f'[Invite]({botsetup.invite}) | '
                                       f'[Donate](https://www.tipeeestream.com/hqsartworks/donation) | [GitHub]({botsetup.github}) | '
                                       f'[Website]({botsetup.website}) | [Support Server]({botsetup.support_dc})\n'
                                       f'Scan QRCode to invite\n'
                                       f'by phillip.hqs', color=0x74332)
        invite.set_author(name='hqs.bot#8761', icon_url=botsetup.botlogo)
        invite.set_thumbnail(
            url='https://media.discordapp.net/attachments/625231860250968094/715998947927392266/qr.png%27')
        await bot.get_all_channel().send(embed=invite)
        botsetup.quick_log()
    for guild in bot.guilds:
        print(f'Name: {guild.name}, ID: {guild.id}')


if botsetup.help == True:
    cogs = [
        'command', 'about', 'fun', 'general', 'moderation', 'music', 'owner', 'tools'
    ]
if botsetup.help == False:
    cogs = [
        'command', 'about', 'fun', 'general', 'moderation', 'music', 'owner', 'tools', 'help'
    ]

print(cogs)
"""Load Cogs"""
for cog in cogs:
    bot.load_extension(f'cogs.{cog}')

"""Start Bot"""
botsetup.run(bot)
