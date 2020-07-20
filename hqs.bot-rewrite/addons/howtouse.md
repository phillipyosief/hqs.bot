##How to use addons
1. Put your addon files in the `Addons` directory
1. Write `/load_addon addonname`
1. To remove a Addon just write `/unload_addon addonname`

###Requirements
Your Python file need to be an cog like this:

`````python
from discord.ext import commands
import discord

author = 'MyName'
title = 'AddonTitle'
description = 'AddonDescription'

class MyNewAddon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send('Successful')

def setup(bot):
    bot.add_cog(MyNewAddon(bot))
`````

Read more about [Discord Cogs](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html)