import discord, random, datetime
from discord.ext import commands

# Define channel reader to hide channel id

def read_channel() -> int:
    f = open("channel.txt", "r")
    lines = f.readline()
    return int(lines)
    

class Events(commands.Cog):
    """"Events, no commands"""
    messages = CHANNEL_ID = 0

    def __init__(self, client):
        self.client = client


    # Events
    # @commands.Cog.listener() = @client.event for Cogs

    @commands.Cog.listener()  
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game('Testing on Servers!'))
        print('Bot is ready.')


    # Upon joining server, member gets 'New' Role and Embeded welcoming text.
    @commands.Cog.listener()  
    async def on_member_join(self, ctx):
        # Search for 'New' role

        role = discord.utils.get(ctx.guild.roles, name = "New") 
        await ctx.add_roles(role)

        # Embed 
        embed = discord.Embed(colour=0x8cdee2, description= f"Welcone {ctx.mention} to the server! You are member number {len(list(ctx.guild.members))}!")

        embed.set_thumbnail(url= f"{ctx.avatar_url}")
        embed.set_author(name= f"{ctx.name}", icon_url=f"{ctx.avatar_url}")
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()

        # Find channel id and send it to that channel
        CHANNEL_ID = read_channel()
        channel = self.client.get_channel(id=CHANNEL_ID)

        await channel.send(embed=embed)

        # print(f'{member} has joined the server.')


    @commands.Cog.listener()  
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')


    # Error Checker
    @commands.Cog.listener() 
    async def on_command_error(self, ctx, error):
        try:
            # embed = discord.Embed(title= f'Error in {ctx.command}', colour = 0x43780)
            embed = discord.Embed(title= f'Error in {ctx.command}', 
            description= f'``!{ctx.command.qualified_name} {ctx.command.signature}`` \n{error}',
            colour = 0x800000)

            # embed.add_field(name= f'Error in {ctx.command}', value=f'``{ctx.command.qualified_name} {ctx.command.signature}`` \n{error}')
            embed.set_author(name= f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
        except:
            # embed = discord.Embed(title= f'Error in {ctx.command}', colour = 0xd4af37)
            embed = discord.Embed(title= f'Error in {ctx.command}', 
            description= f'{error}',
            colour = 0x800000)

            embed.set_author(name= f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()

        finally:
            await ctx.send(embed=embed)


           # await ctx.send(f'{error}.')
        # if isinstance(error, commands.CommandNotFound):
        #     await ctx.send('The command cannot be used.')
        # elif isinstance(error, commands.MissingRequiredArgument):
        #     await ctx.send('Please pass in all required arguments.')
        # else:

        # TESTING FOR STATS TRACKER

        # async def update_stats(self):
        #     await self.client.wait_until_ready()

        #     while not self.clientt.is_closed():
            

def setup(client):
    client.add_cog(Events(client))
