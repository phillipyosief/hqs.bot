# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

"""
NOTE:
The channel IDs are from hqs.bot server
"""

from discord.ext import commands
import botsetup

bot = commands.Bot(command_prefix='hqs.bot')
bot.remove_command('help')

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
            f'Mode: Server\n'
            f'---Logs---------------------------------------------------------\n ')
      print('[i] Edit Serverchannels (Guilds, Prefix, Commands, Members)')
      while True:
            channel = bot.get_channel(726219856319479889)
            await channel.edit(reason='Editing Guilds', name='Guilds: {}'.format(len(bot.guilds)))
            channel = bot.get_channel(726219924367999007)
            await channel.edit(reason='Editing Commands', name='Commands: {}'.format(len(bot.commands)))
            channel = bot.get_channel(726219986502418452)
            await channel.edit(reason='Editing Prefix', name='Prefix: {}'.format(bot.command_prefix))


botsetup.run(bot)
