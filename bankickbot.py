import discord
from discord.ext import commands

client = commands .AutoShardedBot(command_prefix=commands.when_mentioned_or('!'), help_command=None)

@client.event
async def on_Ready():
  print(f'{client.user} has Awoken!')

@client.command()
async def ban(ctx, user: discord.User):
  guild = ctx.guild 
  mbed = discord.Embed(
    title = 'Successs!',
    descsription = f"(user) kullanıcı başarıyla banlandı."
  )
  if ctx.author.guild_permissions.ban_members:
   await ctx.send(embed=mbed)
   await guild.ban(user=user)

@client.command()
async def kick(ctx, user: discord.User):
  guild = ctx.guild 
  mbed = discord.Embed(
    title = 'Successs!',
    descsription = f"(user) kullanıcı başarıyla kicklendi."
  )
  if ctx.author.guild_permissions.kick_members:
   await ctx.send(embed=mbed)
   await guild.kick(user=user)

@client.command()
async def unban(ctx, user: discord.User):
  guild = ctx.guild
  mbed = discord.Embed(
    title = 'Success!',
    descsription = f"{user} kullanıcının banı açıldı."
  )
  if ctx.author.guild_permissions.ban_members:
    await ctx.send(embed=mbed)
    await guild.unban(user=user)

keep_alive()
client.run('TOKEN')
