import discord
import random
from discord.ext import commands

# 1. Configurar permissões
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# 2. Evento de inicialização
@bot.event
async def on_ready():
    print(f'Bot logado como {bot.user}')

# 3. Comandos de Sorteio
@bot.command()
async def quem(ctx):
    membros = [m for m in ctx.guild.members if not m.bot]
    await ctx.send(f"{ctx.author.mention}, deve ser: {random.choice(membros).mention}")

@bot.command()
async def traidor(ctx):
    membros = [m for m in ctx.guild.members if not m.bot]
    await ctx.send(f"O grande traidor é o(a) {random.choice(membros).mention}! 🐍")

@bot.command()
async def viado(ctx):
    membros = [m for m in ctx.guild.members if not m.bot]
    await ctx.send(f"Hoje o prêmio vai para o(a) {random.choice(membros).mention}! 🌈")

@bot.command()
async def casal(ctx):
    membros = [m for m in ctx.guild.members if not m.bot]
    if len(membros) < 2:
        await ctx.send("Não tem gente suficiente para formar um casal! 😭")
        return
    par = random.sample(membros, 2)
    await ctx.send(f"O novo casal do servidor é: {par[0].mention} e {par[1].mention}! ❤️")

# 4. Comando de Dado (RollEm)
@bot.command()
async def dado(ctx, lados: int = 6):
    await ctx.send(f"🎲 **{ctx.author.name}** rolou um d{lados} e tirou: **{random.randint(1, lados)}**")

# 5. Comando de Limpar
@bot.command()
@commands.has_permissions(manage_messages=True)
async def limpar(ctx, quantidade: int):
    await ctx.channel.purge(limit=quantidade + 1)
    await ctx.send(f"✅ Limpei {quantidade} mensagens!", delete_after=3)

# 6. Comandos com GIFs
@bot.command()
async def beijo(ctx, membro: discord.Member):
    links = ["https://tenor.com/view/megumi-kato-kiss-saekano-aki-tomoya-gif-26277378", "https://tenor.com/view/anime-kiss-gif-11217460416170899513", "https://tenor.com/view/kiss-me-%D0%BB%D1%8E%D0%B1%D0%BB%D1%8E-anime-kiss-intimate-gif-17382422", "https://tenor.com/view/kiss-gif-14808454542484343765"]
    await ctx.send(f"{ctx.author.mention} beijou {membro.mention}! 💋\n{random.choice(links)}")

@bot.command()
async def tapa(ctx, membro: discord.Member):
    links = ["https://tenor.com/view/boy-slap-girl-anime-gif-6921254811684530096", "https://tenor.com/view/anime-slap-mad-gif-16057834", "https://tenor.com/view/anime-girl-anime-japan-slap-slap-gif-gif-12801251263026599500", "https://tenor.com/view/slap-jjk-nicevagg-anime-gif-22368283"]
    await ctx.send(f"{ctx.author.mention} deu um tapa em {membro.mention}! ✋💥\n{random.choice(links)}")

# 7. Respostas Aleatórias para comandos inexistentes
@bot.event
async def on_message(message):
    if message.author == bot.user: return
    if message.content.startswith('!') and not message.content.split(' ')[0][1:] in [c.name for c in bot.commands]:
        respostas = ["Sim! :)", "Não! >:(", "Óbvio! :D", "Nem pense nisso... 😐"]
        await message.channel.send(f"{message.author.mention} {random.choice(respostas)}")
    await bot.process_commands(message)

bot.run('token')
