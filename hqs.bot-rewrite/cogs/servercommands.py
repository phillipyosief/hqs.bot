# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
import discord
from discord.ext import commands
import botsetup
from cog_info import invite_text, about_text, colors
import subprocess

red = colors.red
bot = commands.Bot(command_prefix=botsetup.prefix)

class servercommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx, args):
        try:
            bot.load_extension(f'cogs.{args}')
            logs = discord.Embed(title='Succes', color=red)
            await ctx.send(embed=logs)
        except Exception as e:
            error = discord.Embed(title='Error:', description=f'```{e}```', color=red)
            await ctx.send(embed=error)

def setup(bot):
    bot.add_cog(servercommands(bot))