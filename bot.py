import discord
client = discord.Client()

@client.event
async def on_ready():
    print('谷村ジャスティス：', client.user)

async def on_message(message):
  if message.author == client.user:
      return
async def on_message(message):
     if message.content == '早安':
        await message.channel.send('今日も一日よしリーチ')

client.run('MTAwNjkxNzUwNDMzNTEwMjA1Ng.G3njHh.DG2OUzEEMidMV1lj58f1kdTVx3cX7qVSVFaDKE')