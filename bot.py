import discord
import requests
import json
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

    em.set_footer(text='\u200b')
    em.timestamp = datetime.datetime.utcnow()  
    em.set_footer(text='Made By ocryol#8123')
    await ctx.send(embed = em)

client.run("TOKEN HERE")
