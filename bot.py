import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Bot active")

@client.event
async def on_message(message):
    if message.author.bot:
        return;
    if message.content.lower() == "blow":
        #blow()
        await message.reply("blowing out the candles")

try:
    client.run(open(".key", "r").read())
except:
    open(".key", "w+")
    print("Please enter a discord bot token into the '.key' file")
    
