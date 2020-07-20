# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
import discord
from discord.ext import commands
from library.cog_text import help_text
from library.cog_info import colors
from library.icons import links
from library.cog_text import about_text as wm
from library.cog_text import help_text as cmd
import setup as botsetup

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *arg):
        f = discord.Embed(color=colors.fun)
        f.set_author(name='Fun', url=botsetup.website, icon_url=links.giveaway_fun)
        f.add_field(name='/genius <song,artist,lyrics>', value='Get lyrics of a song')
        f.add_field(name='/quote', value='Get random quotes', inline=False)
        f.add_field(name='/wyr', value='Play would you rather', inline=False)
        f.add_field(name='/coinflip', value='Flip a coin', inline=False)
        f.add_field(name='/minesweeper', value='Play minesweeper', inline=False)
        f.add_field(name='/rolldice', value='Roll a dice', inline=False)
        f.add_field(name='/ssp', value='Play scissor, stone, paper', inline=False)
        f.add_field(name='/tournament', value='Battle 4 users', inline=False)
        f.set_footer(text=wm.footer)

        m = discord.Embed(color=colors.moderation)
        m.set_author(name='Moderation', url=botsetup.website, icon_url=links.team_moderation)
        m.add_field(name='/ban <user> <reason>', value='Ban a user', inline=False)
        m.add_field(name='/kick <user> <reason>', value='Kick a user', inline=False)
        m.add_field(name='/clear <amount 1-100>', value='Clear messages', inline=False)
        m.add_field(name='/logs <user>', value='View actions from staff', inline=False)
        m.set_footer(text=wm.footer)

        a = discord.Embed(color=colors.lightblue)
        a.set_author(name='About', url=botsetup.website, icon_url=links.account_about)
        a.add_field(name='/about <user>', value='See aboutsection of a user', inline=False)
        a.add_field(name='/createabout <text>', value='Create a aboutsection', inline=False)
        a.add_field(name='/invite', value='See information about this bot', inline=False)
        a.add_field(name='/plus', value='coming soon', inline=False)
        a.add_field(name='/report', value='Report a command', inline=False)
        a.set_footer(text=wm.footer)

        t = discord.Embed(color=colors.tools)
        t.set_author(name='Tools', url=botsetup.website, icon_url=links.tools)
        t.add_field(name='/avatar <user>', value='Get avatar of a user', inline=False)
        t.add_field(name='/color <hex color>', value='See color', inline=False)
        t.add_field(name='/qrcode', value='Type /qrcode to see how to use /qrcode', inline=False)
        t.add_field(name='/roleinfo <role>', value='View infos about a role', inline=False)
        t.add_field(name='/userinfo <user>', value='View infos about a user', inline=False)
        t.add_field(name='/weather <city>', value='Get the weather', inline=False)
        t.add_field(name='/wikipedia <article>', value='Get a wikipedia article', inline=False)
        t.add_field(name='/survey <topic>', value='Create a survey', inline=False)
        t.add_field(name='/shorturl <url>', value='Short a url with TinyURl')
        t.add_field(name='/checkiban <iban>', value='Check iban')
        t.set_footer(text=wm.footer)

        mu = discord.Embed(color=colors.music)
        mu.set_author(name='Music', url=botsetup.website, icon_url=links.music)
        mu.add_field(name='/join', value='Join a voicechannel', inline=False)
        mu.add_field(name='/leave', value='Leave a voicechannel', inline=False)
        mu.add_field(name='/play <song>', value='Play a song from YouTube', inline=False)
        mu.add_field(name='/karaoke <song>', value='Get the lyrics while playing the song', inline=False)
        mu.add_field(name='/pause', value='Pause music', inline=False)
        mu.add_field(name='/resume', value='Resume music', inline=False)
        mu.add_field(name='/stop', value='Stop music', inline=False)
        mu.add_field(name='/volume <amount 1-100>', value='Change the volume', inline=False)
        mu.set_footer(text=wm.footer)

        o = discord.Embed(color=colors.owner)
        o.set_author(name='Owner', url=botsetup.website, icon_url=links.owner)
        o.add_field(name='/news <#channel> <text>', value='Sending messages to channel')
        o.set_footer(text=wm.footer)

        if arg == ():
            await ctx.send(embed=help_text.help_embed())
        elif arg[0].lower() == 'fun':
            await ctx.send(embed=f)
        elif arg[0].lower() == 'tools':
            await ctx.send(embed=t)
        elif arg[0].lower() == 'music':
            await ctx.send(embed=mu)
        elif arg[0].lower() == 'about':
            await ctx.send(embed=a)
        elif arg[0].lower() == 'owner':
            await ctx.send(embed=o)
        elif arg[0].lower() == 'moderation':
            await ctx.send(embed=m)
        elif arg[0].lower() == 'all':
            await ctx.send(embed=f)
            await ctx.send(embed=t)
            await ctx.send(embed=mu)
            await ctx.send(embed=a)
            await ctx.send(embed=o)
            await ctx.send(embed=m)
        else:
            await ctx.send(embed=help_text.help_embed())


def setup(bot):
    bot.add_cog(Help(bot))
