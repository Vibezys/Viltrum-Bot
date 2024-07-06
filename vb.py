import discord
from discord.ext import commands

#define intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

#define vb's prefix
bot = commands.Bot(command_prefix='?', intents=intents)

#trigger word
trigger_word = "realmcode"

#response for trigger word
response_message = "The realmcode will be displayed in the #realmcode, give the Owner time to update and pay for it plz..."

@bot.event
async def on_message(message):
    #ignore trigger word from bot itself
    if message.author == bot.user:
        return
    
    #check if trigger word is in the users message
    if trigger_word in message.content.lower():
        await message.channel.send(response_message)

    #process commands if any are added later
    await bot.process_commands(message)

bot.run('MTI1ODk5NzgwMDMyNzQ1MDc1NQ.GMopq3.ZEm_ZyI3uEGzTvXnBcQDdnLd4iSjYyQeSytdKQ')