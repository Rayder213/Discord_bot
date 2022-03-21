import discord
from discord import Option
from discord.ext import commands
from get_url import get_url


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[931576011437531136],
                            description='Приветствие')
    @commands.has_permissions(manage_messages=True)
    async def hi(self, ctx):
        return await ctx.respond('Добрейший вечерочек')

    @commands.slash_command(guild_ids=[931576011437531136],
                                description='Запросить видео')
    @commands.has_permissions(manage_messages=True)
    async def vidos(self, ctx, video: Option(str, 'Строка для запроса видео ', required=True)):
        try:
            await ctx.channel.send('одну секунду')
            return await ctx.channel.send(await get_url(video))
        except BaseException as e:
            print(e)
