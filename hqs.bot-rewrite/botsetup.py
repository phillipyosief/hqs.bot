# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

"""Bot Accounts"""
beta = False  # hqs.bot_beta
default = False  # default token
developing = True  # hqs.bot_developing

"""Disable Commands"""
help = True  # True will disable help
musicna = False  # disable music

"""Information"""
version = ''
prefix = ''
ownerid = 000000  # type the ID of the Owner
botname = 'hqs.bot'  # type the name of the Bot
twitchurl = 'https://twitch.tv/philliphqs'  # type your twitch acc
normalcolor = 0x36393E  # color for Embeds (not for all embeds)
supid = 00000000  # Support channel
botlogo = 'https://cdn.discordapp.com/attachments/629639339453841408/709386725478236250/logo2.png'
support_dc = 'https://discord.com/invite/cXztd9q'
logs = False

discord_info = False

"""Botactivity"""
activity1 = '/invite | hqsartworks.me'
activity2 = '/vote | hqsartworks.me'
activity3 = '/help | hqsartworks.me'
activity4 = 'Current version v2.3 | hqsartworks.me'



"""Invitelink for bot"""
invitebeta = 'https://discord.com/api/oauth2/authorize?client_id=715625980630270024&permissions=8&scope=bot'
invite = 'https://discord.com/api/oauth2/authorize?client_id=699223351138189363&permissions=8&scope=bot'

""""Radio"""
radio1 = ''
radio1_name = ''

"""Social Media"""
twitter = 'https://www.twitter.com/phillip_hqs'
instagram = 'https://www.instagram.com/phillip.hqs'
instagram2 = 'https://www.instagram.com/phillip.60528'
github = 'https://github.com/philliphqs/'
snapchat = 'https://www.snapchat.com/add/phillip.hqs'
youtube = 'https://www.youtube.com/realphill'
fiverr = 'https://www.fiverr.com/philliphqs'
website = 'https://hqsartworks.me'

github_repo = 'https://github.com/philliphqs/hqs.bot'

watermark = 'hqs.bot / by phillip.hqs'

"""API Tokens"""

"""Mailgun"""
mailgunurl = ''
mailgunkey = ''
mailgunmail = ''


"""Genius"""
genius_token = ""


"""Twitter Bot"""
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


"""DiscordBot Tokens"""
betat = ''  # Beta
defaultt = ''  # Default
developingt = ''  # Developing

def run(bot):
    if default == True:
        bot.run(defaultt)
    if developing == True:
        bot.run(developingt)
