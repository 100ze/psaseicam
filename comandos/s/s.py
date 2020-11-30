# Comando !s
# importando módulos 
import random

async def criaEmbeds(ctx):
    bot_info = await ctx.bot.application_info() 
    imagem_bot = bot_info.icon_url
    nome_bot = bot_info.name 

    print(nome_bot)
    print(imagem_bot)

async def comando_s(ctx, pergunta):
    await criaEmbeds(ctx)

    # recebendo um número aleatório entre de 0 a 1
    resposta = random.randint(0,1)

    if resposta:
        resposta = 'Sim!'
    else:
        resposta = 'Não.'

    # marcando e respondendo o usuário que fez a pergunta
    await ctx.send('{} {} {}'.format(ctx.author.mention, pergunta, resposta))
