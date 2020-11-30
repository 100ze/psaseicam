# importando módulos 
import os
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime

# pegando o token e o prefixo do bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('PREFIX')

# definindo o prefixo do bot e armazenando o objeto 'bot'
bot = commands.Bot(command_prefix='!')

# mostrando algo no terminal quando o client se conectar
@bot.event
async def on_ready():
    nome_bot = bot.user
    hora = datetime.now().strftime('%d/%m/%Y %H:%M') 
    print('{0} se conectou com sucesso :) em: {1}'.format(nome_bot, hora))

bot.run(TOKEN)
