import discord
client = discord.Client()

@client.event
async def on_ready():
    print('谷村ジャスティス：', client.user)

async def on_message(message):
  if message.author == client.user:
      return
  if message.content == '早安':    
        await message.channel.send('今日も一日よしリーチ')

@client.event
async def on_message(message):
     if message.author == client.user:
        return
     if message.content.startswith('秋山駿'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
             await message.channel.send("秋山駿，你算計我！")
        else:
             await message.channel.send(tmp[1]) 

client.run('MTAwNjkxNzUwNDMzNTEwMjA1Ng.GOj-QU.DFblduucdS5rWGlRFG_9XPowEtNnQYGEe321Qc')