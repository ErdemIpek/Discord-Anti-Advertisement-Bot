import discord
import discord.utils
SHILL_CHANNEL = {PASTE THE CHANNEL ID HERE IF YOU ONLY WANT PEOPLE TO SEND INVITES TO A SPESIFIC CHANNEL }

TOKEN = "TOKEN HERE"

client = discord.Client()#initiate bot

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_message(message):
    text_channel = client.get_channel(SHILL_CHANNEL)
    role = discord.utils.find(lambda r: r.name == 'Paste the name of the admin role here so admins can send invites', message.guild.roles)
    if message.channel.id != SHILL_CHANNEL and ("https://discord.gg/" in message.content or "t.me" in message.content) and role not in message.author.roles:
        await message.delete()
        await message.channel.send("{0} advertisement are not allowed in channels other than {1.mention} !".format(message.author.mention,text_channel)) 
        print(f"Message from {message.author} has been deleted!")



client.run(TOKEN)

