# importando módulos 
import os
# importando o módulo random
import random
from dotenv import load_dotenv
from discord.ext import commands

# pegando o token e o prefixo do bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('PREFIX')

print(TOKEN)
print(PREFIX)
