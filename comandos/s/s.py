# Comando !s
# importando módulos 
import random
import discord

async def criaEmbeds(ctx):
    bot_info = await ctx.bot.application_info() 
    embed_cor = discord.Colour(0).from_rgb(245, 137, 61)
    
    return discord.Embed(colour=embed_cor).set_author(
            name = bot_info.name,
            icon_url = bot_info.icon_url
            )

async def comando_s(ctx, pergunta):
    # tratando a mensagem 
    # retirando espaços em branco
    pergunta = pergunta.strip()
    # limpando menções do usuário
    pergunta = discord.utils.escape_mentions(pergunta)

    # recebendo um número aleatório entre de 0 a 1
    resposta = random.randint(0,1)

    if resposta:
        resposta = 'Sim!'
    else:
        resposta = 'Não.'

    # marcando e respondendo o usuário que fez a pergunta
    await ctx.send('{} {} {}'.format(ctx.author.mention, pergunta, resposta))
    #await ctx.send(embed = await criaEmbeds(ctx))
