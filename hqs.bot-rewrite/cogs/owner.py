# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
from cog_info import colors
from discord.ext import commands
import errorembed
import discord

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

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def news(self, ctx, channel: discord.TextChannel, *, args):
        y = discord.Embed(title='Successful sending!', description=f'Your Message:\n'
                                                                   f'``{args}``\n'
                                                                   f'Channel: {channel}', color=green)
        y.add_field(name='Your message', value=f'``{args}``', inline=False)
        y.add_field(name='TextChannel', value=f'Name: {channel}\n'
                                              f'Category: {channel.category}\n'
                                              f'Position: {channel.position}\n'
                                              f'ID: {channel.id}\n'
                                              f'CategoryID: {channel.category_id}\n', inline=True)
        y.set_footer(text=watermark)
        await ctx.send(embed=y)
        await channel.send(f'{args}')

    @news.error
    async def news_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=errorembed.noperm)

def setup(bot):
    bot.add_cog(owner(bot))