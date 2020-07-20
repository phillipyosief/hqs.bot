# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
import discord
import setup as botsetup
from discord.ext import commands
from library.cog_info import colors
from library.cog_text import about_text
from library.error_embeds import embeds
from library.icons import links
import requests


class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx, target: discord.User):
        with open(f'users/about/{target.id}', 'r') as a:
            read = a.readline()
        ab = discord.Embed(description=f'{read}', color=colors.lightblue)
        ab.set_author(name=f'About {target}', icon_url=links.account_about, url='')
        ab.set_thumbnail(url=f'{target.avatar_url}')
        ab.set_footer(text=about_text.footer)
        await ctx.send(embed=ab)

    @commands.command()
    async def createabout(self, ctx, *, args):
        with open(f'users/about/{ctx.author.id}', 'w') as a:
            write = a.writelines(f'{args}')
        with open(f'users/about/{ctx.author.id}', 'r') as a:
            read = a.readline()
        ab = discord.Embed(description=f'{read}', color=colors.lightblue)
        ab.set_author(name=f'About {ctx.author}', icon_url=links.account_about, url='')
        ab.set_thumbnail(url=f'{ctx.author.avatar_url}')
        ab.set_footer(text=about_text.footer)
        await ctx.send(embed=ab)

    @about.error
    async def about_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.nouser)

    @createabout.error
    async def createabout_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.noargs)


    @commands.command()
    async def invite(self, ctx):
        invite = discord.Embed(description=f'[Invite]({botsetup.invite}) | '
                                           f'[Donate]({botsetup.donate}) | [GitHub]({botsetup.github}) | '
                                           f'[Website]({botsetup.website}) | [Support Server]({botsetup.support_discord})\n'
                                           f'``Scan QRCode to invite``\n'
                                           f'*by phillip.hqs*', color=colors.mainblue)
        invite.set_author(name=f'{self.bot.user.name}#{self.bot.user.discriminator}', icon_url=links.logo)
        invite.set_thumbnail(
            url='https://media.discordapp.net/attachments/625231860250968094/715998947927392266/qr.png')
        await ctx.send(embed=invite)

    @commands.command()
    async def report(self, ctx, *, args):
        try:
            try:
                try:
                    with open(f'users/reports/{ctx.author}', 'a') as r:
                        r.writelines(f'User: {ctx.author}\n'
                                f'User ID: {ctx.author.id}\n'
                                f'Server: {ctx.guild}\n'
                                f'Report:\n'
                                f'{args}\n')
                except:
                    with open(f'users/reports/{ctx.author}', 'w') as r:
                        r.write(f'User: {ctx.author}\n'
                                f'User ID: {ctx.author.id}\n'
                                f'Server: {ctx.guild}\n'
                                f'Report:\n'
                                f'{args}\n')
            except:
                pass

            s = discord.Embed(description=f'```{args}```', color=colors.mainblue)
            s.set_author(name='Report', url=embeds.url, icon_url=links.report)
            s.set_footer(text=about_text.footer)
            await ctx.send(embed=s)
            try:
                return requests.post(
                    "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
                    auth=("api", f"{botsetup.mailgunkey}"),
                    data={"from": f"hqs.bot bugreport         {botsetup.mailgunmail}",
                          "to": ["contact@hqsartworks.me", f"{botsetup.reportmail}"],
                          "subject": f"Bugreport hqs.bot",
                          "text": f"{args}"})
            except:
                pass

        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    async def premium(self, ctx):
        v = discord.Embed(color=colors.mainblue)
        v.set_author(name='hqs.bot plus service', url=f"{botsetup.website}/plus", icon_url=links.coin)
        v.add_field(name='Functions', value=f'⠀\n'
                                            f'Addons\n'
                                            
                                            f'\n'
                                            f'Early access\n'
                                            f'\n'
                                            f'Forever reachable\n'
                                            f'\n'
                                            f'Access to beta\n'
                                            f'\n'
                                            f'Custom languages\n'
                                            f'\n'
                                            f'Custom prefix\n'
                                            f'\n'
                                            f'24/7 Support\n')

        v.add_field(name='With\n'
                         'plus', value='<:right:727934694104236102>\n'
                                       
        
                                       '\n'
                                                       '<:right:727934694104236102>\n'
                                       '\n'
                                                       '<:right:727934694104236102>\n'
                                       '\n'
                                                       '<:right:727934694104236102>\n'
                                       '\n'
                                                       '<:right:727934694104236102>\n'
                                       '\n'
                                                       '<:right:727934694104236102>\n'
                                       '\n'
                                                       '<:right:727934694104236102>\n'
                                       '\n')

        v.add_field(name='Without\n'
                         'plus', value=                   '<:false:727934694313951293>\n'  
                                       '\n'
                                                          '<:false:727934694313951293>\n'
                                       '\n'
                                                          '<:right:727934694104236102>\n'
                                       '\n'
                                                          '<:right:727934694104236102>\n'
                                       '\n'
                                                          '<:false:727934694313951293>\n'
                                       '\n'
                                                          '<:false:727934694313951293>\n'
                                       '\n'
                                                          '<:right:727934694104236102>\n'
                                       '\n')
        v.set_footer(text=about_text.footer)
        await ctx.send(embed=v)
        try:
            link = await ctx.channel.create_invite(max_age=1000, max_uses=10)
            with open('logs/plus_cmd/logs', 'a') as p:
                p.write(f'Server: {ctx.guild}\n'
                        f'User: {ctx.author}\n'
                        f'Channel: {ctx.channel}\n'
                        f'Server ID: {ctx.guild.id}\n'
                        f'User ID: {ctx.author.id}\n')
        except FileNotFoundError:
            link = await ctx.channel.create_invite(max_age=1000, max_uses=10)
            with open('logs/plus_cmd/logs', 'w') as p:
                p.write(f'Server: {ctx.guild}\n'
                        f'User: {ctx.author}\n'
                        f'Channel: {ctx.channel}\n'
                        f'Server ID: {ctx.guild.id}\n'
                        f'User ID: {ctx.author.id}\n'
                        f'Invite: {link}')

    @commands.command()
    async def plus(self, ctx):
        v = discord.Embed(color=colors.mainblue)
        v.set_author(name='hqs.bot plus service', url=f"{botsetup.website}/plus", icon_url=links.coin)
        v.add_field(name='Functions', value=f'⠀\n'
                                            f'Addons\n'

                                            f'\n'
                                            f'Early access\n'
                                            f'\n'
                                            f'Forever reachable\n'
                                            f'\n'
                                            f'Access to beta\n'
                                            f'\n'
                                            f'Custom languages\n'
                                            f'\n'
                                            f'Custom prefix\n'
                                            f'\n'
                                            f'24/7 Support\n')

        v.add_field(name='With\n'
                         'plus', value='<:right:727934694104236102>\n'


                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n')

        v.add_field(name='Without\n'
                         'plus', value='<:false:727934694313951293>\n'
                                       '\n'
                                       '<:false:727934694313951293>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:false:727934694313951293>\n'
                                       '\n'
                                       '<:false:727934694313951293>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n')
        v.set_footer(text=about_text.footer)
        await ctx.send(embed=v)
        try:
            link = await ctx.channel.create_invite(max_age=1000, max_uses=10)
            with open('logs/plus_cmd/logs', 'a') as p:
                p.write(f'Server: {ctx.guild}\n'
                        f'User: {ctx.author}\n'
                        f'Channel: {ctx.channel}\n'
                        f'Server ID: {ctx.guild.id}\n'
                        f'User ID: {ctx.author.id}\n')
        except FileNotFoundError:
            link = await ctx.channel.create_invite(max_age=1000, max_uses=10)
            with open('logs/plus_cmd/logs', 'w') as p:
                p.write(f'Server: {ctx.guild}\n'
                        f'User: {ctx.author}\n'
                        f'Channel: {ctx.channel}\n'
                        f'Server ID: {ctx.guild.id}\n'
                        f'User ID: {ctx.author.id}\n'
                        f'Invite: {link}')

    @commands.command()
    async def vip(self, ctx):
        v = discord.Embed(color=colors.mainblue)
        v.set_author(name='hqs.bot plus service', url=f"{botsetup.website}/plus", icon_url=links.coin)
        v.add_field(name='Functions', value=f'⠀\n'
                                            f'Addons\n'

                                            f'\n'
                                            f'Early access\n'
                                            f'\n'
                                            f'Forever reachable\n'
                                            f'\n'
                                            f'Access to beta\n'
                                            f'\n'
                                            f'Custom languages\n'
                                            f'\n'
                                            f'Custom prefix\n'
                                            f'\n'
                                            f'24/7 Support\n')

        v.add_field(name='With\n'
                         'plus', value='<:right:727934694104236102>\n'


                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n')

        v.add_field(name='Without\n'
                         'plus', value='<:false:727934694313951293>\n'
                                       '\n'
                                       '<:false:727934694313951293>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n'
                                       '<:false:727934694313951293>\n'
                                       '\n'
                                       '<:false:727934694313951293>\n'
                                       '\n'
                                       '<:right:727934694104236102>\n'
                                       '\n')
        v.set_footer(text=about_text.footer)
        await ctx.send(embed=v)
        try:
            link = await ctx.channel.create_invite(max_age=1000, max_uses=10)
            with open('logs/plus_cmd/logs', 'a') as p:
                p.write(f'Server: {ctx.guild}\n'
                        f'User: {ctx.author}\n'
                        f'Channel: {ctx.channel}\n'
                        f'Server ID: {ctx.guild.id}\n'
                        f'User ID: {ctx.author.id}\n')
        except FileNotFoundError:
            link = await ctx.channel.create_invite(max_age=1000, max_uses=10)
            with open('logs/plus_cmd/logs', 'w') as p:
                p.write(f'Server: {ctx.guild}\n'
                        f'User: {ctx.author}\n'
                        f'Channel: {ctx.channel}\n'
                        f'Server ID: {ctx.guild.id}\n'
                        f'User ID: {ctx.author.id}\n'
                        f'Invite: {link}')

def setup(bot):
    bot.add_cog(About(bot))
