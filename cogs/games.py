import discord, random
from discord.ext import commands

class Games(commands.Cog):
    """Games on bot"""
    def __init__(self, client):
        self.client = client

    @commands.command(aliases= ['random'])
    async def roll(self,ctx, maxNum : int):
        number = random.randint(1,maxNum)
        await ctx.send(f'The number {number} was rolled.')
  
def setup(client):
    client.add_cog(Games(client))
