# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
import asyncio
import discord
import requests
import wikipedia
from discord.ext import commands
from cog_info import colors, usernames
import discordwebhook
import time

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

watermark = 'hqs.bot / by phillip.hqs'


class tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def checkiban(self, ctx, *, args):
        check = discord.Embed(title='checking IBAN')
        check.set_thumbnail(url='https://i.pinimg.com/originals/0b/f4/2e/0bf42e527bd585e6ebace4fefbb0c14d.gif')
        checking = await ctx.send(embed=check)
        iban = f'{args}'
        laendercode = iban[:2]
        pruefziffer = iban[2:4]
        blz = iban[4:12]
        kontonummer = iban[12:].zfill(10)
        check = str(98 - int(blz + kontonummer + "131400") % 97).zfill(2)
        await asyncio.sleep(5)
        await checking.delete()
        if check == pruefziffer:
            right = discord.Embed(title='These IBAN is right', color=green, description=f'Typed IBAN: ``{iban}``')
            right.set_thumbnail(
                url='https://66.media.tumblr.com/61c8d368e2a6e53ecf048b8bbc1ef60d/tumblr_mwyo98aufM1t3hbhyo1_r1_250.gif')
            right.set_footer(text=watermark)
            await ctx.send(embed=right)
        else:
            false = discord.Embed(title='These IBAN is false', color=red, description=f'Typed IBAN: ``{iban}``')
            false.set_thumbnail(
                url='https://66.media.tumblr.com/61c8d368e2a6e53ecf048b8bbc1ef60d/tumblr_mwyo98aufM1t3hbhyo1_r1_250.gif')
            await ctx.send(embed=false)

    @commands.command()
    async def weather(self, ctx, *, args):
        try:
            api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
            city = args
            url = api_address + city
            json_data = requests.get(url).json()
            city = json_data['name']
            desc = json_data['weather'][0]['description']
            temp = json_data['weather'][0]['temperature']
            weather = discord.Embed(title=f'Weather in {city}', description=f'{desc}, {temp}\n'
                                                                            f'', color=orange)
            weather.set_author(icon_url='https://pbs.twimg.com/profile_images/1173919481082580992/f95OeyEW_400x400.jpg',
                               name=f'OpenWeatherMap', url=url)
            weather.set_footer(text=f'Click OpenWeatherMap to see more details')

            await ctx.send(embed=weather)
        except:
            nc = discord.Embed(title='Cant find your city')
            nc.set_author(icon_url='https://pbs.twimg.com/profile_images/1173919481082580992/f95OeyEW_400x400.jpg',
                          name=f'OpenWeatherMap', url=url)
            await ctx.send(embed=nc)

    @commands.command()
    async def wikipedia(self, ctx, *, args):
        get = wikipedia.summary({args})
        try:
            try:
                getwiki = discord.Embed(color=0xffffff, title=f'{wikipedia.page(f"{args}").title}',
                                        description=f'{wikipedia.summary(f"{args}")}\n')
                getwiki.set_author(
                    icon_url=f'https://is1-ssl.mzstatic.com/image/thumb/Purple123/v4/d1/9c/8a/d19c8a38-d24e-194d-6a34-40a850752fab/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/246x0w.png',
                    name=f'Wikipedia')
                await ctx.send(embed=getwiki)
            except:
                wiki = open('wikipedia.txt', 'w')
                wiki.write(f'{get}')
                wiki.close()
                await ctx.send(file=discord.File('wikipedia.txt'))
        except Exception as e:
            cantfind = discord.Embed(title='Wikipedia', description=f'```{e}```')
            cantfind.set_author(
                icon_url=f'https://is1-ssl.mzstatic.com/image/thumb/Purple123/v4/d1/9c/8a/d19c8a38-d24e-194d-6a34-40a850752fab/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/246x0w.png',
                name=f'Wikipedia')
            await ctx.send(embed=cantfind)

    @commands.command()
    async def survey(self, ctx, *, args):
        try:
            pool = discord.Embed(description=f'{args}')
            pool.set_author(name='Survey, by phillip.hqs', url='https://hqsartworks.me',
                            icon_url='https://p7.hiclipart.com/preview/895/850/380/logo-brand-survey.jpg')
            pool.set_footer(text='hqs.bot')
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

    @commands.command()
    async def avatar(self, ctx, target: discord.User or discord.member):
        avatar = discord.Embed(title='Avatar:')
        avatar.set_image(url=f'{target.avatar_url}')
        await ctx.send(embed=avatar)

    @wikipedia.error
    async def wikipedia_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            noargs = discord.Embed(title='Missing required article!',
                                   description=f'Please provide an article\n'
                                               f'to use that command',
                                   color=0xff2121)
            noargs.set_author(icon_url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif'
                              , name='Oh no...')
            noargs.set_thumbnail(url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif')
            await ctx.send(embed=noargs)

    @commands.command()
    async def username_gen(self, ctx):
        s = discord.Embed(title='Your new username is...', color=lightgreen)
        s.set_image(url='https://cdn.mensagenscomamor.com/content/images/m000510694.gif?v=1')
        tw = await ctx.send(embed=s)
        await asyncio.sleep(4)
        await tw.delete()
        u = discord.Embed(title='Your new username is...', description=f'{usernames.username}', color=lightblue)
        u.set_author(name='Username generator', url='https://hqsartworks.me', icon_url='https://img.pngio.com/microsoft-learning-personal-photo-png-200_200.png')
        await ctx.send(embed=u)

    @commands.command()
    async def shorturl(self, ctx, args):
        try:
            import tinyurl
            for u in tinyurl.create(f'{args}'):
                url = discord.Embed(title='Shorted URL', description=f'{u}')
                url.set_author(
                    icon_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pcprofessionale.it%2Fnews%2Fhowto%2Fcome-accorciare-link-tinyurl-segnalibri%2F&psig=AOvVaw2orWOWR4YhnnNA-3WkJm6Q&ust=1590841466662000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKiO5rWI2ekCFQAAAAAdAAAAABAR',
                    name='TinyURL', url='https://tinyurl.com/')
                url.set_footer(text=watermark)
                await ctx.send(embed=url)
        except Exception as e:
            cantfind = discord.Embed(description=f'Error:\n'
                                                 f'```{e}```\n')
            cantfind.set_footer(text=f'Report it with /report <bug>\n')
            cantfind.set_author(
                icon_url='https://images.sftcdn.net/images/t_app-logo-xl,f_auto/p/1c7edd10-99eb-11e6-8e5f-00163ec9f5fa/384804281/tinyurl-logo.png',
                name='TinyURL', url='https://tinyurl.com/')
            await ctx.send(embed=cantfind)

    @commands.command()
    @commands.has_role(501795866122649600)
    async def sendmail(self, ctx, arg1, arg2, *, args):
        import botsetup
        try:
            requests.post(
                url=f"{botsetup.mailgunurl}",
                auth=("api", f"{botsetup.mailgunkey}"),
                data={"from": f"[Custom Usermail from {ctx.author}] hqsbot_usermail@{botsetup.mailgunmail}",
                      "to": [f"{arg1}"],
                      "subject": f"send with hqs.bot | Subject: {arg2}",
                      "text": f"===========Content=============================\n"
                              f"{args}\n"
                              f"===============================================\n"
                              f"Invite hqs.bot https://hqsartworks.me\n"
                              f"Join now https://hqsartworks.me/discord.html\n"
                              f"==============================================="})
            mail = discord.Embed(title=f'{arg1}', description=f'Subject: ``{arg2}``\n'
                                                              f'Text: ``{args}``')
            mail.set_author(
                icon_url='https://lh3.googleusercontent.com/proxy/-XB_yJ7y8fHEzX5BtbprXME77HK5_Ww779wUgQEuWY4kn08fN_zuYwESYBl2TvpDbu4ZfA5zI_iwHtefe9fPqA',
                name=f'Sending E-Mail to')
            mail.set_footer(text=watermark)
            await ctx.send(embed=mail)
        except Exception as e:
            cantfind = discord.Embed(title='E-Mail', description=f'```{e}```')
            await ctx.send(embed=cantfind)

    @commands.command()
    async def qrcode(self, ctx, args, *arg):
        if arg == ():
            qr = discord.Embed(title='How to use QR-Code', color=orange)
            qr.set_author(name='QR-Codes',
                          icon_url='https://www.qrcode-generator.de/wp-content/themes/qr/new_structure/markets/core_market/generator/dist/generator/assets/images/websiteQRCode_noFrame.png')
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
            url.png('qr.png', scale=10)
            im = Image.open('qr.png')
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
            url.png('qr.png', scale=10)
            im = Image.open('qr.png')
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
            url.png('qr.png', scale=10)
            im = Image.open('qr.png')
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
            url.png('qr.png', scale=10)
            im = Image.open('qr.png')
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
            url.png('qr.png', scale=10)
            im = Image.open('qr.png')
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
            url.png('qr.png', scale=10)
            im = Image.open('qr.png')
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
            url.png('qr.png', scale=10)
            im = Image.open('qr.png')
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
            url.png('qr.png', scale=10)
            im = Image.open('qr.png')
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
            url.png('qr.png', scale=10)
            im = Image.open('qr.png')
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
            url.png('qr.png', scale=10)
            im = Image.open('qr.png')
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
            url.png('qr.png', scale=10)
            im = Image.open('qr.png')
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
            qr = discord.Embed(title='How to use QR-Code', color=orange)
            qr.set_author(name='QR-Codes',
                          icon_url='https://www.qrcode-generator.de/wp-content/themes/qr/new_structure/markets/core_market/generator/dist/generator/assets/images/websiteQRCode_noFrame.png')
            qr.add_field(name='Twitter', value='/qrcode <username> <twitter>')
            qr.add_field(name='Instagram', value='/qrcode <username> <instagram>')
            qr.add_field(name='Snapchat', value='/qrcode <username> <snapchat>')
            qr.add_field(name='WhatsApp', value='/qrcode <phonenumber> <whatsapp>')
            qr.add_field(name='E-Mail', value='/qrcode <email> <mail>')
            qr.add_field(name='SMS', value='/qrcode <phonenumber> <sms>')
            qr.add_field(name='Call', value='/qrcode <phonenumber> <tel>')
            qr.add_field(name='PayPal', value='/qrcode <paypal.me/name> <paypal>')
            qr.add_field(name='Skype', value='/qrcode <username> <skype>')
            qr.add_field(name='Reddit', value='/qrcode <username> <reddit>')
            qr.add_field(name='url(link)', value='/qrcode <url/link> <url>')
            await ctx.send(embed=qr)
        elif isinstance(error, commands.CommandInvokeError):
            qr = discord.Embed(title='How to use QR-Code', color=orange)
            qr.set_author(name='QR-Codes',
                          icon_url='https://www.qrcode-generator.de/wp-content/themes/qr/new_structure/markets/core_market/generator/dist/generator/assets/images/websiteQRCode_noFrame.png')
            qr.add_field(name='Twitter', value='/qrcode <username> <twitter>')
            qr.add_field(name='Instagram', value='/qrcode <username> <instagram>')
            qr.add_field(name='Snapchat', value='/qrcode <username> <snapchat>')
            qr.add_field(name='WhatsApp', value='/qrcode <phonenumber> <whatsapp>')
            qr.add_field(name='E-Mail', value='/qrcode <email> <mail>')
            qr.add_field(name='SMS', value='/qrcode <phonenumber> <sms>')
            qr.add_field(name='Call', value='/qrcode <phonenumber> <tel>')
            qr.add_field(name='PayPal', value='/qrcode <paypal.me/name> <paypal>')
            qr.add_field(name='Skype', value='/qrcode <username> <skype>')
            qr.add_field(name='Reddit', value='/qrcode <username> <reddit>')
            qr.add_field(name='url(link)', value='/qrcode <url/link> <url>')
            await ctx.send(embed=qr)

def setup(bot):
    bot.add_cog(tools(bot))