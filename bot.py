import discord
from discord.ext import commands
import config, os, asyncio


class BabyshkaContext(commands.Context):
    async def tick(self, value):
        emoji = "\N{WHITE HEAVY CHECK MARK}" if value else "\N{CROSS MARK}"
        try:
            await self.message.add_reaction(emoji)
        except discord.HTTPException:
            pass

    async def send(self, content, type=0.3, *args, **kwargs):

        if type:

            async with self.typing():
                await asyncio.sleep(type)
            return await super().send(content=content, *args, **kwargs)
        await super().send(content=content, *args, **kwargs)


class Babyshka(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=".",
            case_insensitive=True,
            owner_ids={652407551849267200, 719797637435621395},
            strip_after_prefix=True,
            intents=discord.Intents.all(),
        )

        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")

    async def on_ready(self):
        print(f"{self.user} logged in. | {self.user.id}")

    async def get_context(self, message, *, cls=BabyshkaContext):
        return await super().get_context(message, cls=cls)


bot = Babyshka()
bot.run(config.TOKEN)
