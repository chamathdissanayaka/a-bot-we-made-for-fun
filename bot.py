import discord
from discord.ext import commands

bot = commands.Bot(
    command_prefix=".",
    case_insensitive=True,
    owner_ids={652407551849267200, 719797637435621395},
    strip_after_prefix=True,
)

...
