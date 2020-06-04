# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import discord
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

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, target: discord.Member or discord.Guild):
        try:
            ban = discord.Embed(title=f'Banned {target}', description='explore more commands with /help', color=0xe10005)
            ban.set_footer(text=watermark)
            await target.ban()
            await ctx.send(embed=ban)
        except:
            failban = discord.Embed(title=f'Failed to ban {target}', description='Please give a Reason or Member\n'
                                                                                 '´/ban <@member>´\n',
                                    color=botsetup.error)
            failban.set_footer(text=watermark)
            await ctx.send(embed=failban)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=botsetup.noperm)


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def clear(self, ctx, amount=100):
        try:
            channel = ctx.message.channel
            messages = []
            async for message in channel.history(limit=amount):
                messages.append(message)
            await channel.delete_messages(messages)
            await ctx.send('Messaged deleted')
        except:
            timeout = discord.Embed(title='Check your Permissons!',
                                    description='If you have the permissions. Try the command later.',
                                    color=botsetup.error)
            timeout.set_footer(text=watermark)
            await ctx.send(embed=timeout)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=botsetup.noperm)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, target: discord.Member):
        try:
            await target.kick()
            kick = discord.Embed(title=f"kicked: {target}", description="To see more write /help team", color=0xe10005)
            await ctx.send(embed=kick)
            kick.set_footer(text="hqs.bot ∫ by phillip.hqs")
        except:
            failkick = discord.Embed(title=f'Failed to kick {target}', description='Please give a Reason or Member\n'
                                                                                   '´/kick <@member> <reason>´\n',
                                     color=botsetup.error)
            failkick.set_footer(text="hqs.bot ∫ by phillip.hqs")
            await ctx.send(embed=failkick)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=botsetup.noperm)

def setup(bot):
    bot.add_cog(moderation(bot))