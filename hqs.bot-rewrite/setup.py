# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

"""Bot Accounts"""
beta = False  # Beta bot
default = False  # Default bot
developing = True  # Test bot (developing)

"""Bot properties"""
version = 'v3.0'  # type version
prefix = '/'  # set bot prefix
test_prefix = '#'
botname = 'hqs.bot'  # bot name
ownerid = 629068960482066432
donate = 'https://www.tipeeestream.com/hqsartworks/donation'
logo = 'https://raw.githubusercontent.com/philliphqs/philliphqs.github.io/master/icons/logo.png'
website_solution = 'https://hqsartworks.me/errorsolution'
reportmail = 'contact@hqsartworks.me'

"""Channels"""
display_server = True
display_commands = True
display_prefix = True
display_members = True

display_server_channel = 726219856319479889
display_commands_channel = 726219924367999007
display_prefix_channel = 726219986502418452
display_members_channel = 726210333185933344

"""Modes"""
discord_info = True

"""Bot activity"""
activity1 = '/invite | hqsartworks.me'
activity2 = '/vote | hqsartworks.me'
activity3 = '/help | hqsartworks.me'
activity4 = f'Current version v{version} | hqsartworks.me'

"""Invitelink for bot"""
invite_beta = 'https://discord.com/api/oauth2/authorize?client_id=715625980630270024&permissions=8&scope=bot'
invite_developing = ''
invite = 'https://discord.com/api/oauth2/authorize?client_id=699223351138189363&permissions=8&scope=bot'

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
support_discord = 'https://discord.com/invite/cXztd9q'
donate = 'https://www.tipeeestream.com/hqsartworks/donation'

"""API Tokens"""
mailgunurl = ''  # Mailgun details
mailgunkey = ''   # Mailgun details
mailgunmail = ''    # Mailgun details

genius_token = ""   # Genius details

consumer_key = ""  # Twitter bot details
consumer_secret = ""  # Twitter bot details
access_token = ""   # Twitter bot details
access_token_secret = ""   # Twitter bot details

rapidapi_key = ""




"""Tokens"""
betat = ''  # Beta
defaultt = ''
developingt = ''

def run(bot):
    if default == True:
        bot.run(defaultt)
    if developing == True:
        bot.run(developingt)