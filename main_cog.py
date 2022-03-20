import discord
from discord import Option
from discord.ext import commands


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[931576011437531136],
                            description='Приветствие')
    @commands.has_permissions(manage_messages=True)
    async def hi(self, ctx):
        return await ctx.respond('Добрейший вечерочек')
