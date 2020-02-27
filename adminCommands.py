import discord, random
from discord.ext import commands
from discord.ext.commands import has_permissions

class AdminCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)

    async def makeAdmin(self, ctx, members : commands.Greedy[discord.Member]):
        for member in members:
            role = discord.utils.get(ctx.guild.roles, name='Admin Role')
            await member.add_roles(role)
            await ctx.send(f'{member.mention} was given Admin.')


    # async def makeAdmin(self, ctx, member : discord.Member):
    #     role = discord.utils.get(self.member.guild.roles, name='Admin Role')
    #     await self.member.add_roles(role)
        


    @commands.command()
    @has_permissions(administrator=True)

    async def removeAdmin(self, ctx, members: commands.Greedy[discord.Member]):
        for member in members:
            role = discord.utils.get(ctx.guild.roles, name='Admin Role')
            await member.remove_roles(role)
            await ctx.send(f'{member.mention} was removed of Admin.')



    # Adding Roles to people(s)

    @commands.command(aliases=['addRole'], description='Adds a given role, Admin Role is forbidden in this.')
    @has_permissions(administrator=True)

    async def addRoles(self, ctx, members: commands.Greedy[discord.Member], roles : commands.Greedy[discord.Role]):
        ADMIN = discord.utils.get(ctx.guild.roles, name = 'Admin Role')

        for member in members:
            for role in roles:

                new_role = discord.utils.get(ctx.guild.roles, name = str(role)) # str(role)
                
                if new_role == ADMIN:
                    await ctx.send(f'Cannot use addRoles command to give admin, please try a valid role.')
                else:
                    await member.add_roles(new_role)
                    await ctx.send(f'{member.mention} was granted {new_role}.')



    # Removing 'x' amount of roles
    
    @commands.command(aliases=['removeRole'], description='Deletes a given role, Admin Role is forbidden in this.')
    @has_permissions(administrator=True)

    async def removeRoles(self, ctx, members: commands.Greedy[discord.Member], roles : commands.Greedy[discord.Role]):
        ADMIN = discord.utils.get(ctx.guild.roles, name = 'Admin Role')

        for member in members:
            for role in roles:

                new_role = discord.utils.get(ctx.guild.roles, name = str(role)) # str(role)
                
                if new_role == ADMIN:
                    await ctx.send(f'Cannot use addRoles command to remove admin, please try a valid role.')
                else:
                    await member.remove_roles(new_role)
                    await ctx.send(f'{member.mention} lost {new_role}.')

    # Killing bot commands 

    @commands.command()
    @has_permissions(administrator=True)

    async def kill(self, ctx):
        responces = [   'I\'ve been slain.',
                        'Who unplugged the cord?',
                        'Ima head out.',
                        'Peace!']

        await ctx.send(f'{random.choice(responces)}')
        await ctx.bot.close()

    # async def deleteAdmin(self, ctx, member : discord.Member):
    #     role = discord.utils.get(ctx.guild.roles, name ="Admin Role") 
    #     await ctx.remove_roles(member, role)
    #     await ctx.send(f'{member.mention} was taken off Admin')


    # Commands relating to removing someone from server
    # !kick, !ban and !unban

    @commands.command()
    @has_permissions(administrator=True)
    async def kick(self, ctx, members : commands.Greedy[discord.Member], *, reason : str=None):
        for member in members:
            if member == ctx.message.author:
                await ctx.send(f'You cannot kick yourself {ctx.message.author.mention}.')
            elif member.guild_permissions.administrator:
                await ctx.send(f'Kicking {member.mention} is illegal because they are also Admin.')
            else:
                await member.kick(reason=reason)
                await ctx.send(f'{member.mention} has been kicked.')
        

    @commands.command()
    @has_permissions(administrator=True)
    async def ban(self, ctx, members :commands.Greedy[discord.Member]):
        for member in members:
            if member == ctx.message.author:
                await ctx.send(f'Please, you cannot ban yourself {ctx.message.author.mention}.')
            elif member.guild_permissions.administrator:
                await ctx.send(f'Banning {member.mention} causes an error because he has Admin.')
            else:
                await member.ban(reason= None)
                await ctx.send(f'{member.mention} has been banned.')


    @commands.command()
    @has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_members = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_members:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return


def setup(client):
    client.add_cog(AdminCommands(client))
