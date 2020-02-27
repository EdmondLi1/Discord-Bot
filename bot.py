import discord, random, datetime
import os
from discord.ext import commands
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix= '!')

# REMOVE HELP
client.remove_command("help")

# Define read token from token file, to keep it hidden

def read_token():
    f = open("token.txt", "r")
    lines = f.readline()
    return lines

# Define token variable
token = str(read_token())


# List of commands

@client.command()
@has_permissions(administrator=True)

async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been loaded!')


@client.command()
@has_permissions(administrator=True)

async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been unloaded!')


@client.command()
@has_permissions(administrator=True)

async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been reloaded!')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
