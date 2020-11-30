# Comando !s
# importando módulos 
import random

async def c_s(ctx, pergunta):
    # recebendo um número aleatório entre de 0 a 1
    resposta = random.randint(0,1)

    if resposta:
        resposta = 'Sim!'
    else:
        resposta = 'Não.'

    # marcando e respondendo o usuário que fez a pergunta
    await ctx.send('{} {} {}'.format(ctx.author.mention, pergunta, resposta))
