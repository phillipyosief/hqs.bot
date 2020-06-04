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
import json
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

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def feedback(self, ctx, *, args):
        try:
            fb = open(f'feedback_{ctx.author}', 'w')
            fb.write(f'{args}')
            fb.close()
            sfb = discord.Embed(title='Sending Feedback')
            await ctx.send(embed=sfb)
        except:
            nfb = discord.Embed(title='Please write a text', description='explore more commands with ```/help``')
            await ctx.send(embed=nfb)

    @feedback.error
    async def feedback_error(self, ctx, error):
        await ctx.send(embed=botsetup.noargs)

    @commands.command()
    async def create(self, ctx, arg1, *, args):
        embed = discord.Embed(title=arg1, description=args, color=orange)
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        embed.set_footer(text='Custom user message / hqs.bot')
        await ctx.send(embed=embed)

    @create.error
    async def create_error(self, ctx, error):
        await ctx.send(embed=botsetup.noargs)



    @commands.command()
    async def role(self, ctx, role: discord.Role, *arg):
        if arg == ():
            role1 = discord.Embed(title=f'Role: {role.name}', color=role.color)
            role1.add_field(name=f'ID',          value=f'{role.id}')
            role1.add_field(name=f'Hierarchy',   value=f'{role.position}')
            role1.add_field(name=f'Created at', value=f'{role.created_at}')
            role1.add_field(name=f'Color',       value=f'{role.color}')
            role1.add_field(name=f'Members', value=f'{len(role.members)}')
            role1.add_field(name=f'Permissions value', value=f'{role.permissions.value}')
            role1.add_field(name=f'Mentionable', value=f'{role.mentionable}')
            role1.add_field(name=f'Meniton',          value=f'{role.mention}')
            role1.set_footer(text='type /role help to see more')
            await ctx.send(embed=role1)
        elif arg[0].lower() == 'permissions':
            perm = discord.Embed(title=f'Role: {role.name}', color=role.color)
            perm.add_field(name='add_reactions', value=f'{role.permissions.add_reactions}\n')
            perm.add_field(name='administrator', value=f'{role.permissions.administrator}\n')
            perm.add_field(name='attach_files', value=f'{role.permissions.attach_files}\n')
            perm.add_field(name='ban_members', value=f'{role.permissions.ban_members}\n')
            perm.add_field(name='change_nickname', value=f'{role.permissions.change_nickname}\n')
            perm.add_field(name='connect', value=f'{role.permissions.connect}\n')
            perm.add_field(name='create_instant_invite', value=f'{role.permissions.create_instant_invite}\n')
            perm.add_field(name='deafen_members', value=f'{role.permissions.deafen_members}\n')
            perm.add_field(name='embed_links', value=f'{role.permissions.embed_links}\n')
            perm.add_field(name='external_emojis', value=f'{role.permissions.external_emojis}\n')
            perm.add_field(name='general', value=f'{role.permissions.attach_files}\n')
            perm.add_field(name='kick_members', value=f'{role.permissions.kick_members}\n')
            perm.add_field(name='manage_channels', value=f'{role.permissions.manage_channels}\n')
            perm.add_field(name='manage_emojis', value=f'{role.permissions.manage_emojis}\n')
            perm.add_field(name='manage_guild', value=f'{role.permissions.manage_guild}\n')
            perm.add_field(name='manage_messages', value=f'{role.permissions.manage_messages}\n')
            perm.add_field(name='manage_nicknames', value=f'{role.permissions.manage_nicknames}\n')
            perm.add_field(name='manage_permissions', value=f'{role.permissions.manage_permissions}\n')
            perm.add_field(name='manage_roles', value=f'{role.permissions.manage_roles}\n')
            perm.add_field(name='manage_webhooks', value=f'{role.permissions.manage_webhooks}\n')
            perm.add_field(name='mention_everyone', value=f'{role.permissions.mention_everyone}\n')
            perm.add_field(name='add_reactions', value=f'{role.permissions.add_reactions}\n')
            perm.add_field(name='move_members', value=f'{role.permissions.move_members}\n')
            perm.add_field(name='value', value=f'{role.permissions.value}\n')
            perm.set_footer(text='type /role help to see more')
            await ctx.send(embed=perm)
        elif arg[0].lower() == 'members':
            await ctx.send(embed=botsetup.nota)
            #member = discord.Embed(title=f'Role: {role.name}', color=role.color)
            #count = len(role.members)
            #all = role.members.pop(count)
            #member.add_field(name=f'Members', value=f'{all}\n')
            #member.set_footer(text='type /role help to see more')
            #await ctx.send(embed=member)

    @role.error
    async def role_error(self, ctx, error):
        await ctx.send(embed=botsetup.norole)


    @commands.command()
    async def textchannel(self, ctx, channel: discord.TextChannel):
        txt = discord.Embed(title=f'TextChannel: {channel.name}', color=orange)
        txt.add_field(name=f'ID', value=f'{channel.id}')
        txt.add_field(name=f'Hierarchy', value=f'{channel.position}')
        txt.add_field(name=f'Created at', value=f'{channel.created_at}')
        txt.add_field(name=f'Category', value=f'{channel.category}')
        txt.add_field(name=f'Category ID', value=f'{channel.category_id}')
        txt.add_field(name=f'Members', value=f'{len(channel.members)}')
        txt.add_field(name=f'Meniton', value=f'{channel.mention}')
        txt.add_field(name=f'Last message ID', value=f'{channel.last_message_id}')
        txt.add_field(name=f'Slowmode', value=f'{channel.slowmode_delay}')
        txt.set_footer(text='type /channel help to see more')
        await ctx.send(embed=txt)

    @textchannel.error
    async def textchannel_error(self, ctx, error):
        await ctx.send(embed=botsetup.nochan)

    @commands.command()
    async def voicechannel(self, ctx, *, channel: discord.VoiceChannel):
        voice = discord.Embed(title=f'VoiceChannel: {channel.name}', color=orange)
        voice.add_field(name=f'ID', value=f'{channel.id}')
        voice.add_field(name=f'Hierarchy', value=f'{channel.position}')
        voice.add_field(name=f'Created at', value=f'{channel.created_at}')
        voice.add_field(name=f'Category', value=f'{channel.category}')
        voice.add_field(name=f'Category ID', value=f'{channel.category_id}')
        voice.add_field(name=f'Members', value=f'{len(channel.members)}')
        voice.add_field(name=f'Meniton', value=f'{channel.mention}')
        voice.add_field(name=f'Userlimit', value=f'{channel.user_limit}')
        voice.add_field(name=f'Bitrate', value=f'{channel.bitrate}')
        voice.set_footer(text='type /help to see more')
        await ctx.send(embed=voice)

    @voicechannel.error
    async def voicechannel_error(self, ctx, error):
        await ctx.send(embed=botsetup.nochan)








def setup(bot):
    bot.add_cog(general(bot))