from discord.ext import commands
import discord
from discord.utils import get

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
        overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        author: discord.PermissionOverwrite(read_messages=True),
        therapist_role: discord.PermissionOverwrite(read_messages=True)
        }
        
        if category is None:
            category = await guild.create_category_channel("Private Rooms")

        channel = await guild.create_text_channel(f"{author}'s-room", category=category, overwrites=overwrites)
        
        await channel.send("Welcome to your Private Room, "+ ctx.message.author.mention)

    @commands.command(name="dir")
    async def dirit(self, ctx, *, arg):
        guild = ctx.message.guild
        await ctx.send(dir(arg))

def setup(bot):
    bot.add_cog(DMHC(bot))