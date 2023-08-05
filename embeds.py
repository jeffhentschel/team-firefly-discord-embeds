import discord
import json
from discord.ext import commands
import os

intents = discord.Intents.default()

with open("embeds.json") as f:
    embed_groups = json.load(f)

bot = commands.Bot(command_prefix='?', intents=intents)

def create_embed(data):
    embed = discord.Embed(
        title=data["title"],
        description=data["description"],
        url=data["link"]
    )
    if "author" in data:
        embed.set_author(name=data["author"])
    if "thumbnail" in data:
        embed.set_thumbnail(url=data["thumbnail"])
    if "fields" in data:
        for field in data["fields"]:
            embed.add_field(name=field["name"], value=field["value"], inline=False)

    return embed

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

    for embed_group in embed_groups:
        print(f"Creating embeds for {embed_group['type']}")
        channel = bot.get_channel(embed_group["channel"])
        for item in embed_group["embeds"]:
            if "id" in item:
                continue
            print(f"Sending embed for {item['title']}")
            await channel.send(embed=create_embed(item))

    quit(0)

DISCORD_KEY = os.environ.get("DISCORD_KEY")
bot.run(DISCORD_KEY)
