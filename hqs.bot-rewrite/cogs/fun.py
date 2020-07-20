# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
import discord
from discord.ext import commands
from library.cog_info import quotes as quotes
from library.cog_info import colors, wouldyourather
from library.icons import links
from library.cog_text import about_text as wm
from library.error_embeds import embeds
import random
import json
import setup as botsetup
import requests
import lyricsgenius


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        try:
            quote = [quotes.quote_1,
                     quotes.quote_2,
                     quotes.quote_3,
                     quotes.quote_4,
                     quotes.quote_5,
                     quotes.quote_6,
                     quotes.quote_7,
                     quotes.quote_8,
                     quotes.quote_9,
                     quotes.quote_10]
            quote = discord.Embed(description=f'{random.choice(quote)}', color=colors.lightgreen)
            quote.set_footer(text=wm.footer)
            quote.set_author(name='Quotes', url=botsetup.website, icon_url=links.quote)
            await ctx.send(embed=quote)
        except Exception as e:
            ex = discord.Embed(description=f'```{e}```', color=colors.lightred)
            ex.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            ex.set_footer(text=embeds.footer)
            await ctx.send(embed=ex)

    @commands.command()
    async def genius(self, ctx, *, args):
        try:
            preview = "https://deezerdevs-deezer.p.rapidapi.com/search"
            genius = lyricsgenius.Genius(botsetup.genius_token)
            song = genius.search_song(f"{args}")

            querystring = {"q": f"{song.title} {song.artist}"}
            headers = {
                'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
                'x-rapidapi-key': botsetup.rapidapi_key}
            response = requests.request("GET", preview, headers=headers, params=querystring)
            x = response.text
            y = json.loads(x)
            title = y["data"][0]["title"]
            min = y["data"][0]["duration"]
            preview = y["data"][0]["preview"]
            l = discord.Embed(description=f'Duration: {min} minutes\n'
                                          f'Preview: [Play now]({preview})\n'f' \n'
                                          f'{song.lyrics}\n'f' \n'
                                          f'Song by {song.artist}\n', color=colors.genius)
            l.set_author(name=f'Genius: {song.title}', url='https://genius.com', icon_url=links.genius)
            l.set_thumbnail(url=f'{song.song_art_image_url}')
            l.set_footer(text=wm.footer)
            try:
                await ctx.send(embed=l)
            except:
                with open('users/genius_lyrics.txt', 'w') as g:
                    g.write(song.lyrics)
                    g.write(wm.footer)
                    txt = discord.Embed(description='', color=colors.genius)
                    txt.set_author(name=f'Genius: {song.title}', url='https://genius.com', icon_url=links.genius)
                    txt.set_footer(text=wm.footer)
                    await ctx.send(embed=txt)
                    await ctx.send(file=discord.File('users/genius_lyrics.txt'))
                    g.close()
        except Exception as e:
            nosong = discord.Embed(description=f'Cant find ``{args}``\n'
                                               f'```{e}```', color=colors.lightred)
            nosong.set_author(name='Genius: No song', url='https://genius.com', icon_url=links.genius)
            nosong.set_footer(text=embeds.footer)

    @commands.command()
    async def wyr(self, ctx):
        try:
            wyr_ = random.choice(wouldyourather.questions)
            wyr = discord.Embed(description=f'{wyr_}\n', color=0xff5252)
            wyr.set_author(icon_url=links.wyr, url='https://either.io', name='either.io')
            react = await ctx.send(embed=wyr)
            await react.add_reaction('🅰')
            await react.add_reaction('🅱')
        except Exception as e:
            ex = discord.Embed(description=f'```{e}```', color=colors.lightred)
            ex.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            ex.set_footer(text=embeds.footer)
            await ctx.send(embed=ex)

    @genius.error
    async def genius_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.noargs)


def setup(bot):
    bot.add_cog(Fun(bot))
