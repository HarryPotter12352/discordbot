import discord
from discord.ext import commands
import random
client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print("Bot is ready")




kball = ["As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "It is certain", "It is decidedly so", "Most likely", "My reply is no", "My sources say no", "Outlook not so good", "Outlook good", "Reply hazy, try again", "Signs point to yes", "Very doubtful", "Without a doubt", "Yes", "Yes - definitely", "You may rely on it"]

@client.command()
async def ball(ctx, question : str):
    await ctx.send (random.choice(kball))


@client.command()
async def av(ctx, member : discord.Member):
    await ctx.send(member.avatar_url)

@client.command()
async def roll(ctx, no1 : float, no2 : float):
    await ctx.send(random.randint(no1,no2))

@client.command()
async def id(ctx, member : discord.Member):
    await ctx.send(member.id)

@client.command()
async def dumb(ctx, member : discord.Member):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{member.mention} is really dumb")
    await member.send(f"{ctx.author} says you are dumb")



@client.command()
@commands.has_role("Moderator")
async def say(ctx,*, content : str):
    await ctx.channel.purge(limit=1)
    await ctx.send(content)


@client.command()
async def embed(ctx, title : str,*, content : str):
    embed = discord.Embed(title=title, description=content, colour = ctx.author.colour)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def askban(ctx, member : discord.Member):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"You wanna get banned {member.mention}?")

@client.command()
@commands.has_permissions(administrator=True)
async def poll(ctx,*, content : str):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=content, description = f"Question by {ctx.author.mention}", colour= ctx.author.colour)
    my_msg = await ctx.send(embed=embed)
    await my_msg.add_reaction("✅")
    await my_msg.add_reaction("❌")


@client.command()
async def add(ctx, no1 : float, no2 : float):
    await ctx.send(no1+no2)

@client.command()
async def subtract(ctx, no1 : float, no2 : float):
    await ctx.send(no1-no2)

@client.command()
async def multiply(ctx, no1 : float, no2 : float):
    await ctx.send(no1*no2)

@client.command()
async def divide(ctx, no1 : float, no2 : float):
    await ctx.send(no1/no2)
    

@client.command()
async def imagine(ctx,*, content : str):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"I can't even imagine {content} bro")

@client.command()
async def flip(ctx):
    response = ["Heads", "Tails"]
    embed = discord.Embed(title="And you rolled.....", description=random.choice(response), colour=ctx.author.colour)
    await ctx.send(embed=embed)

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, person : discord.Member, *, reason=None):
    await person.kick(reason=reason)
    await ctx.send(f'User {person} has been kicked')
    await person.send(f"You were kicked, because of {reason} by {ctx.author}")


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "For being a jerk!"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")


@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"Unbanned: {user.mention}")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit=2):
    await ctx.channel.purge(limit=limit+1)
    await ctx.send(f"Purged {limit} messages")
    await ctx.channel.purge(limit=1)
