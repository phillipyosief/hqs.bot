# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import discord


beta = False # hqs.bot_beta
default = True # default token
musicna = True # disable music
developing = False # hqs.bot_developing
help = False # True will disable help

if selfbot == False:
    prefix = '/'  # Command prefix
if selfbot == True:
    prefix = '#'  # Command prefix



nota = discord.Embed(title='Sorry...',
                     description='This command are currently not available',
                     color=0xff2121)

noargs = discord.Embed(title='Missing required text!', description=f'Please provide a text\n'
                                                                   f'to use that command', color=0xff2121)
noargs.set_author(icon_url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif'
                  , name='Oh no...')
noargs.set_thumbnail(url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif')

noiban = discord.Embed(title='Missing required IBAN Number!', description=f'Please provide a IBAN Number\n'
                                                          f'to use that command', color=0xff2121)
noiban.set_author(icon_url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif', name='Oh no...')
noiban.set_thumbnail(url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif')

nouser = discord.Embed(title='Missing required user!', description=f'Please provide a user\n'
                                                               f'to use that command', color=0xff2121)
nouser.set_author(icon_url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif'
              , name='Oh no...')
nouser.set_thumbnail(url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif')

norole = discord.Embed(title='Missing required role!', description=f'Please provide a role\n'
                                                           f'to use that command', color=0xff2121)
norole.set_author(icon_url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif'
          , name='Oh no...')
norole.set_thumbnail(url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif')

nochan = discord.Embed(title='Missing required channel!', description=f'Please provide a channel\n'
                                                       f'to use that command', color=0xff2121)
nochan.set_author(icon_url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif'
      , name='Oh no...')
nochan.set_thumbnail(url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif')

noperm = discord.Embed(title='Missing required permissions!', description=f'You dont have the permissions\n'
                                                                          f'to do that', color=0xff2121)
noperm.set_author(icon_url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif'
  , name='Oh no...')
noperm.set_thumbnail(url='https://i.pinimg.com/originals/0b/25/b9/0b25b9f0ac2dddfb1f0a75f9a9a004aa.gif')

ownerid = ''  # type the ID of the Owner
botname = ''  # type the name of the Bot
twitchurl = 'https://twitch.tv/philliphqs'  # type your twitch link
normalcolor = 0x36393E  # color for Embeds (not for all embeds)
supid = ''  # Support channel
botlogo = '' # logo for bot

support_dc = 'https://discord.com/invite/cXztd9q'

mailgunurl = '' 
mailgunkey = ''
mailgunmail = ''

# deezer rapidapi
botsetup.rapidapihost = ''
botsetup.rapidapikey = ''

# Tokens
betat = ''
defaultt = ''
developingt = ''

invitebeta = 'https://discord.com/api/oauth2/authorize?client_id=715625980630270024&permissions=8&scope=bot'
invite = 'https://discord.com/api/oauth2/authorize?client_id=699223351138189363&permissions=8&scope=bot'

betalogo = 'https://cdn.discordapp.com/avatars/715625980630270024/25ee757283f56bf090fbe953987887e7.png?size=128'
# Genius details
genius_token = ""

# custom radio (only support for laut.fm)
radio1 = 'https://laut.fm/hqsfm'  # type a radio link
radio1_name = 'hqs.fm'  # type the radio name

# twitter details
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Roles
owner = 501795866122649600  # type the role id
moderation = 501795866122649600  # type the role id
supporter = 501795866122649600  # type the role id
team = owner + moderation + supporter  # DONT DELETE
mute = 501795866122649600  # Add a Role that cant write in any channel (only read)
user = 501795866122649600  # type the role ID that all users have

# Channels
news = 516230048861257728  # type the ID of the news channel
support = 516231370381721611  # type the of the support channel
logs = 534782504805072928  # type the ID of the logs channel

# type your server ID
serverid = 501793911594024960

# Invite text
invitetext_title = ''  # Title of invite
invitetext_description = ''  # description of invite text

# About Server text
aboutserver_title = 'about server title'
aboutserver_description = 'about server description'

# quotes
quote_1 = 'Two things are infinite: the universe and human stupidity; and Im not sure about the universe. - Albert Einstein'  # type a quote or let it
quote_2 = 'Be who you are and say what you feel, because those who mind dont matter, and those who matter dont mind - Bernard M. Baruch'  # type a quote or let it
quote_3 = 'A room without books is like a body without a soul. - Marcus Tullius Cicero'  # type a quote or let it
quote_4 = 'Without music, life would be a mistake. ― Friedrich Nietzsche'  # type a quote or let it
quote_5 = 'Twenty years from now you will be more disappointed by the things that you didnt\n' \
          ' do than by the ones you did do. So throw off the bowlines. Sail away from the safe harbor. Catch the trade winds ' \
          'in your sails. Explore. Dream. Discover. - H. Jackson Brown Jr.'  # type a quote or let it
quote_6 = 'The greatest glory in living lies not in never falling, but in rising every time we fall.\n' \
          '- Nelson Mandela'  # type a quote or let it
quote_7 = 'The way to get started is to quit talking and begin doing. - Walt Disney'  # type a quote or let it
quote_8 = 'Your time is limited, so dont waste it living someone elses life. Dont be trapped by dogma – which\n' \
          'is living with the results of other peoples thinking. - Steve Jobs'  # type a quote or let it
quote_9 = 'If you look at what you have in life, youll always have more. If you look at what you dont have\n' \
          'in life, youll never have enough. - Oprah Winfrey'  # type a quote or let it
quote_10 = 'If you set your goals ridiculously high and its a failure, you will\n' \
           'fail above everyone elses success. - James Cameron'  # type a quote or let it

# dice emoji
dice_1 = '1️⃣'  # if you want you can set custom emojis
dice_2 = '2️⃣'  # if you want you can set custom emojis
dice_3 = '3️⃣'  # if you want you can set custom emojis
dice_4 = '4️⃣'  # if you want you can set custom emojis
dice_5 = '5️⃣'  # if you want you can set custom emojis
dice_6 = '6️⃣'  # if you want you can set custom emojis

# colors
geniusc = 0xf8ff38
error = 0xff0000

# logos
checkra1n = 'https://cdn.discordapp.com/attachments/663457551949627392/709400429875822632/checkra1n.png'

# jailbreak downloads
bootra1n64 = 'https://github.com/foxlet/bootra1n/releases/download/0.10.1/bootra1n-x86_64-0.10.1-20200408.iso'
bootra1n32 = 'https://github.com/foxlet/bootra1n/releases/download/0.10.1/bootra1n-i686-0.10.1-20200408.iso'
etcher = 'https://github-production-release-asset-2e65be.s3.amazonaws.com/45055693/fc715500-8fc0-11ea-8265-49988be85b68?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20200511%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200511T140354Z&X-Amz-Expires=300&X-Amz-Signature=c8c6067e0edc4b6c7c38d96725cdb8d4aa2e4f611a519f36f5547ea9c0606e1a&X-Amz-SignedHeaders=host&actor_id=63358485&repo_id=45055693&response-content-disposition=attachment%3B%20filename%3DbalenaEtcher-Setup-1.5.86.exe&response-content-type=application%2Foctet-stream'
rufus = 'https://github.com/pbatard/rufus/releases/download/v3.10/rufus-3.10.exe'

# Social Media
twitter = 'https://www.twitter.com/phillip_hqs'
instagram = 'https://www.instagram.com/phillip.hqs'
instagram2 = 'https://www.instagram.com/phillip.60528'
github = 'https://github.com/philliphqs/hqs.bot'
snapchat = 'https://www.snapchat.com/add/phillip.hqs'
youtube = 'https://www.youtube.com/realphill'
fiverr = 'https://www.fiverr.com/philliphqs'
website = 'https://hqsartworks.me'



async def quick_log(bot, text=None, embed=None):
    import main
    #await bot.get_all_channel().send(text, embed=main.invite)

def run(bot):
    if default == True:
        bot.run(defaultt)
    if developing == True:
        bot.run(developingt)




