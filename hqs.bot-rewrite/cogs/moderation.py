# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#
from discord.ext import commands
import discord
from library.icons import links
from library.cog_info import colors
from library.cog_text import about_text as wm
import setup as botsetup
from library.error_embeds import embeds
from datetime import datetime


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, target: discord.Member or discord.Guild, args):
        try:
            ban = discord.Embed(description=f'You are banned from {ctx.guild.id}\n'
                                            f'Reason:'
                                            f'```{args}```', color=colors.red)
            ban.set_author(name='Ban', url=botsetup.website, icon_url=links.ban)
            ban.set_footer(text=wm.footer)

            succes = discord.Embed(description=f'View more information with\n'
                                               f'``/logs {target.id}``', color=colors.lightgreen)
            succes.add_field(name='Moderator', value=f'{ctx.author.mention}', inline=False)
            succes.add_field(name='Reason', value=f'{args}', inline=False)
            succes.add_field(name='Banned', value=f'{target}', inline=False)
            succes.add_field(name='Banned ID', value=f'{target.id}', inline=False)
            succes.set_author(name=f'Banned {target}', url=botsetup.website, icon_url=links.ban)
            succes.set_footer(text=wm.footer)

            try:
                await target.send(embed=ban)
            except Exception as n:
                m = discord.Embed(description=f'Cant write ban message to {target.mention}\n', color=colors.red)
                m.set_author(name='Report this Error', url=botsetup.website_solution, icon_url=links.error)
                m.set_footer(text=embeds.footer)
                await ctx.send(embed=m)

            await target.ban(reason=f'View more information about this ban with /logs {target.id}')

            try:
                try:
                    with open(f'users/simple_logs/{target.id}_{ctx.guild.id}', 'a') as a:
                        now = datetime.now()
                        time = now.strftime("%d/%m/%Y %H:%M:%S")
                        a.writelines(f' \n'
                                     f'Information of ban:\n'
                                     f'Time: {time}\n'
                                     f'Moderator: {ctx.author}\n'
                                     f'Moderator ID: {ctx.author.id}\n'
                                     f'Banned: {target}\n'
                                     f'Banned ID: {target.id}\n'
                                     f'Reason:\n'
                                     f'{args}\n'
                                     f' \n')
                except:
                    with open(f'users/simple_logs/{target.id}_{ctx.guild.id}', 'w') as a:
                        now = datetime.now()
                        time = now.strftime("%d/%m/%Y %H:%M:%S")
                        a.writelines(f'Information of ban:\n'
                                     f'Time: {time}\n'
                                     f'Moderator: {ctx.author}\n'
                                     f'Moderator ID: {ctx.author.id}\n'
                                     f'Banned: {target}\n'
                                     f'Banned ID: {target.id}\n'
                                     f'Reason:\n'
                                     f'{args}\n'
                                     f' \n')
            except Exception as u:
                with open(f'users/simple_logs/{target.id}_{ctx.guild.id}', 'w') as a:
                    a.writelines(f'Error while writing:\n'
                                 f'{a}\n'
                                 f'Report it with /report')

            await ctx.send(embed=succes)
        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, target: discord.Member or discord.Guild, args):
        try:
            kick = discord.Embed(description=f'You are kicked from {ctx.guild.id}\n'
                                            f'Reason:'
                                            f'```{args}```', color=colors.red)
            kick.set_author(name='Kick', url=botsetup.website, icon_url=links.kick)
            kick.set_footer(text=wm.footer)

            succes = discord.Embed(description=f'View more information with\n'
                                               f'``/logs {target.id}``', color=colors.lightgreen)
            succes.add_field(name='Moderator', value=f'{ctx.author.mention}', inline=False)
            succes.add_field(name='Reason', value=f'{args}', inline=False)
            succes.add_field(name='Kicked', value=f'{target}', inline=False)
            succes.add_field(name='Kicked ID', value=f'{target.id}', inline=False)
            succes.set_author(name=f'Kicked {target}', url=botsetup.website, icon_url=links.kick)
            succes.set_footer(text=wm.footer)

            try:
                await target.send(embed=kick)
            except Exception as n:
                m = discord.Embed(description=f'Cant write kick message to {target.mention}\n', color=colors.red)
                m.set_author(name='Report this Error', url=botsetup.website_solution, icon_url=links.error)
                m.set_footer(text=embeds.footer)
                await ctx.send(embed=m)

            await target.kick(reason=f'View more information about this kick with /logs {target.id}')

            try:
                try:
                    with open(f'users/simple_logs/{target.id}_{ctx.guild.id}', 'a') as a:
                        now = datetime.now()
                        time = now.strftime("%d/%m/%Y %H:%M:%S")
                        a.writelines(f'Information of kick:\n'
                                     f'Time: {time}\n'
                                     f'Moderator: {ctx.author}\n'
                                     f'Moderator ID: {ctx.author.id}\n'
                                     f'Kicked: {target}\n'
                                     f'Kicked ID: {target.id}\n'
                                     f'Reason:\n'
                                     f'{args}\n'
                                     f' \n')
                except:
                    with open(f'users/simple_logs/{target.id}_{ctx.guild.id}', 'w') as a:
                        now = datetime.now()
                        time = now.strftime("%d/%m/%Y %H:%M:%S")
                        a.writelines(f'Information of kick:\n'
                                     f'Time: {time}\n'
                                     f'Moderator: {ctx.author}\n'
                                     f'Moderator ID: {ctx.author.id}\n'
                                     f'Kicked: {target}\n'
                                     f'Kicked ID: {target.id}\n'
                                     f'Reason:\n'
                                     f'{args}\n'
                                     f' \n')
            except Exception as u:
                with open(f'users/simple_logs/{target.id}_{ctx.guild.id}', 'w') as a:
                    a.writelines(f'Error while writing:\n'
                                 f'{a}\n'
                                 f'Report it with /report')

            await ctx.send(embed=succes)

        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=100):
        try:
            succes = discord.Embed(color=colors.lightgreen)
            succes.set_author(name=f'Cleared {amount} messages', url=botsetup.website, icon_url=links.clear)
            succes.add_field(name='Moderator', value=f'{ctx.author.mention}', inline=False)
            succes.add_field(name='Moderator ID', value=f'{ctx.author.id}', inline=False)
            succes.add_field(name='Channel', value=f'{ctx.message.channel.mention}', inline=False)
            succes.add_field(name='Channel ID', value=f'{ctx.message.channel.id}', inline=False)
            succes.set_footer(text=wm.footer)

            channel = ctx.message.channel
            messages = []
            async for message in channel.history(limit=amount):
                messages.append(message)
            await channel.delete_messages(messages)

            await ctx.send(embed=succes)
            try:
                try:
                    with open(f'users/simple_logs/{ctx.author.id}_{ctx.guild.id}', 'a') as a:
                        now = datetime.now()
                        time = now.strftime("%d/%m/%Y %H:%M:%S")
                        a.writelines(f'Information of clear:\n'
                                     f'Time: {time}\n'
                                     f'Moderator: {ctx.author}\n'
                                     f'Moderator ID: {ctx.author.id}\n'
                                     f'Cleared messages: {amount}\n'
                                     f'Channel: {ctx.message.channel}\n'
                                     f' \n')
                except:
                    with open(f'users/simple_logs/{ctx.author.id}_{ctx.guild.id}', 'w') as a:
                        now = datetime.now()
                        time = now.strftime("%d/%m/%Y %H:%M:%S")
                        a.writelines(f'Information of clear:\n'
                                     f'Time: {time}\n'
                                     f'Moderator: {ctx.author}\n'
                                     f'Moderator ID: {ctx.author.id}\n'
                                     f'Cleared messages: {amount}\n'
                                     f'Channel: {ctx.message.channel}\n'
                                     f' \n')

            except Exception as u:
                with open(f'users/simple_logs/{ctx.author.id}_{ctx.guild.id}', 'w') as a:
                    a.writelines(f'Error while writing:\n'
                                 f'{a}\n'
                                 f'Report it with /report')

        except Exception as e:
            fail = discord.Embed(description=f'```{e}```', color=colors.red)
            fail.set_author(name='Report this Error', url=embeds.url, icon_url=links.error)
            fail.set_footer(text=embeds.footer)
            await ctx.send(embed=fail)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def logs(self, ctx, target: discord.Member or discord.Guild):
        try:
            try:
                with open(f'users/simple_logs/{target.id}_{ctx.guild.id}', 'r') as r:
                    read = r.read()
                logs = discord.Embed(description=f'```{read}```', color=colors.lightgreen)
                logs.set_author(name=f'Logs from {target.mention}', url=botsetup.website, icon_url=links.logs)
                logs.set_footer(text=wm.footer)
                await ctx.send(embed=logs)
            except:
                dm = discord.Embed(description=f'Ive send {ctx.author.mention} an message', color=colors.lightgreen)
                dm.set_author(name=f'Logs from {target.mention}', url=botsetup.website, icon_url=links.logs)
                dm.set_footer(text=wm.footer)

                with open(f'users/simple_logs/{target.id}_{ctx.guild.id}', 'r'):
                    await ctx.author.send(file=discord.File(f'users/simple_logs/{target.id}_{ctx.guild.id}'))

                await ctx.send(embed=dm)

                prv = discord.Embed(description='The logs are to big to send in Discord\n'
                                                'It will cleared in 5 seconds\n', color=colors.lightgreen)
                prv.set_author(name=f'Logs from {target.mention}', url=botsetup.website, icon_url=links.logs)
                prv.set_footer(text=wm.footer)

                await ctx.author.send(embed=prv)


                with open(f'users/simple_logs/{target.id}_{ctx.guild.id}', 'w') as d:
                    d.write(f'Sent logs to moderator: {ctx.author}\n'
                            f'Moderator ID: {ctx.author.id}\n'
                            f'\n')

        except FileNotFoundError as e:
            n = discord.Embed(title=f'No logs 📜',
                              description=f'The bot doesnt have recorded any\n'
                                          f'commands from this user (check the ID)',
                              color=colors.red)
            n.set_author(name=embeds.name, url=embeds.url, icon_url=links.error)
            n.set_footer(text=embeds.footer)
            await ctx.send(embed=n)


    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.noargs)
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=embeds.nobotpermissions)

    @logs.error
    async def logs_error(self, ctx, error):
        if isinstance(error, FileNotFoundError):
            n = discord.Embed(title=f'No logs 📜',
                              description=f'The bot doesnt have recorded any\n'
                                          f'commands from this user (check the ID)',
                              color=colors.red)
            n.set_author(name=embeds.name, url=embeds.url, icon_url=links.error)
            n.set_footer(text=embeds.footer)
            await ctx.send(embed=n)




def setup(bot):
    bot.add_cog(Moderation(bot))