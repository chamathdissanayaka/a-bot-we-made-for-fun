import discord
from discord.ext import commands


class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! My latency is {round(self.bot.latency * 1000)}ms")


def setup(bot):
    bot.add_cog(About(bot))
