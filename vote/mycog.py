import discord

from redbot.core import commands

class vote(commands.Cog):

    """My custom cog"""

    @commands.command()

    async def vote(self, ctx):

        """Gives you link to vote bot."""

        # Your code will go here

        await ctx.send("Click on This link to vote me 🙃\n\nhttps://top.gg/bot/732916004656513077")
