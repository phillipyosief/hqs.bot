# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
import discord
from discord.ext import commands
import setup as botsetup
from library.cog_info import colors
from library.cog_text import about_text as wm
from library.error_embeds import embeds
from library.icons import links
from cogs import addons
import main



class Addons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load_addon(self, ctx, arg):
        for c in main.cogs:
            if arg.lower() == f'{c}':
                await ctx.send('nope')
        try:
            try:
                if arg.lower() == 'music':
                    self.bot.unload_extension('cogs.music')


                self.bot.load_extension(f"addons.{arg}")

                s = discord.Embed(color=colors.mainblue)
                s.set_author(name='Addons', url=botsetup.website, icon_url=links.load)
                cf = 'Couldnt fetch'

                addon = arg
                try:
                    s.add_field(name='Title', value=addons.arg.title)
                except:
                    s.add_field(name='Title', value=cf + ' title')
                try:
                    s.add_field(name='Description', value=addons.arg.author)
                except:
                    s.add_field(name='Description', value=cf + ' description')
                try:
                    s.add_field(name='Author', value=addons.arg.author)
                except:
                    s.add_field(name='Author', value=cf + ' author')
                s.set_footer(text=wm.footer)
                await ctx.send(embed=s)
            except Exception as e:
                fail = discord.Embed(description=f'```{e}```', color=colors.red)
                fail.set_author(name='Couldnt load addon', url=embeds.url, icon_url=links.error)
                fail.set_footer(text=embeds.footer)
                await ctx.send(embed=fail)
                pass

        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    async def unload_addon(self, ctx, arg):
        try:
            try:
                self.bot.unload_extension(f"addons.{arg}")
                if arg.lower() == 'music':
                    self.bot.load_extension('cogs.music')
            except Exception as e:
                fail = discord.Embed(description=f'```{e}```', color=colors.red)
                fail.set_author(name='Couldnt unload addon', url=embeds.url, icon_url=links.error)
                fail.set_footer(text=embeds.footer)
                await ctx.send(embed=fail)
                pass
            s = discord.Embed(color=colors.mainblue)
            s.set_footer(text=wm.footer)
            s.set_author(name='Unload addon', url=botsetup.website, icon_url=links.load)
            await ctx.send(embed=s)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

def setup(bot):
    bot.add_cog(Addons(bot))