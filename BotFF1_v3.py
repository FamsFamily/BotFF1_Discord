import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def he(ctx, count_he = 3):
    await ctx.send("he" * count_he)

@bot.command()
async def wk(ctx, count_wk = 3):
    await ctx.send("wk" * count_wk)

@bot.command()
async def hi(ctx, count_hi = 3):
    await ctx.send("hi" * count_hi)

@bot.command()
async def ha(ctx, count_ha = 3):
    await ctx.send("ha" * count_ha)

@bot.command()
async def hiks(ctx, count_hiks = 3):
    await ctx.send("hiks " * count_hiks)

@bot.command()
async def ho(ctx, count_ho = 3):
    await ctx.send("ho" * count_ho)

@bot.command()
async def hu(ctx, count_hu = 3):
    await ctx.send("hu" * count_hu)

@bot.command()
async def uhuk(ctx, count_uhuk = 3):
    await ctx.send("uhuk " * count_uhuk)

bot.run("TOKEN RAHASIA ADA DI SINI")
