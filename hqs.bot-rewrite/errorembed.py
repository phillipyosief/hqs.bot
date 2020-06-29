# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import discord

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



