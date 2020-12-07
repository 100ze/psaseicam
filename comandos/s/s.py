# Comando !s
# importando módulos 
import random
import discord

# variáveis
gif_nao_url = 'https://cdn.discordapp.com/attachments/768313363024838686/784615962807762964/n0.gif'
gif_sim_url = 'https://cdn.discordapp.com/attachments/768313363024838686/784814372140613642/s0.gif'

async def criaEmbeds(ctx):
    bot_info = await ctx.bot.application_info() 
    embed_cor = discord.Colour(0).from_rgb(245, 137, 61)
    
    return discord.Embed(colour=embed_cor).set_author(
            name = bot_info.name,
            icon_url = bot_info.icon_url
            )

async def comando_s(ctx, pergunta = ''):
    embed = await criaEmbeds(ctx)

    # tratando a mensagem 
    # retirando espaços em branco
    pergunta = pergunta.strip()
    # limpando menções do usuário
    pergunta = discord.utils.escape_mentions(pergunta)
    # adicionando pergunta ao titulo do embed
    embed.title = pergunta

    # recebendo um número aleatório entre de 0 a 1
    resposta = random.randint(0,1)

    if resposta:
        embed.set_footer(text = 'Sim!')
        embed.set_image(url = gif_sim_url)
    else:
        embed.set_footer(text = 'Não.')
        embed.set_image(url = gif_nao_url)

    # marcando e respondendo o usuário que fez a pergunta
    await ctx.send(ctx.author.mention, embed = embed)
