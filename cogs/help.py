import discord, datetime, asyncio
from discord.ext import commands

class Help(commands.Cog):
    """Help Formatter"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, *cog):

        if not cog:
            embed = discord.Embed(colour= 0x8de805,title = '**Cogs**')

            cogs_disc = ''

            for x in self.client.cogs:
                cogs_disc += f'``{x}`` - {self.client.cogs[x].__doc__}\n'

            embed.add_field(name= 'Cogs', value=cogs_disc)
            
        else:
            # No COG = HERE
            if len(cog) > 1:
                embed = discord.Embed(colour= 0x800000,title='Error', description='Too many Cogs!')
                # Fix colour to red for error
            else:
                # Finding a specific command module
                found = False
                for x in self.client.cogs:
                    for y in cog:
                        if x == y:
                            embed = discord.Embed(title='Command',colour= 0x8de805)
                            scog_info = ''
                            for command in self.client.get_cog(y).get_commands():
                                if not command.hidden:
                                    scog_info += f'``{command.name}`` - {command.help}\n'
                            
                            embed.add_field(name= f'{cog[0]} Module', value= scog_info)
                            found = True

                if not found:
                    for x in self.client.cogs:
                        for command in self.client.get_cog(x).get_commands():

                            if command.name == cog[0]:
                                embed = discord.Embed(colour= 0x8de805)
                                embed.add_field(name= f'{cog[0]} - {command.help}', value= f'Proper Syntax:\n`!{command.qualified_name} {command.signature}`')

                                found = True

                    if not found:
                        embed = discord.Embed(title= 'Error', description= f'How do you even use ``{cog[0]}``?', colour=0x800000)
                        
                else:
                    await ctx.message.add_reaction(emoji='👍')
                    
       
        embed.set_author(name= f"{ctx.message.author}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))
