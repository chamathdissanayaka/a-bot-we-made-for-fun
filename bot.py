import discord
from discord.ext import commands
import config, os


class BabyshkaContext(commands.Context):
    async def tick(self, value):
        emoji = "\N{WHITE HEAVY CHECK MARK}" if value else "\N{CROSS MARK}"
        try:
            await self.message.add_reaction(emoji)
        except discord.HTTPException:
            pass


class Babyshka(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=".",
            case_insensitive=True,
            owner_ids={652407551849267200, 719797637435621395},
            strip_after_prefix=True,
        )

        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                self.load_extension(filename[:-3])

    async def on_ready(self):
        print(f"{self.user} logged in. | {self.user.id}")

    async def get_context(self, message, *, cls=BabyshkaContext):
        return await super().get_context(message, cls=cls)


bot = Babyshka()
bot.run(config.TOKEN)
