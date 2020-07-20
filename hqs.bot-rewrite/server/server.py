# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
from discord.ext import commands
import setup

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
          if setup.display_server == True:
            channel = bot.get_channel(setup.display_server_channel)
            await channel.edit(reason='Editing Guilds', name='Guilds: {}'.format(len(bot.guilds)))
          elif setup.display_commands == True:
            channel = bot.get_channel(setup.display_commands_channel)
            await channel.edit(reason='Editing Commands', name='Commands: {}'.format(len(bot.commands)))
          elif setup.display_prefix == True:
            channel = bot.get_channel(setup.display_prefix_channel)
            await channel.edit(reason='Editing Prefix', name='Prefix: {}'.format(bot.command_prefix))
          elif setup.display_members == True:
            channel = bot.get_channel(setup.display_members_channel)
            await channel.edit(reason='Editing Members', name='Members: {}'.format(bot.command_prefix))

@bot.event
async def on_member_join():
    try:
        channel = bot.get_channel(setup.display_members_channel)
        await channel.edit(reason='Editing Members', name='Members: {}'.format(bot.get_all_members()))
    except Exception as e:
        print(f'[error] {e}')

setup.run(bot)