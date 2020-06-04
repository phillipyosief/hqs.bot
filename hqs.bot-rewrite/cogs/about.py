# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import discord
from discord.ext import commands
import botsetup

aboutserver_title = botsetup.aboutserver_title
aboutserver_description = botsetup.aboutserver_description

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

watermark = 'hqs.bot / by phillip.hqs'

class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aboutserver(self, ctx):
        aboutserver = discord.Embed(title=aboutserver_title, description=aboutserver_description,
                                    color=botsetup.normalcolor)
        aboutserver.set_footer(text=watermark)
        await ctx.send(embed=aboutserver)


    @commands.command()
    async def invite(self, ctx):
        invite = discord.Embed(description=f'[Invite]({botsetup.invite}) | '
                                           f'[Donate](https://www.tipeeestream.com/hqsartworks/donation) | [GitHub]({botsetup.github}) | '
                                           f'[Website]({botsetup.website}) | [Support Server]({botsetup.support_dc})\n'
                                           f'``Scan QRCode to invite``\n'
                                           f'*by phillip.hqs*', color=lightblue)
        if botsetup.beta == True:
            invite.set_author(name='hqs.bot_beta#1961', icon_url=botsetup.betalogo)
            invite.set_thumbnail(
                url='https://media.discordapp.net/attachments/625231860250968094/715999013484232794/qr.png')
            await ctx.send(embed=invite)
        elif botsetup.beta == False:
            invite.set_author(name='hqs.bot#8761', icon_url=botsetup.botlogo)
            invite.set_thumbnail(
                url='https://media.discordapp.net/attachments/625231860250968094/715998947927392266/qr.png')
            await ctx.send(embed=invite)

    @commands.command()
    async def createabout(self, ctx, *, args):
        file = open(f'{ctx.author}', 'w')
        file.write(f'{args}')
        file.close()
        send = open(f'{ctx.author}', 'r')
        read = send.readline()
        about = discord.Embed(title=f'About {ctx.author}', description=f'{read}', color=orange)
        about.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed=about)

    @createabout.error
    async def createabout_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=botsetup.noargs)

    @commands.command()
    async def about(self, ctx, target: discord.Member or discord.client):
        send = open(f'{target}', 'r')
        read = send.readline()
        about = discord.Embed(title=f'About {target}', description=f'{read}', color=orange)
        about.set_thumbnail(url=target.avatar_url)
        await ctx.send(embed=about)




def setup(bot):
    bot.add_cog(about(bot))
