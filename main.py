import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.author) in ["robbbot#6138"]:
      await message.add_reaction('🟪')
    
    if str(message.author) in ["Desert Ham#2846"]:
      await message.add_reaction('<:DS:784463585531265104>')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$darcysux' ) or message.content.startswith('$ds'):
        await message.channel.send('<:DS:784463585531265104>')

    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that  👍')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')  
            
    if message.content.startswith('$commands'):
        channel = message.channel
        await channel.send('$hello, $ds, $darcysux, $commands')       

client.run(os.getenv('TOKEN'))
