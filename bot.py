import discord
import requests
import json
import random
import datetime, time
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = '!')



@client.command()
async def fakeidentitygenerator(ctx):
    r       = requests.get(f"https://api.namefake.com/")
    fig     = r.json()
    em      = discord.Embed(color=000000)
    fields  = [ 
        {'name': 'Name:',          'value': fig['name']},
        {'name': 'Address:',     'value': fig['address']},
        {'name': 'Latitude:',     'value': fig['latitude']},
        {'name': 'Longitude:',   'value': fig['longitude']},
        {'name': 'Maiden Name:',     'value': fig['maiden_name']},
        {'name': 'Birthdate:',         'value': fig['birth_data']},
        {'name': 'Home phone:',    'value': fig['phone_h']},
        {'name': 'Work phone:',   'value': fig['phone_w']},
        {'name': 'User Agent:',   'value': fig['useragent']},
        {'name': 'IP:',   'value': fig['ipv4']},
        {'name': 'Mac Address:',   'value': fig['macaddress']},
        {'name': 'Company:',   'value': fig['company']},
        {'name': 'Height:',   'value': fig['height']},
        {'name': 'Weight:',   'value': fig['weight']},
        {'name': 'Blood Type:',   'value': fig['blood']},
        {'name': 'Eye Color:',   'value': fig['eye']},
        {'name': 'Hair:',   'value': fig['hair']},
        {'name': 'Favourite Sport:',   'value': fig['sport']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
        if 'female' in fig['pict']:
          em.set_thumbnail(url=random.choice(female))
        elif 'male' in fig['pict']:
          em.set_thumbnail(url=random.choice(male))

    em.set_footer(text='\u200b')
    em.timestamp = datetime.datetime.utcnow()  
    em.set_footer(text='Made By ocryol#8123')
    await ctx.send(embed = em)

female = ["https://i.ibb.co/RB74HGB/image-5.jpg", "https://i.ibb.co/V31dTBG/image-8.jpg", "https://i.ibb.co/rmp46zF/image-11.jpg", "https://i.ibb.co/25t47rn/image-13.jpg", "https://i.ibb.co/Jk6QNfr/image-15.jpg"]


male = ["https://i.ibb.co/86GmJbs/image-4.jpg", "https://i.ibb.co/BgxCKwR/image-9.jpg", "https://i.ibb.co/khsWhg2/image-10.jpg", "https://i.ibb.co/qRnzq9v/image-12.jpg", "https://i.ibb.co/NsDJYz1/image-14.jpg"]

client.run("TOKEN HERE")
