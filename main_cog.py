from discord import Option
from discord.ext import commands
from get_url import get_url
from get_picture import get_picture
from discord import File

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[931576011437531136],
                            description='Приветствие')
    async def hi(self, ctx):
        return await ctx.respond('Добрейший вечерочек')

    @commands.slash_command(guild_ids=[931576011437531136],
                             description='Запросить видео')
    async def vidos(self, ctx, video: Option(str, 'Строка для запроса видео ', required=True)):
        try:
            await ctx.channel.send('одну секунду')
            return await ctx.channel.send(await get_url(video))
        except BaseException as e:
            print(e)

    @commands.slash_command(guild_ids=[931576011437531136],
                            description='Запросить картинку')
    async def pictures(self, ctx, picture: Option(str, 'Строка для запроса картинки ', required=True)):
        print(1)
        await ctx.channel.send('одну секунду')
        photos = await get_picture(picture)
        if photos:
            pass
            my_photo = File(photos)
            print(my_photo)

            return await ctx.channel.send(file=my_photo)
        return await ctx.channel.send("не удалось получить картинку")
