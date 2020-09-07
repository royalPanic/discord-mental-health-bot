from discord.channel import CategoryChannel
from discord.ext import commands
import discord
from discord.utils import get
import discord.abc

class DMHC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="requestroom", aliases=['req'])
    async def request_Room(self, ctx):
        """Command that allows a user to request a private room."""
        guild = ctx.message.guild
        therapist_role = get(guild.roles, name="Counselor")
        category = get(guild.categories, name="Private Rooms")
        author=ctx.author
        authorID = author.id
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),author: discord.PermissionOverwrite(read_messages=True),therapist_role: discord.PermissionOverwrite(read_messages=True)}
        
        if get(guild.channels, name=str(authorID)) is None:

            if category is None:
                category = await guild.create_category_channel("Private Rooms")

            channel = await guild.create_text_channel(str(authorID), category=category, overwrites=overwrites)
        
            await channel.send("Welcome to your Private Room, "+ ctx.message.author.mention)

        else:
            await ctx.send("You already have a private room.")

    @commands.command(name="closeroom", aliases=['close'])
    async def close_room(self, ctx):
        """Command that allows a user to close a private room."""
        guild = ctx.message.guild
        prcatid = get(guild.categories, name="Private Rooms").id
        category = ctx.message.channel.category_id
        channel = ctx.message.channel
        if category == prcatid:
            await channel.delete()
        else:
            await ctx.send("This channel is not a Private Room, cannot delete.")

def setup(bot):
    bot.add_cog(DMHC(bot))