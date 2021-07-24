import discord
import TurnMotor
client = discord.Client()
import time


from TurnMotor import TurnMotor

turnMotor = TurnMotor()


@client.event
async def on_ready():
    print("Bot active")

@client.event
async def on_message(message):
    if message.author.bot:
        return;
    if message.content.lower() == "blow":
        turnMotor.run()
        await message.reply("blowing out the candles")
        time.sleep(3)
        turnMotor.stop()
        await message.reply("stopping blowing out candles")

try:
    client.run(open(".key", "r").read())
except:
    open(".key", "w+")
    print("Please enter a discord bot token into the '.key' file")
    
