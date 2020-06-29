# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
from cog_info import colors
import discord
from discord.ext import commands
import errorembed
import botsetup

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

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx: commands.Context, *arg):
        t = True
        f = False

        def hlembed():
            hl = discord.Embed(title='Hilfe:', color=lightblue)
            hl.add_field(name='FUN', value='Minigames commands and other fun commands')
            hl.add_field(name='TOOLS', value='Commands for tools like Wikipedia')
            hl.add_field(name='MUSIC', value='Music commands')
            hl.add_field(name='ABOUT', value='About the bot and server')
            hl.add_field(name='OWNER', value='Commands for the owner')
            hl.add_field(name='GENERAL', value='General commands')
            hl.add_field(name='MODERATION', value='Commands for the moderators')
            hl.set_footer(text='Type /help all to see all commands')
            return hl

        if arg == ():
            await ctx.send(embed=hlembed())
        elif arg[0].lower() == 'general':
            general = discord.Embed(title='General⚙', color=lightblue)
            general.add_field(name='/feedback <text>', value='Send feedback to the bot developer', inline=t)
            general.add_field(name='/create <text>', value='create embed', inline=t)
            await ctx.send(embed=general)
        elif arg[0].lower() == 'fun':
            fun = discord.Embed(title='Fun🕹', color=pink)
            fun.add_field(name='/battle <@user> <@user>', value='Battle other user', inline=t)
            fun.add_field(name='/pokemonbattle <@user> <@user>', value='Start a pokemonbattle', inline=f)
            fun.add_field(name='/tournament <@user> <@user> <@user> <@user>', value='Battle with 4 users', inline=t)
            fun.add_field(name='/coinflip', value='Flip an coin', inline=f)
            fun.add_field(name='/minesweeper', value='Play minesweeper', inline=t)
            #fun.add_field(name='/gif <text or tags>', value='Send gif', inline=f)
            fun.add_field(name='/rolldice', value='Roll a dice', inline=t)
            fun.add_field(name='/tweet <text>', value='Send a tweet (@alphaclanc)', inline=f)
            fun.add_field(name='/quote', value='Send a quote', inline=t)
            fun.add_field(name='/addquote <quote>', value='Add a quote to list', inline=f)
            fun.add_field(name='/genius <song,artist,songtext>', value='Send a song lyric', inline=t)
            await ctx.send(embed=fun)
        elif arg[0].lower() == 'moderation':
            moderation = discord.Embed(title='Moderation🚨', color=blue)
            moderation.add_field(name='/ban <@user>', value='Ban an user', inline=t)
            moderation.add_field(name='/kick <@user>', value='Kick an user', inline=f)
            moderation.add_field(name='/clear <amount>', value='Clear messages')
            await ctx.send(embed=moderation)
        elif arg[0].lower() == 'about':
            about = discord.Embed(title='About👤', color=orange)
            about.add_field(name='/about <@user>', value='See the about text', inline=f)
            about.add_field(name='/createabout', value='Create a about text', inline=f)
            await ctx.send(embed=about)
        elif arg[0].lower() == 'tools':
            tools = discord.Embed(title='Tools🛠', color=grey)
            tools.add_field(name='/user <@user>', value='See infos about a user', inline=f)
            tools.add_field(name='/role <@role>', value='See infos about a role', inline=f)
            tools.add_field(name='/role <@role> permissions', value='See permission from the role', inline=f)
            tools.add_field(name='/textchannel <#channel>', value='See infos about a textchannel', inline=f)
            tools.add_field(name='/voicechannel <voicechannel>', value='See infos about a voicechannel', inline=f)
            tools.add_field(name='/weather <city>', value='Check weather', inline=t)
            tools.add_field(name='/wikipedia <article>', value='Show you a Wikipedia article', inline=f)
            tools.add_field(name='/checkiban <iban>', value='Check if the number is verified (only German IBAN numbers)', inline=f)
            tools.add_field(name='/qrcode', value='type /qrcode to see how to use /qrcode', inline=f)
            tools.add_field(name='/shorturl <url>', value='Currently not available because the API is broken we will fix it', inline=f)
            await ctx.send(embed=tools)
        elif arg[0].lower() == 'music':
            if botsetup.musicna == False:
                music = discord.Embed(title='Music🎶', color=red)
                music.add_field(name='/join', value='Join voicechannel', inline=f)
                music.add_field(name='/leave', value='Leave the voicechannel', inline=t)
                music.add_field(name='/pause', value='Pause music', inline=f)
                music.add_field(name='/stop', value='Stop a music', inline=t)
                music.add_field(name='/radio', value='Play hqsfm radio', inline=f)
                music.add_field(name='/resume', value='Resume music', inline=t)
                music.add_field(name='/play <song,link>', value='Play a song from YouTube', inline=f)
                music.add_field(name='/karaoke <song or artist or songtext>', value='All fun commands', inline=t)
                await ctx.send(embed=music)
            if botsetup.musicna == True:
                await ctx.send(embed=errorembed.nota)
        elif arg[0].lower() == 'owner':
            owner = discord.Embed(title='Owner🔐')
            owner.add_field(name='/news <title> <description>', value='Send a embed')
            await ctx.send(embed=owner)
        elif arg[0].lower() == 'all':
            general = discord.Embed(title='General⚙', color=lightblue)
            general.add_field(name='/feedback <text>', value='Send feedback to the bot developer', inline=t)
            await ctx.send(embed=general)
            fun = discord.Embed(title='Fun🕹', color=pink)
            fun.add_field(name='/userbattle <@user> <@user>', value='Battle other user', inline=t)
            fun.add_field(name='/pokemonbattle <@user> <@user>', value='Start a pokemonbattle', inline=f)
            fun.add_field(name='/tournament <@user> <@user> <@user> <@user>', value='Battle with 4 users', inline=t)
            fun.add_field(name='/coinflip', value='Flip an coin', inline=f)
            fun.add_field(name='/minesweeper', value='Play minesweeper', inline=t)
            fun.add_field(name='/gif <text or tags>', value='Send gif', inline=f)
            fun.add_field(name='/rolldice', value='Roll a dice', inline=t)
            fun.add_field(name='/tweet <text>', value='Send a tweet (@alphaclanc)', inline=f)
            fun.add_field(name='/quote', value='Send a quote', inline=t)
            fun.add_field(name='/addquote <quote>', value='Add a quote to list', inline=f)
            fun.add_field(name='/genius <song,artist,songtext>', value='Send a song lyric', inline=t)

            moderation = discord.Embed(title='Moderation🚨', color=blue)
            moderation.add_field(name='/ban <@user>', value='Ban an user', inline=t)
            moderation.add_field(name='/kick <@user>', value='Kick an user', inline=f)
            moderation.add_field(name='/clear <amount>', value='Clear messages')
            await ctx.send(embed=moderation)
            about = discord.Embed(title='About👤', color=orange)
            about.add_field(name='/about <@user>', value='See the about text', inline=f)
            about.add_field(name='/createabout', value='Create a about text', inline=f)
            await ctx.send(embed=about)
            tools = discord.Embed(title='Tools🛠', color=grey)
            tools.add_field(name='/userinfo <@user>', value='See infos about a user', inline=f)
            tools.add_field(name='/role <@role>', value='See infos about a role', inline=f)
            tools.add_field(name='/weather <city>', value='Check weather', inline=t)
            tools.add_field(name='/wikipedia <theme>', value='Show you a Wikipedia article', inline=f)
            tools.add_field(name='/checkiban <iban>', value='Check if the number is verified (only German IBAN numbers)', inline=f)
            tools.add_field(name='/qrcode', value='type /qrcode to see how to use /qrcode', inline=f)
            tools.add_field(name='/shorturl <url>', value='Currently not available because the API is broken we will fix it', inline=f)
            await ctx.send(embed=tools)
            await ctx.send(embed=fun)
            if botsetup.musicna == False:
                music = discord.Embed(title='Music🎶', color=red)
                music.add_field(name='/join', value='Join voicechannel', inline=f)
                music.add_field(name='/leave', value='Leave the voicechannel', inline=t)
                music.add_field(name='/pause', value='Pause music', inline=f)
                music.add_field(name='/stop', value='Stop a music', inline=t)
                music.add_field(name='/radio', value='Play hqsfm radio', inline=f)
                music.add_field(name='/resume', value='Resume music', inline=t)
                music.add_field(name='/play <song,link>', value='Play a song from YouTube', inline=f)
                music.add_field(name='/karaoke <song or artist or songtext>', value='All fun commands', inline=t)
                await ctx.send(embed=music)
            if botsetup.musicna == True:
                mna = discord.Embed(title='Sorry...', description='The Music commands is currently not available\n'
                                                                  'we will fix it as soon as possible!')
                await ctx.send(embed=mna)
        else:
            await ctx.send(embed=hlembed())


def setup(bot):
    bot.add_cog(help(bot))