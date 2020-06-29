# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
from __future__ import unicode_literals
from cog_info import colors
import asyncio
import time
import aiohttp
import discord
import lyricsgenius
import youtube_dl
from discord.ext import commands
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

# genius details
genius = lyricsgenius.Genius(
    botsetup.genius_token)  # your genius api token

data = []

# custom radio (only laut.fm radios)
radio1 = botsetup.radio1
radio1_name = botsetup.radio1_name

# colors
blue = 0x0062ff
black = 0x000000
yellow = 0xf5ff30
white = 0xffffff
green = 0x21ff55
grey = 0x636363
darkgrey = 0x1c1c1c
red = 0xff2121
purple = 0xb338ff
pink = 0xff47e0
lightblue = 0x4778ff
lightgreen = 0x73ffad
orange = 0xff9757

youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_opts = {
    'format': 'bestaudio/best',
    'outmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'

}
ffmpeg_opts = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}
ytdl = youtube_dl.YoutubeDL(ytdl_opts)


class RadioSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.05):
        super().__init__(source, volume)
        self.data = data

    @classmethod
    async def from_radio(cls, url, *, loop=None, stream=True):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_opts), data=data)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=1):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')
        self.webpage_url = data.get('webpage_url')
        self.thumbnail = data.get('thumbnail')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.raw_duration = data.get('duration')
        self.description = data.get('description')
        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        self.upload_date = f'{data.get("upload_date")[6:8]}.{data.get("upload_date")[4:6]}.' \
                           f'{data.get("upload_date")[0:4]}'

    class RadioSource(discord.PCMVolumeTransformer):
        def __init__(self, source, *, data, volume=0.05):
            super().__init__(source, volume)
            self.data = data

        @classmethod
        async def from_radio(cls, url, *, loop=None, stream=True):
            loop = loop or asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
            if 'entries' in data:
                data = data['entries'][0]

            filename = data['url'] if stream else ytdl.prepare_filename(data)
            return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_opts), data=data)

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_opts), data=data)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        # Create an actual string
        duration = []
        if days > 0:
            duration.append(f'{days} Days')
        if hours > 0:
            duration.append(f'{hours} Hours')
        if minutes > 0:
            duration.append(f'{minutes} Minutes')
        if seconds > 0:
            duration.append(f'{seconds} Seconds')

        return ', '.join(duration)


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        join = discord.Embed(title=f'joined {ctx.author.voice.channel}',
                             description='explore more commands with ´/help´', color=orange)
        join.set_footer(text="hqs.bot ∫ by phillip.hqs")
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(embed=join)

    @commands.command()
    async def leave(self, ctx):
        join = discord.Embed(title=f'leaving...', description='explore more commands with ´/help´', color=lightblue)
        join.set_footer(text="hqs.bot ∫ by phillip.hqs")
        server = ctx.message.guild.voice_client
        await server.disconnect()
        await ctx.send(embed=join)

    @commands.command()
    async def play(self, ctx: commands.Context, *, url):
        if botsetup.musicna == False:
            self.url = url
            self.wp = 0
            player = await YTDLSource.from_url(self.url, loop=self.bot.loop, stream=True)
            playembed = discord.Embed(title='Playing now', description=f'``\n{player.title}\n``',
                                      color=red)
            playembed.add_field(name='Length:', value=player.duration)
            playembed.add_field(name='Uploader:', value=f'[{player.uploader}]({player.uploader_url})')
            playembed.add_field(name='Song URL:', value=f'[Link to Song]({player.webpage_url})')
            playembed.set_thumbnail(url=player.thumbnail)
            channel = ctx.author.voice.channel
            if ctx.voice_client is not None:
                try:
                    await ctx.voice_client.move_to(channel)
                    ctx.voice_client.play(player)
                    vs = ctx.voice_client
                    vs.source.volume = 100 / 1000
                    await ctx.send(embed=playembed)
                    pass
                except discord.ClientException:
                    ctx.voice_client.stop()
                    await asyncio.sleep(1)
                    ctx.voice_client.play(player)
                    vs = ctx.voice_client
                    vs.source.volume = 100 / 1000
                    await ctx.send(embed=playembed)
                    pass
            elif channel is None:
                playerror = discord.Embed(title='Play:', description='You have to join in a channel', color=red,
                                          timestamp=ctx.message.created_at)
                playerror.set_footer(text="hqs.bot ∫ by phillip.hqs")
                await ctx.send(embed=playerror)
                pass
            else:
                await channel.connect()
                ctx.voice_client.play(player)
                vs = ctx.voice_client
                vs.source.volume = 100 / 1000
                await ctx.send(embed=playembed)
                pass
            while self.islooptrue:
                await asyncio.sleep(player.raw_duration)
                if self.islooptrue is False:
                    break
                elif self.islooptrue:
                    if ctx.voice_client is not None:
                        player = await YTDLSource.from_url(self.url, loop=self.bot.loop, stream=True)
                        try:
                            print('nach try')
                            print(self.url)
                            await ctx.voice_client.move_to(channel)
                            ctx.voice_client.play(player)
                            vs = ctx.voice_client
                            vs.source.volume = 100 / 1000
                            await ctx.send(embed=playembed)
                            pass
                        except discord.ClientException:
                            print('client exc')
                            print(self.url)
                            ctx.voice_client.stop()
                            ctx.voice_client.play(player)
                            vs = ctx.voice_client
                            vs.source.volume = 100 / 1000
                            await ctx.send(embed=playembed)
                            pass
                    else:
                        self.islooptrue = False
        elif botsetup.musicna == True:
            await ctx.send(embed=botsetup.nota)

    @commands.command()
    async def karaoke(self, ctx, *, args):
        if botsetup.musicna == False:
            try:
                loadingly = discord.Embed(title=f'Searching your lyric', description='This can take few minutes',
                                          color=0xfffca1)
                loadingly.set_footer(text="hqs.bot ∫ by phillip.hqs")

                loadingly.set_author(name="Search Songtext",
                                     icon_url="https://www.koester-planung.de/_Resources/Static/Packages/Avency.KoesterBau.Base/Images/ajax-loader.gif")

                song = genius.search_song(f"{args}")
                loadingly1 = await ctx.send(embed=loadingly)
                # try:
                lyric = discord.Embed(title=f'Song: {song.title}', description=f'{song.lyrics}\n'
                                                                               f'  \n'
                                                                               f'Song by {song.artist}\n',
                                      color=botsetup.geniusc)
                lyric.set_footer(text="hqs.bot ∫ by phillip.hqs")
                lyric.set_author(name="Genius",
                                 icon_url="https://apkdirectory.com/logos/genius-song-lyrics-038-more.png", )

                await asyncio.sleep(1)
                await loadingly1.delete()
                try:
                    ready = discord.Embed(title='Karaoke starts in 6 Seconds!', description='Are you ready', color=yellow)
                    ready.set_thumbnail(url=song.song_art_image_url)
                    ready.set_author(name="Genius",
                                     icon_url="https://apkdirectory.com/logos/genius-song-lyrics-038-more.png", )
                    ready.set_footer(text="hqs.bot ∫ by phillip.hqs")

                    await ctx.send(embed=ready)
                    await ready.delete()
                    await asyncio.sleep(5)
                    sendly = await ctx.send(embed=lyric)
                except:
                    ready = discord.Embed(title='Karaoke starts in 6 Seconds!', description='Are you ready', color=yellow)
                    ready.set_thumbnail(url=song.song_art_image_url)
                    ready.set_author(name="Genius",
                                     icon_url="https://apkdirectory.com/logos/genius-song-lyrics-038-more.png", )
                    ready.set_footer(text="hqs.bot ∫ by phillip.hqs")
                    file1 = open(f'genius_lyric.txt', 'w')
                    file1.write('hqs.bot / by phillip.hqs\n'
                                '      \n')
                    file1.write(song.lyrics)
                    file1.write('      \n'
                                'hqs.bot / by phillip.hqs')
                    file1.close()
                    finishdl = discord.Embed(title="You can download the lyric from the song:", color=botsetup.geniusc)
                    finishdl.set_author(name="Download finished",
                                        icon_url="https://apkdirectory.com/logos/genius-song-lyrics-038-more.png", )
                    finishdl.set_footer(text="hqs.bot ∫ by phillip.hqs")
                    await asyncio.sleep(1)
                    await ctx.send(embed=finishdl)

                    await ctx.send(file=discord.File(f'genius_lyric.txt'))

                    await asyncio.sleep(2)
            except:
                gnoly = discord.Embed(title='Cant find your song', description=f'\n'
                                                                               f'If the song are available on [genius](https://genius.com)\n'
                                                                               f'click [bug report](https://hqs.bplaced.net/bugreport.html)',
                                      color=botsetup.error)
                gnoly.set_author(name=f'Error: Cant find song/artist: {args}',
                                 icon_url='https://abload.de/img/15169975161ok74.gif')
                await ctx.send(embed=gnoly)
                await asyncio.sleep(5)
                await loadingly1.delete()

            self.url = f'{song.artist}, {song.title}'
            self.wp = 0
            player = await YTDLSource.from_url(self.url, loop=self.bot.loop, stream=True)
            playembed = discord.Embed(title='Start to sing!', description=f'``{player.title}\n``',
                                      color=red)
            playembed.add_field(name='Length:', value=player.duration)
            playembed.add_field(name='Uploader:', value=f'[{player.uploader}]({player.uploader_url})')
            playembed.add_field(name='Song URL:', value=f'[Link to Song]({player.webpage_url})')
            playembed.set_thumbnail(url=song.song_art_image_url)
            playembed.set_footer(text="hqs.bot ∫ by phillip.hqs")

            channel = ctx.author.voice.channel
            if ctx.voice_client is not None:
                try:
                    await ctx.voice_client.move_to(channel)
                    ctx.voice_client.play(player)
                    vs = ctx.voice_client
                    vs.source.volume = 100 / 1000
                    await ctx.send(embed=playembed)
                    pass
                except discord.ClientException:
                    ctx.voice_client.stop()
                    await asyncio.sleep(1)
                    ctx.voice_client.play(player)
                    vs = ctx.voice_client
                    vs.source.volume = 100 / 1000
                    await ctx.send(embed=playembed)
                    pass
            elif channel is None:
                playerror = discord.Embed(title='Play:', description='You have to join in a channel', color=red,
                                          timestamp=ctx.message.created_at)
                await ctx.send(embed=playerror)
                pass
            else:
                await channel.connect()
                ctx.voice_client.play(player)
                vs = ctx.voice_client
                vs.source.volume = 100 / 1000
                await ctx.send(embed=playembed)
                pass
        elif botsetup.musicna == True:
            await ctx.send(embed=botsetup.nota)

    @commands.command()
    async def radio(self, ctx, *arg):
        if botsetup.musicna == False:
            if arg == ():
                self.wp = 1
                station = f'{radio1_name}'
                async with aiohttp.ClientSession().get(f'http://api.laut.fm/station/{station}/current_song') as response:
                    song = await response.json()
                title = f'{song["artist"]["name"]} mit "{song["title"]}"'
                duration = time.strftime("%M:%S", time.gmtime(song['length']))
                player = await RadioSource.from_radio(f'{radio1}')
                radembed = discord.Embed(title='Auf hqs.fm wird gespielt', description=f'``fix\n{title}\n``',
                                         color=botsetup.normalcolor)
                radembed.add_field(name='Length:', value=f'{duration}')
                radembed.add_field(name='Radio URL:', value=f'[{radio1_name}]({radio1})')
                channel = ctx.author.voice.channel
                if ctx.voice_client is not None:
                    try:
                        await ctx.voice_client.move_to(channel)
                        ctx.voice_client.play(player)
                        vs = ctx.voice_client
                        vs.source.volume = 100 / 1000
                        await ctx.send(embed=radembed)
                        pass
                    except discord.ClientException:
                        ctx.voice_client.stop()
                        await asyncio.sleep(1)
                        ctx.voice_client.play(player)
                        vs = ctx.voice_client
                        vs.source.volume = 100 / 1000
                        await ctx.send(embed=radembed)
                        pass
                elif channel is None:
                    raderror = discord.Embed(title='Radio:', color=botsetup.normalcolor,
                                             description='Join a voice channel!')
                    raderror.set_author(name=botsetup.botname, icon_url='https://abload.de/img/speaker2zmkjgtik70.gif')
                    await ctx.send(embed=raderror)
                    pass
                else:
                    await channel.connect()
                    ctx.voice_client.play(player)
                    vs = ctx.voice_client
                    vs.source.volume = 100 / 1000
                    await ctx.send(embed=radembed)
                    pass

            elif arg[0] is not None:
                self.radioarg = arg[0]
                self.wp = 2
                radembed = discord.Embed(title='Radio station', description=f'```fix\n{arg[0]}\n```',
                                         color=red)
                radembed.add_field(name='Radio URL:', value=f'[URL]({arg[0]})')
                player = await RadioSource.from_radio(radio1)
                channel = ctx.author.voice.channel
                if ctx.voice_client is not None:
                    try:
                        await ctx.voice_client.move_to(channel)
                        ctx.voice_client.play(player)
                        vs = ctx.voice_client
                        vs.source.volume = 100 / 1000
                        await ctx.send(embed=radembed)
                        pass
                    except discord.ClientException:
                        ctx.voice_client.stop()
                        await asyncio.sleep(1)
                        ctx.voice_client.play(player)
                        vs = ctx.voice_client
                        vs.source.volume = 100 / 1000
                        await ctx.send(embed=radembed)
                        pass
                elif channel is None:
                    raderror = discord.Embed(title='Radio:', color=botsetup.normalcolor,
                                             description='You have to join a Voice channel', colour=red)
                    raderror.set_author(name=botsetup.botname, icon_url='https://abload.de/img/speaker2zmkjgtik70.gif')
                    await ctx.send(embed=raderror)
                    pass
                else:
                    await channel.connect()
                    ctx.voice_client.play(player)
                    vs = ctx.voice_client
                    vs.source.volume = 100 / 1000
                    await ctx.send(embed=radembed)
                    pass
        elif botsetup.musicna == True:
            await ctx.send(embed=botsetup.nota)

    @commands.command()
    async def pause(self, ctx):
        pauseembed = discord.Embed(title='Pause:', description='paused music', color=botsetup.normalcolor,
                                   timestamp=ctx.message.created_at)
        pauseerror = discord.Embed(title='Pause:', color=botsetup.normalcolor, timestamp=ctx.message.created_at,
                                   description='Im not playing music now')
        pauseembed.set_footer(text="hqs.bot ∫ by phillip.hqs")
        pauseerror.set_footer(text="hqs.bot ∫ by phillip.hqs")
        if ctx.voice_client is not None:
            ctx.voice_client.pause()
            self.islooptrue = False
            await ctx.send(embed=pauseembed)
        else:
            await ctx.send(embed=pauseerror)

    @commands.command()
    async def resume(self, ctx):
        resumeembed = discord.Embed(title='Resume:', color=botsetup.normalcolor, timestamp=ctx.message.created_at,
                                    description='continue music')
        resumeerror = discord.Embed(title='Resume:', color=botsetup.normalcolor, timestamp=ctx.message.created_at,
                                    description='Im not playing music now')
        resumeembed.set_footer(text="hqs.bot ∫ by phillip.hqs")
        resumeerror.set_footer(text="hqs.bot ∫ by phillip.hqs")
        if ctx.voice_client is not None:
            ctx.voice_client.resume()
            await ctx.send(embed=resumeembed)
        else:
            await ctx.send(embed=resumeerror)

    @commands.command()
    async def stop(self, ctx):
        stopembed = discord.Embed(title='Stop:', color=pink, timestamp=ctx.message.created_at,
                                  description='stopped music')
        stoperror = discord.Embed(title='Stop:', color=purple, timestamp=ctx.message.created_at,
                                  description='Im not playing music now')
        stoperror.set_footer(text="hqs.bot ∫ by phillip.hqs")
        stopembed.set_footer(text="hqs.bot ∫ by phillip.hqs")
        if ctx.voice_client is not None:
            ctx.voice_client.stop()
            self.islooptrue = False
            await ctx.send(embed=stopembed)
        else:
            await ctx.send(embed=stoperror)

    @commands.command()
    async def volume(self, ctx, value: int):
        if 100 >= value >= 1 and value != 0:
            vs = ctx.voice_client
            vs.source.volume = value / 1000
            volumeset = discord.Embed(title='Volume:', color=botsetup.normalcolor, timestamp=ctx.message.created_at,
                                      description=f'Change volume to `{value}%`')
            volumeset.set_footer(text="hqs.bot ∫ by phillip.hqs")
            await ctx.send(embed=volumeset)

        elif value > 100 or value == 0 or value < 1:
            volumeset = discord.Embed(title='Volume:', color=botsetup.normalcolor, timestamp=ctx.message.created_at,
                                      description=f'Choose a number between ´´1 - 100´´'
                                      )
            volumeset.set_footer(text="hqs.bot ∫ by phillip.hqs")
            await ctx.send(embed=volumeset)





def setup(bot):
    bot.add_cog(music(bot))
