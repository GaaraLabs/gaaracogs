import discord

from redbot.core import commands

class support(commands.Cog):

    """My custom cog"""

    @commands.command()

    async def support(self, ctx):

        """Gives support server and wiki link."""

        # Your code will go here

        await ctx.send("**Link for support server** \n\nhttps://discord.gg/u4ZnVe4rQv")
