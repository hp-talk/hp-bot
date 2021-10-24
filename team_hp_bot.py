from discord.ext import commands

bot = commands.Bot(command_prefix='..', description='A simple Discord bot')

token = '<YOUR_TOKEN_HERE>'

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(token)
