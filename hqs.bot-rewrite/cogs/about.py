# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import discord
from discord.ext import commands
import botsetup
from cog_info import invite_text, about_text, colors
import errorembed

about_title = about_text.aboutserver_title
about_description = about_text.aboutserver_description

invite_title = invite_text.invitetext_title
invite_description = invite_text.invitetext_description

watermark = 'hqs.bot / by phillip.hqs'

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

class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aboutserver(self, ctx):
        aboutserver = discord.Embed(title=about_title, description=about_description,
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
            invite.set_author(name='hqs.bot_beta#1961', icon_url=botsetup.botlogo)
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
            await ctx.send(embed=errorembed.noargs)

    @commands.command()
    async def inviteserver(self, ctx):
        inviteserver = discord.Embed(title=about_title, description=about_description,
                                     color=botsetup.normalcolor)
        inviteserver.set_footer(text=watermark)
        await ctx.send(embed=inviteserver)




def setup(bot):
    bot.add_cog(about(bot))