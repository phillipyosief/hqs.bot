# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import discord
import botsetup

github_release = 'https://github.com/philliphqs/hqs.bot/releases/tag/'
color = 0x40b9ff
version = 'v2.8'
title = f'hqs.bot {version} - Changelogs'
description = 'Music commands are enabled\n' \
              'Changing folder structure\n'
github = f'{github_release}{version}'

embed = discord.Embed(title=title, description=f'{description}\n'
                                               f'\n'
                                               f'[GitHub Link]({github})', color=color)
embed.set_author(name=botsetup.name, url=botsetup.github_repo, icon_url=botsetup.botlogo)
embed.set_footer(text=botsetup.watermark)