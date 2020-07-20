# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
from __future__ import unicode_literals
import asyncio
import discord
import lyricsgenius
import youtube_dl
from discord.ext import commands
import setup as botsetup
from library.cog_info import colors
from library.cog_text import about_text as wm
from library.error_embeds import embeds
from library.icons import links

genius = lyricsgenius.Genius(
    botsetup.genius_token)

data = []

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
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.views = data.get('view_count')

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

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        try:
            j = discord.Embed(color=colors.music)
            j.set_author(name=f'Joined {ctx.author.voice.channel}', url=botsetup.website, icon_url=links.join)
            j.add_field(name='Channel ID', value=f'{ctx.author.voice.channel.id}', inline=False)
            j.add_field(name='Category', value=f'{ctx.author.voice.channel.category}', inline=False)
            j.set_footer(text=wm.footer)
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(embed=j)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    async def leave(self, ctx):
        try:
            l = discord.Embed(color=colors.music)
            l.set_author(name=f'Leaved {ctx.author.voice.channel}', url=botsetup.website, icon_url=links.leave)
            l.add_field(name='Channel ID', value=f'{ctx.author.voice.channel.id}', inline=False)
            l.add_field(name='Category', value=f'{ctx.author.voice.channel.category}', inline=False)
            l.set_footer(text=wm.footer)
            server = ctx.message.guild.voice_client
            await server.disconnect()
            await ctx.send(embed=l)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    async def play(self, ctx: commands.Context, *, url):
        self.url = url
        self.wp = 0


        player = await YTDLSource.from_url(self.url, loop=self.bot.loop, stream=True)

        playembed = discord.Embed(description=f'Likes: {player.likes}, Dislike: {player.dislikes}, Views: {player.views}', color=colors.music)
        playembed.set_author(name=f'Playing now: {player.title}', url=player.webpage_url, icon_url=links.play)
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
            await ctx.send(embed=embeds.j)
            pass
        else:
            await channel.connect()
            ctx.voice_client.play(player)
            vs = ctx.voice_client
            vs.source.volume = 100 / 1000
            await ctx.send(embed=playembed)
            pass

    @commands.command()
    async def pause(self, ctx):
        try:
            p = discord.Embed(color=colors.music)
            p.set_author(name='Pause', url=botsetup.website, icon_url=links.pause)
            p.add_field(name='Channel ID', value=f'{ctx.author.voice.channel.id}', inline=False)
            p.add_field(name='Category', value=f'{ctx.author.voice.channel.category}', inline=False)
            p.set_footer(text=wm.footer)

            e = discord.Embed(color=colors.music, description='Im not playing music now')
            e.set_author(name='Pause', url=botsetup.website, icon_url=links.pause)
            e.set_footer(text=wm.footer)
            if ctx.voice_client is not None:
                ctx.voice_client.pause()
                self.islooptrue = False
                await ctx.send(embed=p)
            else:
                await ctx.send(embed=e)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    async def resume(self, ctx):
        try:
            p = discord.Embed(color=colors.music)
            p.set_author(name='Resume', url=botsetup.website, icon_url=links.resume)
            p.add_field(name='Channel ID', value=f'{ctx.author.voice.channel.id}', inline=False)
            p.add_field(name='Category', value=f'{ctx.author.voice.channel.category}', inline=False)
            p.set_footer(text=wm.footer)

            e = discord.Embed(color=colors.music, description='Im not playing music now')
            e.set_author(name='Resume', url=botsetup.website, icon_url=links.resume)
            e.set_footer(text=wm.footer)
            if ctx.voice_client is not None:
                ctx.voice_client.resume()
                await ctx.send(embed=p)
            else:
                await ctx.send(embed=e)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    async def stop(self, ctx):
        try:
            p = discord.Embed(color=colors.music)
            p.set_author(name='Stop', url=botsetup.website, icon_url=links.stop)
            p.add_field(name='Channel ID', value=f'{ctx.author.voice.channel.id}', inline=False)
            p.add_field(name='Category', value=f'{ctx.author.voice.channel.category}', inline=False)
            p.set_footer(text=wm.footer)

            e = discord.Embed(color=colors.music, description='Im not playing music now')
            e.set_author(name='Stop', url=botsetup.website, icon_url=links.stop)
            e.set_footer(text=wm.footer)
            if ctx.voice_client is not None:
                ctx.voice_client.stop()
                self.islooptrue = False
                await ctx.send(embed=p)
            else:
                await ctx.send(embed=e)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    async def volume(self, ctx, value: int):
        if 100 >= value >= 1 and value != 0:
            vs = ctx.voice_client
            vs.source.volume = value / 1000

            v = discord.Embed(color=colors.music, description=f'Change volume to ``{value}%``')
            v.set_author(name='Volume', url=botsetup.website, icon_url=links.volume)
            v.set_footer(text=wm.footer)
            await ctx.send(embed=v)

        elif value > 100 or value == 0 or value < 1:
            s = discord.Embed(color=colors.music, description=f'Choose a number between ´´1 - 100´´')
            s.set_author(name='Volume', url=botsetup.website, icon_url=links.volume)
            s.set_footer(text=wm.footer)
            await ctx.send(embed=s)


def setup(bot):
    bot.add_cog(Music(bot))