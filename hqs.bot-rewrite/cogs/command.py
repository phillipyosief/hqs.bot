from discord.ext import commands


class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# coming soon!

def setup(bot):
    bot.add_cog(commands(bot))
