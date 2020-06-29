# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import asyncio
import discord
from discord.ext import commands
import botsetup

bot = commands.Bot(command_prefix='hqs.bot')

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
          f'Mode: Logs'
          f'---Logs---------------------------------------------------------\n ')
    print('[i] Storing all informations')



@bot.event
async def on_message(message):
    with open('logs/logs_messages.txt', 'a', encoding="utf-8") as logs:
        logs.write(f'Author: {message.author}\n'
                   f'ID: {message.author.id}\n'
                   f'Server: {message.guild}\n'
                   f'Message:\n'
                   f'{message.content}\n'
                   f' \n')
        logs.close()

@bot.event
async def on_member_join(member):
    try:
        channel = bot.get_channel(726210333185933344)
        await channel.edit(reason='Editing Members count', name='Members: {}'.format(channel.guild.member_count))
        with open('logs/logs_join.txt', 'a', encoding="utf-8") as logs:
            logs.write(f'[+] {member}, {member.guild}\n')
            logs.close()
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_member_remove(member):
    try:
        channel = bot.get_channel(726210333185933344)
        await channel.edit(name='Members: {}'.format(channel.guild.member_count))
        with open('logs/logs_leave.txt', 'a', encoding="utf-8") as logs:
            logs.write(f'[-] {member}, {member.guild}\n')
            logs.close()
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_member_ban(member):
    try:
        channel = bot.get_channel(726210333185933344)
        await channel.edit(name='Members: {}'.format(channel.guild.member_count))
        with open('logs/logs_ban.txt', 'a', encoding="utf-8") as logs:
            logs.write(f'{member}, {member.guild}\n')
            logs.close()
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_member_unban(member):
    try:
        channel = bot.get_channel(726210333185933344)
        await channel.edit(name='Members: {}'.format(channel.guild.member_count))
        with open('logs/logs_unban.txt', 'a', encoding="utf-8") as logs:
            logs.write(f'{member}, {member.guild}\n')
            logs.close()
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_member_delete(member, message):
    try:
        channel = bot.get_channel(726210333185933344)
        await channel.edit(name='Members: {}'.format(channel.guild.member_count))
        with open('logs/logs_delete.txt', 'a', encoding="utf-8") as logs:
            logs.write(f'[-] {member}, {message.content}, {member.guild}\n')
            logs.close()
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_member_edit(before, member, message):
    try:
        channel = bot.get_channel(726210333185933344)
        await channel.edit(name='Members: {}'.format(channel.guild.member_count))
        with open('logs/logs_edit.txt', 'a', encoding="utf-8") as logs:
            logs.write(f'Before: \n'
                       f'{member}, {message.content}, {member.guild}\n')
            logs.close()
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_member_edit(after, member, message):
    try:
        channel = bot.get_channel(726210333185933344)
        await channel.edit(name='Members: {}'.format(channel.guild.member_count))
        with open('logs/logs_edit.txt', 'a', encoding="utf-8") as logs:
            logs.write(f'After: \n'
                       f'{member}, {message.content}, {member.guild}\n')
            logs.close()
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_error(exception, error, message):
    try:
        general_error = discord.Embed(title='Error:', description=f'``{error}``\n'
                                                              f'```{exception}```\n', color=0xff2121)
        general_error.set_thumbnail(url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif')
        await message.channel.send(embed=general_error)
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_command_error(exception, error, message):
    try:
        general_error = discord.Embed(title='Error:', description=f'``{error}``\n'
                                                                  f'```{exception}```\n', color=0xff2121)
        general_error.set_thumbnail(url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif')
        await message.channel.send(embed=general_error)
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_guild_join(invite, member):
    try:
        with open('logs/logs_guild_join.txt', 'a', encoding="utf-8") as logs:
            logs.write(f'[+] {member}, {invite.url}, {member.guild}\n')
            logs.close()
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_guild_remove(member):
    try:
        with open('logs/logs_guild_remove.txt', 'a', encoding="utf-8") as logs:
            logs.write(f'[-] {member}, {member.guild}\n')
            logs.close()
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_guild_role_delete(role):
    try:
        with open('logs/logs_guild_role.txt', 'a', encoding="utf-8") as logs:
            logs.write(f'[*] {role.permissions.value}, {role}, {role.guild}\n')
            logs.close()
    except Exception as e:
        print(f'[error] {e}')

@bot.event
async def on_guild_role_update(role):
    try:
        with open('logs/logs_guild_role.txt', 'a', encoding="utf-8") as logs:
            logs.write(f'[*] {role.permissions.value}, {role}, {role.guild}\n')
            logs.close()
    except Exception as e:
        print(f'[error] {e}')

bot.remove_command('help')




botsetup.run(bot)
