import discord
from discord.ext import commands, tasks
import scraper


TOKEN = <insert token>
CHANNEL_ID = <insert channel id>
keywords = []

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.listen()
async def on_ready():
    doJobSearch.start()

@tasks.loop(hours=24)
async def doJobSearch():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    toRet = scraper.split_string_by_length(scraper.getJobs(keywords))
    for message in toRet:
        await channel.send(message)

@bot.command(help="add keywords to scrape for\nwords should be input separated by a ',' \ni.e. 'help, 'software engineer''")
async def ak(ctx, keyword: str):
    for word in keyword.split(','):
        keywords.append(word)
    await ctx.send(f"{keywords}")
    
@bot.command(help="view keywords")
async def vk(ctx):
    await ctx.send(f"{keywords}")

@bot.command(help="remove all keywords")
async def ck(ctx):
    keywords.clear()
    await ctx.send(f"{keywords}")

@bot.command(help="remove specific keyword or list of keywords, \nwords should be input separated by a ',' \ni.e. 'help, software engineer'")
async def rk(ctx, keyword):
    for word in keyword.split(','):
        keywords.remove(word)
    await ctx.send(f"{keywords}")
  
@bot.command(help="manually trigger job search")
async def js(ctx):
    toRet = scraper.split_string_by_length(scraper.getJobs(keywords))
    for message in toRet:
        await ctx.send(message)
        
bot.run(TOKEN)