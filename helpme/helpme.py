import discord

from redbot.core import commands

class helpme(commands.Cog):

    """My custom cog"""

    @commands.command()

    async def helpme(self, ctx):

        """Gives you list of all commands the bot has."""

        embed = discord.Embed(
                title="Error",
                description="Modmail functioning guild not found.",
                color=self.bot.error_color,
            )
            await ctx.send(embed=embed)
