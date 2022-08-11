import discord
import asyncio
import re

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content('山駿'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
             await message.channel.send("媽的好爛==")
        else:
             await message.channel.send(tmp[1]) 
    
    if message.content('你好'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
             await message.channel.send("早安您好神室町")
        else:
             await message.channel.send(tmp[1]) 

    if message.content('秋山駿'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
             await message.channel.send("秋山駿，你算計我！")
        else:
             await message.channel.send(tmp[1]) 

    if message.content('早安'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
             await message.channel.send("早安，雖然是很想這麼說啦......我差不多要出去巡邏了，那就待會兒見啦")
        else:
             await message.channel.send(tmp[1]) 

    if message.content('麻將'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
             await message.channel.send("喔？當然沒問題啦，話說在前頭，我可是很強的喔？")
        else:
             await message.channel.send(tmp[1]) 

@client.event
async def on_ready():
    print('谷村ジャスティス：', client.user)
    game = discord.Game('天鳳')
    await client.change_presence(status=discord.Status.online, activity=game) 

client.run('MTAwNjkxNzUwNDMzNTEwMjA1Ng.GZlibs.YlyFvJl4CRhTD0K_PcOVi7SVdwW3iQeAx6lSjI')