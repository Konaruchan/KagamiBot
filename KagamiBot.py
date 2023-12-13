import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='-')

@bot.command(name='battledice')
async def battledice(ctx, ataque: int, defensa: int):
    potencia = random.randint(1, 6)
    daño_base = (34 - defensa) / 10
    potencia_2 = ((2/3) * daño_base + ataque/10) - defensa/10
    potencia_4 = ((4/3) * daño_base + ataque/10) - defensa/10
    potencia_5 = ((5/3) * daño_base + ataque/10) - defensa/10
    critico = (6/3) * daño_base + ataque/10 - defensa/10

    if potencia == 1:
        resultado = f"¡El atacante falló miserablemente con una potencia de {potencia}!"
    elif potencia == 6:
        resultado = f"¡Golpe crítico! El atacante desató su furia con una potencia de {potencia}!"
    else:
        resultado = f"El atacante logró una potencia de {potencia}."

    await ctx.send(f"{resultado}\nPS perdidos por el atacado: \n"
                   f"Potencia 3: {round(daño_base**3)}\n"
                   f"Potencia 2: {round(potencia_2)}\n"
                   f"Potencia 4: {round(potencia_4)}\n"
                   f"Potencia 5: {round(potencia_5)}\n"
                   f"Golpe Crítico: {round(critico)}")

# token = 'DYI0WtgAb5chH4Rc_DazXcL-DZOeqa24'
# bot.run(token)
