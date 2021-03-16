import discord
from discord.ext import commands
from keep_alive import keep_alive

client = commands .AutoShardedBot(command_prefix=commands.when_mentioned_or('!'), help_command=None) #prefix

@client.event
async def on_Ready():
  print(f'{client.user} has Awoken!')

@client.command()
async def ban(ctx, user: discord.User):
  guild = ctx.guild 
  mbed = discord.Embed(
    title = 'Successs!',
    descsription = f"(user) has successfully been banned."
  )
  if ctx.author.guild_permissions.ban_members:
   await ctx.send(embed=mbed)
   await guild.ban(user=user)

@client.command()
async def kick(ctx, user: discord.User):
  guild = ctx.guild 
  mbed = discord.Embed(
    title = 'Successs!',
    descsription = f"(user) has successfully been kicked."
  )
  if ctx.author.guild_permissions.kick_members:
   await ctx.send(embed=mbed)
   await guild.kick(user=user)

@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)

@client.command()
async def unban(ctx, user: discord.User):
  guild = ctx.guild
  mbed = discord.Embed(
    title = 'Success!',
    descsription = f"{user} has successfully been unbanned."
  )
  if ctx.author.guild_permissions.ban_members:
    await ctx.send(embed=mbed)
    await guild.unban(user=user)

keep_alive()
client.run('TOKEN')
