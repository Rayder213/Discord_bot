import discord
from discord import Bot

from main_cog import MainCog
from data.config import TOKEN


class my_bot(Bot):
    async def on_ready(self):
        pass


MyBot = my_bot(intens=discord.Intents().all())
MyBot.add_cog(MainCog(MyBot))
MyBot.run(TOKEN)


