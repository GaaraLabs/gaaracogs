from redbot.core import commands

class Mycog(commands.Cog):

    """My custom cog"""

    @commands.command()

    async def vote(self, ctx):

        """This does stuff!"""

        # Your code will go here

        await ctx.send("[Click Here To Vote Me](https://top.gg/bot/732916004656513077)")
