import discord, random, datetime
from discord.ext import commands


class Commands(commands.Cog):
    """Commands for everyone"""
    def __init__(self, client):
        self.client = client
        self.messages = 0


    # Commands
    # self not needed for member objects*
    @commands.command(aliases = ['Ping'])
    async def ping(self, ctx) -> str:
        """Outputs 'Pong!' and the Bot's Ping
        Aliases = Ping
        """
        # if ctx[0] != '!ping':
        #     raise Exception(commands.BadArgument)
        # else:
        await ctx.send(f'Pong! ``{round(self.client.latency * 1000)}ms``')
        # await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

        
    # Aliases make so that command map to more than one root command 
    # Ex: !clement = !clements = !zhang
    # O: Your mark isn\'t looking very good right now.

    @commands.command(aliases = ['clements', 'zhang'])
    async def clement(self,ctx):
        await ctx.send('Your mark isn\'t looking very good right now.')


    @commands.command()
    async def clear(self, ctx, amount = 3):
        await ctx.channel.purge(limit = amount + 1)


    @commands.command(aliases= ['whatDoYouThink', 'Think'])
    async def think(self, ctx, *, prompt):
        responses = [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]

        await ctx.send(f'Question: {prompt}\nAnswer: {random.choice(responses)}')


    @commands.command()
    async def insult(self, ctx, members : commands.Greedy[discord.Member], amount=1):
        insults = [ 'shut up.',
                    'isn\'t looking very good right now.',
                    'let out a loud one.',
                    'belongs in GLE1O9.',
                    'fang pi.',
                    'is feeding ahlie.',
                    'cannot do pronounce three correctly.',
                    'got a 70 on geo.',
                    'loves Ryerson!']

        if amount >= 5: amount = 5

        for iterations in range(amount):
            for member in members:
                await ctx.send(f'{member.mention} {random.choice(insults)}')


    @commands.Cog.listener()
    async def on_message(self, message):
        self.messages += 1


    @commands.command()
    async def stats(self, ctx):
        await ctx.send(f'Since Discord Bot was on, {self.messages} messages were sent.')


def setup(client):
    client.add_cog(Commands(client))
