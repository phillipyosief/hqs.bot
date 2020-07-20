# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
import discord
from library.error_embeds import embeds_text
from library.icons import links

name = 'Report this error'
footer = 'Report commands with /report'
url = 'https://hqsartworks.me/bugreport'

"""Not available error"""
notavailable = discord.Embed(title=embeds_text.na_title,
                             description=embeds_text.na_description,
                             color=embeds_text.na_color)
notavailable.set_author(name=name, url=url, icon_url=links.error)
notavailable.set_footer(text=footer)

"""No args error"""
noargs = discord.Embed(title=embeds_text.noargs_title,
                       description=embeds_text.noargs_description,
                       color=embeds_text.noargs_color)
noargs.set_author(name=name, url=url, icon_url=links.error)
noargs.set_footer(text=footer)

"""No user error"""
nouser = discord.Embed(title=embeds_text.nu_title,
                       description=embeds_text.nu_description,
                       color=embeds_text.nu_color)
nouser.set_author(name=name, url=url, icon_url=links.error)
nouser.set_footer(text=footer)

"""No role error"""
norole = discord.Embed(title=embeds_text.nr_title,
                       description=embeds_text.nr_description,
                       color=embeds_text.nr_color)
norole.set_author(name=name, url=url, icon_url=links.error)
norole.set_footer(text=footer)

"""No channel error"""
nochannel = discord.Embed(title=embeds_text.nc_title,
                          description=embeds_text.nc_description,
                          color=embeds_text.nc_color)
nochannel.set_author(name=name, url=url, icon_url=links.error)
nochannel.set_footer(text=footer)

"""No permissions error"""
nopermissions = discord.Embed(title=embeds_text.np_title,
                              description=embeds_text.np_description,
                              color=embeds_text.np_color)
nopermissions.set_author(name=name, url=url, icon_url=links.error)
nopermissions.set_footer(text=footer)

"""Bot no permission"""
nobotpermissions = discord.Embed(title=embeds_text.nbp_title)
nobotpermissions.set_author(name=name, url=url, icon_url=links.error)
nobotpermissions.set_footer(text=footer)

"""Join a channel"""
j = discord.Embed(title=embeds_text.j_title, description=embeds_text.j_description)
j.set_author(name=name, url=url, icon_url=links.error)
j.set_footer(text=footer)

"""API Errors"""

"""No city error"""
nocity = discord.Embed(title=embeds_text.ncity_title,
                       description=embeds_text.ncity_description,
                       color=embeds_text.ncity_color)
nocity.set_author(name=name, url=url, icon_url=links.error)
nocity.set_footer(text=footer)



