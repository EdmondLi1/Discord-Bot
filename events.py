import discord, random
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    # @commands.Cog.listener()  = @client.event for Cogs
    @commands.Cog.listener()  
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game('Testing on Servers!'))
        print('Bot is ready.')


    @commands.Cog.listener()  
    async def on_member_join(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name = "New") 
        await ctx.add_roles(role)

        # print(f'{member} has joined the server.')


    @commands.Cog.listener()  
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')


    # Error Checker
    @commands.Cog.listener() 
    async def on_command_error(self, ctx, error):
        # if isinstance(error, commands.CommandNotFound):
        #     await ctx.send('The command cannot be used.')
        # elif isinstance(error, commands.MissingRequiredArgument):
        #     await ctx.send('Please pass in all required arguments.')
        # else:
        await ctx.send(f'{error}.')

def setup(client):
    client.add_cog(Events(client))