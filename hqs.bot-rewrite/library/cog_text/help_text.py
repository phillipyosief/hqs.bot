# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
import discord
from library.icons import links
from library.cog_info import colors
from library.cog_text import about_text as wm
import setup
















title = 'Help'
description = 'Use ``/help <category>`` to see the category commands.\n' \
              'To see all commands type ``/help all``'
fun_title = 'FUN'
fun_description = 'Fun commands'
tools_title = 'TOOLS'
tools_description = 'Tool commands like /wikipedia'
music_title = 'MUSIC'
music_description = 'Music commands'
about_title = 'ABOUT'
about_description = 'About the bot and server'
owner_title = 'OWNER'
owner_description = 'Commands for server owners'
general_title = 'GENERAL'
general_description = 'General commands'
moderation_title = 'MODERATION'
moderation_description = 'Commands for moderation'
games_title = 'GAMES'
games_description = 'All minigames commands'

def help_embed():
    h = discord.Embed(description=description, color=colors.mainblue)
    h.set_author(name='Help', url=setup.website, icon_url=links.help_)
    h.add_field(name=fun_title, value=fun_description)
    h.add_field(name=tools_title, value=tools_description)
    h.add_field(name=music_title, value=music_description)
    h.add_field(name=about_title, value=about_description)
    h.add_field(name=owner_title, value=owner_description)
    h.add_field(name=general_title, value=general_description)
    h.add_field(name=moderation_title, value=moderation_description)
    h.set_footer(text=wm.footer)
    return h


f = discord.Embed(color=colors.fun)
f.set_author(name='Fun', url=setup.website, icon_url=links.giveaway_fun)
f.set_footer(text=wm.footer)



g = discord.Embed(color=colors.general)
g.set_author(name='General', url=setup.website, icon_url=links.info_general)
g.set_footer(text=wm.footer)



m = discord.Embed(color=colors.moderation)
m.set_author(name='Fun', url=setup.website, icon_url=links.team_moderation)
m.set_footer(text=wm.footer)



a = discord.Embed(color=colors.lightblue)
a.set_author(name='About', url=setup.website, icon_url=links.account_about)
a.set_footer(text=wm.footer)



t = discord.Embed(color=colors.tools)
t.set_author(name='Tools', url=setup.website, icon_url=links.tools)
t.set_footer(text=wm.footer)



mu = discord.Embed(color=colors.music)
mu.set_author(name='Music', url=setup.website, icon_url=links.music)
mu.set_footer(text=wm.footer)



o = discord.Embed(color=colors.owner)
o.set_author(name='Owner', url=setup.website, icon_url=links.owner)
o.set_footer(text=wm.footer)



