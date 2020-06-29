# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
from discord.ext import commands
import botsetup

class changelogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def changelogs(self, ctx):
        print(changelogs + botsetup.version + changelogs.embed)
        await ctx.send(embed=changelogs + botsetup.version)


    @commands.command()
    async def o(self, ctx):
        await ctx.send('hi')

def setup(bot):
    bot.add_cog(changelogs(bot))