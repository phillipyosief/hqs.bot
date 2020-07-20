# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
from discord.ext import commands
from library.cog_info import colors
from library.icons import links
from library.error_embeds import embeds
from library.cog_text import about_text as wm
import setup as botsetup
import wikipedia
import requests
import discord
import pyqrcode
import png

class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, target: discord.Member or discord.Guild):
        try:
            try:
                with open(f'users/about/{target.id}') as r:
                    read = r.read()
                color = target.top_role.color
                u = discord.Embed(description=f'{read}', color=color)
                u.set_author(name=f'User: {target}', url=botsetup.website, icon_url=links.account_about)
                u.set_thumbnail(url=target.avatar_url)
                u.add_field(name='Mention', value=target.mention)
                u.add_field(name='ID', value=target.id)
                u.add_field(name='Role', value=target.top_role)
                u.add_field(name='Discriminator', value=target.discriminator)
                u.add_field(name='Joined server', value=target.joined_at)
                u.add_field(name='Activity', value=target.activity)
                u.add_field(name='Status', value=target.status)
                u.add_field(name='Permission value', value=target.top_role.permissions.value)
                u.add_field(name='Role color', value=target.top_role.color)
                u.set_footer(text='See more about role with /role')
                await ctx.send(embed=u)
            except:
                color = target.top_role.color
                u = discord.Embed(description=f'No about available', color=color)
                u.set_author(name=f'User: {target}', url=botsetup.website, icon_url=links.account_about)
                u.set_thumbnail(url=target.avatar_url)
                u.add_field(name='Mention', value=target.mention)
                u.add_field(name='ID', value=target.id)
                u.add_field(name='Role', value=target.top_role)
                u.add_field(name='Discriminator', value=target.discriminator)
                u.add_field(name='Joined server', value=target.joined_at)
                u.add_field(name='Activity', value=target.activity)
                u.add_field(name='Status', value=target.status)
                u.add_field(name='Permission value', value=target.top_role.permissions.value)
                u.add_field(name='Role color', value=target.top_role.color)
                u.set_footer(text='See more about role with /role')
                await ctx.send(embed=u)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @userinfo.error
    async def error_userinfo(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.nouser)

    @commands.command()
    async def roleinfo(self, ctx, role: discord.Role):
        try:
            r = discord.Embed(color=role.color)
            r.set_author(name=f'Role: {role.name}', url='https://hqsartworks.me',
                         icon_url=links.account_about)
            r.add_field(name=f'ID', value=f'{role.id}')
            r.add_field(name=f'Hierarchy', value=f'{role.position}')
            r.add_field(name=f'Created at', value=f'{role.created_at}')
            r.add_field(name=f'Color', value=f'{role.color}')
            r.add_field(name=f'Members', value=f'{len(role.members)}')
            r.add_field(name=f'Permissions value', value=f'{role.permissions.value}')
            r.add_field(name=f'Mentionable', value=f'{role.mentionable}')
            r.add_field(name=f'Mention', value=f'{role.mention}')
            r.add_field(name=f'Server', value=f'{role.guild}')
            r.add_field(name='add_reactions', value=f'{role.permissions.add_reactions}\n')
            r.add_field(name='administrator', value=f'{role.permissions.administrator}\n')
            r.add_field(name='attach_files', value=f'{role.permissions.attach_files}\n')
            r.add_field(name='ban_members', value=f'{role.permissions.ban_members}\n')
            r.add_field(name='change_nickname', value=f'{role.permissions.change_nickname}\n')
            r.add_field(name='connect', value=f'{role.permissions.connect}\n')
            r.add_field(name='create_instant_invite', value=f'{role.permissions.create_instant_invite}\n')
            r.add_field(name='deafen_members', value=f'{role.permissions.deafen_members}\n')
            r.add_field(name='embed_links', value=f'{role.permissions.embed_links}\n')
            r.add_field(name='external_emojis', value=f'{role.permissions.external_emojis}\n')
            r.add_field(name='kick_members', value=f'{role.permissions.kick_members}\n')
            r.add_field(name='manage_channels', value=f'{role.permissions.manage_channels}\n')
            r.add_field(name='manage_emojis', value=f'{role.permissions.manage_emojis}\n')
            r.add_field(name='manage_guild', value=f'{role.permissions.manage_guild}\n')
            r.add_field(name='manage_messages', value=f'{role.permissions.manage_messages}\n')
            r.add_field(name='manage_nicknames', value=f'{role.permissions.manage_nicknames}\n')
            r.add_field(name='manage_permissions', value=f'{role.permissions.manage_permissions}\n')
            r.add_field(name='manage_roles', value=f'{role.permissions.manage_roles}\n')
            r.add_field(name='manage_webhooks', value=f'{role.permissions.manage_webhooks}\n')
            r.add_field(name='mention_everyone', value=f'{role.permissions.mention_everyone}\n')
            r.add_field(name='add_reactions', value=f'{role.permissions.add_reactions}\n')
            r.add_field(name='move_members', value=f'{role.permissions.move_members}\n')
            r.add_field(name='value', value=f'{role.permissions.value}\n')
            r.set_footer(text=wm.footer)
            await ctx.send(embed=r)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @roleinfo.error
    async def error_roleinfo(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.norole)

    @commands.command()
    async def avatar(self, ctx, target: discord.User or discord.Guild):
        try:
            avatar = discord.Embed(color=colors.tools)
            avatar.set_author(name=f'Avatar: {target}', url=target.avatar_url,
                              icon_url=links.account_about)
            avatar.set_image(url=f'{target.avatar_url}')
            avatar.set_footer(text=wm.footer)
            await ctx.send(embed=avatar)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @avatar.error
    async def error_avatar(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.nouser)

    @commands.command()
    async def weather(self, ctx, *, args):
        try:
            api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
            city = args
            url = api_address + city
            json_data = requests.get(url).json()
            city = json_data['name']
            desc = json_data['weather'][0]['description']
            weather = discord.Embed(color=colors.tools, description=desc)
            weather.set_author(icon_url=links.weather,
                               name=f'Weather in {city}', url=botsetup.website)
            weather.set_footer(text=wm.footer)

            await ctx.send(embed=weather)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @weather.error
    async def error_weather(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.nocity)

    @commands.command()
    async def color(self, ctx, arg):
        try:
            c = discord.Embed(description=f'Color: {arg}', color=arg)
            c.set_author(name='Color', url=botsetup.website, icon_url=links.clear)
            c.set_footer(text='Color')
            await ctx.send(embed=c)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    async def checkiban(self, ctx, *, args):
        try:
            iban = f'{args}'
            laendercode = iban[:2]
            pruefziffer = iban[2:4]
            blz = iban[4:12]
            kontonummer = iban[12:].zfill(10)
            check = str(98 - int(blz + kontonummer + "131400") % 97).zfill(2)

            if check == pruefziffer:
                right = discord.Embed(color=colors.tools, description=f'Typed IBAN: ``{iban}``')
                right.set_author(name=f'IBAN is right', url=botsetup.website, icon_url=links.iban)
                right.set_footer(text=wm.footer)
                await ctx.send(embed=right)
            else:
                false = discord.Embed(color=colors.tools, description=f'Typed IBAN: ``{iban}``')
                false.set_author(name=f'IBAN is false', url=botsetup.website, icon_url=links.iban)
                false.set_footer(text=wm.footer)
                await ctx.send(embed=false)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @checkiban.error
    async def error_checkiban(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.noargs)

    @commands.command()
    async def wikipedia(self, ctx, *, args):
        get = wikipedia.summary(args)
        try:
            try:
                getwiki = discord.Embed(color=colors.tools, title=f'{wikipedia.page(f"{args}").title}',
                                        description=f'{wikipedia.summary(f"{args}")}\n')
                getwiki.set_author(
                    icon_url=links.wikipedia,
                    name=f'Wikipedia', url='https://wikipedia.com/')
                getwiki.set_footer(text=wm.footer)
                await ctx.send(embed=getwiki)
            except:
                wiki = open('users/wikipedia.txt', 'w')
                wiki.write(f'{get}')
                wiki.close()
                await ctx.send(file=discord.File('users/wikipedia.txt'))
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @wikipedia.error
    async def error_wikipedia(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.noargs)

    @commands.command()
    async def rtd(self, ctx):
        import requests
        from bs4 import BeautifulSoup

        url = 'https://hqsartworks.me'
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)

        output = ''
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head',
            'input',
            'script',
            'style'
            # there may be more elements you don't want, such as "style", etc.
        ]

        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)
        print(output)
        await ctx.send(output)

    @commands.command()
    async def survey(self, ctx, *, args):
        try:
            pool = discord.Embed(description=f'{args}', color=colors.tools)
            pool.set_author(name='Survey', url='https://hqsartworks.me',
                            icon_url=links.survey)
            pool.set_footer(text=wm.footer)
            reaction = await ctx.send(embed=pool)
            await reaction.add_reaction('👍')
            await reaction.add_reaction('👎')
        except Exception as e:
            cantfind = discord.Embed(description=f'Error:\n'
                                                 f'```{e}```\n')
            cantfind.set_footer(text=f'Report it with /report <bug>\n')
            cantfind.set_author(name='Survey, by phillip.hqs', url='https://hqsartworks.me',
                            icon_url='https://p7.hiclipart.com/preview/895/850/380/logo-brand-survey.jpg')
            await ctx.send(embed=cantfind)

    @survey.error
    async def error_survey(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.noargs)



    @commands.command()
    async def shorturl(self, ctx, args):
        try:
            import tinyurl
            for u in tinyurl.create(f'{args}'):
                url = discord.Embed(description=f'{u}', color=colors.tools)
                url.set_author(
                    icon_url=links.tinyurl,
                    name='TinyURL', url='https://tinyurl.com/')
                url.set_footer(text=wm.footer)
                await ctx.send(embed=url)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    async def qrcode(self, ctx, args, *arg):
        if arg == ():
            qr = discord.Embed(title='How to use QR-Code', color=colors.tools)
            qr.set_author(name='QR-Codes',
                          icon_url=links.qrcode)
            qr.add_field(value='Twitter', name='/qrcode <username> <twitter>', inline=True)
            qr.add_field(value='Instagram', name='/qrcode <username> <instagram>', inline=False)
            qr.add_field(value='Snapchat', name='/qrcode <username> <snapchat>', inline=True)
            qr.add_field(value='WhatsApp', name='/qrcode <phonenumber> <whatsapp>', inline=False)
            qr.add_field(value='E-Mail', name='/qrcode <email> <mail>', inline=True)
            qr.add_field(value='SMS', name='/qrcode <phonenumber> <sms>', inline=False)
            qr.add_field(value='Call', name='/qrcode <phonenumber> <tel>', inline=True)
            qr.add_field(value='PayPal', name='/qrcode <paypal.me/name> <paypal>', inline=False)
            qr.add_field(value='Skype', name='/qrcode <username> <skype>', inline=True)
            qr.add_field(value='Reddit', name='/qrcode <username> <reddit>', inline=False)
            qr.add_field(value='URL(link)', name='/qrcode <url/link> <url>', inline=True)
            await ctx.send(embed=qr)
        elif arg[0].lower() == 'url':
            import pyqrcode
            from PIL import Image
            url = pyqrcode.QRCode(f'{args}', error='H')
            url.png('users/qr.png', scale=10)
            im = Image.open('users/qr.png')
            im = im.convert("RGBA")
            logo = Image.open('assets/logo.jpg')
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)
            im.save('qr.png')
            await ctx.send(file=discord.File('qr.png'))
        elif arg[0].lower() == 'mail':
            import pyqrcode
            from PIL import Image
            url = pyqrcode.QRCode(f'mailto:{args}', error='H')
            url.png('users/qr.png', scale=10)
            im = Image.open('users/qr.png')
            im = im.convert("RGBA")
            logo = Image.open('assets/logo.jpg')
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)
            im.save('qr.png')
            im.show()
            await ctx.send(file=discord.File('qr.png'))
        elif arg[0].lower() == 'whatsapp':
            import pyqrcode
            from PIL import Image
            url = pyqrcode.QRCode(f'https://wa.me/{args}', error='H')
            url.png('users/qr.png', scale=10)
            im = Image.open('users/qr.png')
            im = im.convert("RGBA")
            logo = Image.open('assets/logo.jpg')
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)
            im.save('qr.png')
            await ctx.send(file=discord.File('qr.png'))
        elif arg[0].lower() == 'instagram':
            import pyqrcode
            from PIL import Image
            url = pyqrcode.QRCode(f'https://instagram.com/{args}', error='H')
            url.png('users/qr.png', scale=10)
            im = Image.open('users/qr.png')
            im = im.convert("RGBA")
            logo = Image.open('assets/logo.jpg')
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)
            im.save('qr.png')
            await ctx.send(file=discord.File('qr.png'))
        elif arg[0].lower() == 'twitter':
            import pyqrcode
            from PIL import Image
            url = pyqrcode.QRCode(f'https://twitter.com/{args}', error='H')
            url.png('users/qr.png', scale=10)
            im = Image.open('users/qr.png')
            im = im.convert("RGBA")
            logo = Image.open('assets/logo.jpg')
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)
            im.save('qr.png')
            await ctx.send(file=discord.File('qr.png'))
        elif arg[0].lower() == 'snapchat':
            import pyqrcode
            from PIL import Image
            url = pyqrcode.QRCode(f'https://snapchat.com/add/{args}', error='H')
            url.png('users/qr.png', scale=10)
            im = Image.open('users/qr.png')
            im = im.convert("RGBA")
            logo = Image.open('assets/logo.jpg')
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)
            im.save('qr.png')
            await ctx.send(file=discord.File('qr.png'))
        elif arg[0].lower() == 'reddit':
            import pyqrcode
            from PIL import Image
            url = pyqrcode.QRCode(f'https://reddit.com/u/{args}', error='H')
            url.png('users/qr.png', scale=10)
            im = Image.open('users/qr.png')
            im = im.convert("RGBA")
            logo = Image.open('assets/logo.jpg')
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)
            im.save('qr.png')
            await ctx.send(file=discord.File('qr.png'))
        elif arg[0].lower() == 'paypal':
            import pyqrcode
            from PIL import Image
            url = pyqrcode.QRCode(f'https://paypal.me/{args}', error='H')
            url.png('users/qr.png', scale=10)
            im = Image.open('users/qr.png')
            im = im.convert("RGBA")
            logo = Image.open('assets/logo.jpg')
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)
            im.save('qr.png')
            await ctx.send(file=discord.File('qr.png'))
        elif arg[0].lower() == 'tel':
            import pyqrcode
            from PIL import Image
            url = pyqrcode.QRCode(f'tel:{args}', error='H')
            url.png('users/qr.png', scale=10)
            im = Image.open('users/qr.png')
            im = im.convert("RGBA")
            logo = Image.open('assets/logo.jpg')
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)
            im.save('qr.png')
            await ctx.send(file=discord.File('qr.png'))
        elif arg[0].lower() == 'sms':
            import pyqrcode
            from PIL import Image
            url = pyqrcode.QRCode(f'sms:{args}', error='H')
            url.png('users/qr.png', scale=10)
            im = Image.open('users/qr.png')
            im = im.convert("RGBA")
            logo = Image.open('assets/logo.jpg')
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)
            im.save('qr.png')
            await ctx.send(file=discord.File('qr.png'))
        elif arg[0].lower() == 'skype':
            import pyqrcode
            from PIL import Image
            url = pyqrcode.QRCode(f'skype:{args}', error='H')
            url.png('users/qr.png', scale=10)
            im = Image.open('users/qr.png')
            im = im.convert("RGBA")
            logo = Image.open('assets/logo.jpg')
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)
            im.save('qr.png')
            await ctx.send(file=discord.File('qr.png'))

    @qrcode.error
    async def qrcode_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            qr = discord.Embed(title='How to use QR-Code', color=colors.tools)
            qr.set_author(name='QR-Codes',
                          icon_url=links.qrcode)
            qr.add_field(value='Twitter', name='/qrcode <username> <twitter>', inline=True)
            qr.add_field(value='Instagram', name='/qrcode <username> <instagram>', inline=False)
            qr.add_field(value='Snapchat', name='/qrcode <username> <snapchat>', inline=True)
            qr.add_field(value='WhatsApp', name='/qrcode <phonenumber> <whatsapp>', inline=False)
            qr.add_field(value='E-Mail', name='/qrcode <email> <mail>', inline=True)
            qr.add_field(value='SMS', name='/qrcode <phonenumber> <sms>', inline=False)
            qr.add_field(value='Call', name='/qrcode <phonenumber> <tel>', inline=True)
            qr.add_field(value='PayPal', name='/qrcode <paypal.me/name> <paypal>', inline=False)
            qr.add_field(value='Skype', name='/qrcode <username> <skype>', inline=True)
            qr.add_field(value='Reddit', name='/qrcode <username> <reddit>', inline=False)
            qr.add_field(value='URL(link)', name='/qrcode <url/link> <url>', inline=True)
            await ctx.send(embed=qr)
        elif isinstance(error, commands.CommandInvokeError):
            fail = discord.Embed(description=f'```{error}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)


def setup(bot):
    bot.add_cog(Tools(bot))