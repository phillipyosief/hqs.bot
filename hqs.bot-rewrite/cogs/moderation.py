# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
from cog_info import colors
import discord
from discord.ext import commands
import botsetup
import errorembed

blue = colors.blue
black = colors.black
yellow = colors.yellow
white = colors.white
green = colors.green
grey = colors.grey
darkgrey = colors.darkgrey
red = colors.red
purple = colors.purple
pink = colors.pink
lightblue = colors.lightblue
lightgreen = colors.lightgreen
orange = colors.orange

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
        except Exception as e:
            failban = discord.Embed(title=f'Failed to ban {target}', description=f'Error: ```{e}```\n'
                                                                                 '´/ban <@member>´\n',
                                    color=red)
            failban.set_footer(text=watermark)
            await ctx.send(embed=failban)

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
        except Exception as e:
            timeout = discord.Embed(title='Error',
                                    description=f'```{e}```',
                                    color=red)
            timeout.set_footer(text=watermark)
            await ctx.send(embed=timeout)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, target: discord.Member):
        try:
            await target.kick()
            kick = discord.Embed(title=f"kicked: {target}", description="To see more write /help team", color=0xe10005)
            await ctx.send(embed=kick)
            kick.set_footer(text="hqs.bot ∫ by phillip.hqs")
        except Exception as e:
            failkick = discord.Embed(title=f'Failed to kick {target}', description=f'Error: ```{e}```\n'
                                                                                   '´/kick <@member> <reason>´\n',
                                     color=botsetup.error)
            failkick.set_footer(text="hqs.bot ∫ by phillip.hqs")
            await ctx.send(embed=failkick)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=errorembed.noperm)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=errorembed.noperm)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=errorembed.noperm)

def setup(bot):
    bot.add_cog(moderation(bot))