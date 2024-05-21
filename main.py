import requests
import discord
import json
import datetime
from replit import db

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
      
      

    #stock api code
    if message.content.startswith('$commands'):
      await message.reply()
    if message.content.startswith("$ticker details"):
      if message.content == "$ticker details":
        await message.reply("Enter a stock ticker")
      else:
        ticker = message.content[16:]
        data = requests.get(f'https://api.polygon.io/v1/meta/symbols/{ticker}/company?').text
        for value in data:
          print(value)
    
    if message.content.startswith('$ticker stock'):
      if message.content == '$ticker stock':
        await message.reply("ENTER A STOCK TICKER")
      else:
        ticker = message.content[14:]
        data = requests.get(f'https://api.polygon.io/vX/reference/financials?ticker={ticker}&apiKey=')
        await message.reply(data.text)

    if message.content.startswith('$market holidays'):
      data = requests.get('https://api.polygon.io/v1/marketstatus/upcoming?apiKey=')
      await message.reply(data.text)
    
    if message.content.startswith('$market status'):
      data = requests.get('https://api.polygon.io/v1/marketstatus/now?apiKey=')
      await message.reply(data.text)
    
    if message.content.startswith('$exchanges'):
      data = requests.get('https://api.polygon.io/v3/reference/exchanges?apiKey=')
      print(data.text)
      await message.reply(data.text)

    if message.content.startswith('$daily open'):
      if message.content == '$daily open':
        await message.reply("ENTER A STOCK TICKER")
      else:
        u = datetime.datetime.today()
        J = str(u)
        O = J[:10]
        P = O[8:]
        if int(P) == 1:
          DATE = datetime.datetime.today()
          ticker = message.content[12:]
          data = requests.get(f'https://api.polygon.io/v1/open-close/{ticker}/{DATE}?adjusted=true&apiKey=')
          await message.reply(data.text)
        else:
        #code to remove get yesterdays date
          ticker = message.content[12:]
          r = datetime.datetime.today()
          x = str(r)
          data = x[:10]
          y = data[8:]
          z = int(y)
          x1 = z - 1
          DATE = data[:8] + str(x1)
          print(DATE)
          data = requests.get(f'https://api.polygon.io/v1/open-close/{ticker}/{DATE}?adjusted=true&apiKey=')
          data_text = data.text
          new_data = data_text[36:]
          await message.reply(new_data)
   
#start of the news bot 
    if message.content == '!top headlines america':
      data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=")
      await message.reply(data.text)
    elif message.content == '!top headlines hong kong':
      data = requests.get("https://newsapi.org/v2/top-headlines?country=hk&apiKey=")
      await message.reply(data.text)
    elif message.content == '!top headlines business':
      data = requests.get("https://newsapi.org/v2/top-headlines?category=business")
      await message.reply(data.text)
    else:
      data = requests.get("https://newsapi.org/v2/top-headlines?category=sports")
      await message.reply(data.text)
    
    #everything keyword code
    if message.content == '!everything':
      data = requests.get("https://newsapi.org/v2/everything?country=us")
    

client.run('#client ID')
