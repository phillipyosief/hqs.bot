# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import asyncio
import random
import discord
import lyricsgenius
import tweepy
from discord.ext import commands
import botsetup
from cog_info import colors, quotes
import errorembed
from cog_info import wouldyourather

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

consumer_key = botsetup.consumer_key
consumer_secret = botsetup.consumer_secret
access_token = botsetup.access_token
access_token_secret = botsetup.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

quote_1 = quotes.quote_1
quote_2 = quotes.quote_2
quote_3 = quotes.quote_3
quote_4 = quotes.quote_4
quote_5 = quotes.quote_5
quote_6 = quotes.quote_6
quote_7 = quotes.quote_7
quote_8 = quotes.quote_8
quote_9 = quotes.quote_9
quote_10 = quotes.quote_10

watermark = 'hqs.bot / by phillip.hqs'

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tweet(self, ctx, *, args):
        if args:
            with open("blacklist/blacklist_words.txt") as file:
                bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]
                message_content = args
                for bad_word in bad_words:
                    if bad_word in message_content:
                        blacklist = discord.Embed(title='Dont insult or advertise',
                                                  description='check [rules](https://hqs.bplaced.net/rules.html)',
                                                  color=red)
                        await ctx.send(embed=blacklist)
                        return
            try:
                api.update_status(status=f'New Tweet from {ctx.guild}\n'
                                         f'Author: {ctx.author}\n'
                                         f'---------\n'
                                         f'{args}\n'
                                         f'---------\n'
                                         f'hqs.bot: https://discord.com/oauth2/authorize?client_id=699223351138189363&permissions=8&scope=bot\n'
                                         f"AlphaClan: https://discord.gg/uFdVUMH\n"
                                         f"Website: https://hqsartworks.me\n")
                tweet1 = discord.Embed(title=f'Your tweet was sent successfully 😃',
                                       description=f'[Click here](https://twitter.com/alphaclanc) to see your tweet on tweet on twitter\n'
                                                   f'```{args}```', color=lightblue)
                tweet1.set_footer(text="hqs.bot ∫ by phillip.hqs")
                await ctx.send(embed=tweet1)
            except Exception as e:
                tweetfailed = discord.Embed(description=f'Error:\n'
                                                        f'``{e}``')
                tweetfailed.set_footer(text=watermark)
                await ctx.send(embed=tweetfailed)

    @commands.command()
    async def quote(self, ctx):
        quotes = [quote_1,
                  quote_2,
                  quote_3,
                  quote_4,
                  quote_5,
                  quote_6,
                  quote_7,
                  quote_8,
                  quote_9,
                  quote_10]
        quote = discord.Embed(title='Quote:', description=f'{random.choice(quotes)}', color=green)
        quote.set_footer(text=watermark)
        await ctx.send(embed=quote)

    @commands.command()
    async def genius(self, ctx, *, arg1):
        import json
        import requests
        url = "https://deezerdevs-deezer.p.rapidapi.com/search"

        try:
            loadingly = discord.Embed(title=f'Song/Artist: {arg1}', description='This can take few minutes',
                                      color=0xfffca1)
            loadingly.set_footer(text="hqs.bot ∫ by phillip.hqs")
            loadingly.set_author(name="Search Songtext",
                                 icon_url="https://www.koester-planung.de/_Resources/Static/Packages/Avency.KoesterBau.Base/Images/ajax-loader.gif")
            genius = lyricsgenius.Genius("A27ABe0jwhSJ_I1AJKNZOGBKzLjFHDeHFz1fMnNgbMo87PAE9y4UR_t9vZDuj6qe")
            loadingly
            song = genius.search_song(f"{arg1}")
            loadingly1 = await ctx.send(embed=loadingly)
            loadingly = discord.Embed(title='Loading Song...', description='This can take few minutes')
            loadingly.set_footer(text="hqs.bot ∫ by phillip.hqs")
            # try:
            querystring = {"q": f"{song.title} {song.artist}"}
            headers = {
                'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
                'x-rapidapi-key': "4edb62a493mshb56e4910dca2475p164b5bjsnd94e916906d7"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            x = response.text
            y = json.loads(x)
            title = y["data"][0]["title"]
            min = y["data"][0]["duration"]
            preview = y["data"][0]["preview"]
            lyric = discord.Embed(title=f'Song: {song.title}', description=f'Duration: {min} minutes\n'
                                                                           f'Preview: [Play now]({preview})\n'
                                                                           f' \n'
                                                                           f'{song.lyrics}\n'
                                                                           f'  \n'
                                                                           f'Song by {song.artist}\n',
                                  color=botsetup.geniusc)

            lyric.set_footer(text="hqs.bot ∫ by phillip.hqs")
            lyric.set_author(name="Genius",
                             icon_url="https://apkdirectory.com/logos/genius-song-lyrics-038-more.png", )
            await asyncio.sleep(5)
            await loadingly1.delete()
            try:
                await ctx.send(embed=lyric)
            except:
                file1 = open(f'genius_lyric.txt', 'w')
                file1.write('hqs.bot / by phillip.hqs\n'
                            '      \n')
                file1.write(song.lyrics)
                file1.write('      \n'
                            'hqs.bot / by phillip.hqs')
                file1.close()
                finishdl = discord.Embed(title="You can download the lyric from the song:",
                                         description=f'Duration: {min} minutes\n'
                                                     f'Preview: [Play now]({preview})\n',
                                         color=botsetup.geniusc)
                finishdl.set_author(name="Download finished",
                                    icon_url="https://apkdirectory.com/logos/genius-song-lyrics-038-more.png", )
                await ctx.send(embed=finishdl)
                await ctx.send(file=discord.File(f'genius_lyric.txt'))
        except:
            gnoly = discord.Embed(description=f'\n'
                                              f'If the song are available on [genius](https://genius.com)\n'
                                              f'click [bug report](https://hqs.bplaced.net/bugreport.html)',
                                  color=botsetup.error)
            gnoly.set_author(name=f'Error: Cant find song/artist: {arg1}',
                             icon_url='https://abload.de/img/15169975161ok74.gif')
            await ctx.send(embed=gnoly)
            await asyncio.sleep(5)
            await loadingly1.delete()

    @commands.command()
    async def wyr(self, ctx):
        wyr_ = random.choice(wouldyourather.questions)
        wyr = discord.Embed(description=f'{wyr_}\n', color=0xff5252)
        wyr.set_author(icon_url='https://images-na.ssl-images-amazon.com/images/I/61qsWw4O5IL.png',
                       url='https://either.io', name='either.io')
        react = await ctx.send(embed=wyr)
        await react.add_reaction('🅰')
        await react.add_reaction('🅱')



    @genius.error
    async def genius_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=errorembed.noargs)

    @tweet.error
    async def tweet_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=errorembed.noargs)


def setup(bot):
    bot.add_cog(fun(bot))