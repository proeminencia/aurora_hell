import discord
from discord.ext import commands
import scrapping
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    sincs = await bot.tree.sync()
    print(f"{len(sincs)} comandos sincronizados")
    print("Bot inicializado")

@bot.tree.command(name="show_leaderboard", description="Displays the leaderbord according to the selected")
@app_commands.choices(leaderboard=[
    app_commands.Choice(name='Experience', value=0),
    app_commands.Choice(name='Melee', value=1),
    app_commands.Choice(name='Distance', value=2),
    app_commands.Choice(name='Mage', value=3),
    app_commands.Choice(name='Defense', value=4)
])
async def rank_level(interact:discord.Interaction, leaderboard: app_commands.Choice[int]):
    await interact.response.defer()
    pag1, pag2, pag3, pag4 = scrapping.show_leaderboard(leaderboard.value)
    file1 = discord.File(fp=pag1, filename="rank_page_1.png")
    file2 = discord.File(fp=pag2, filename="rank_page_2.png")
    file3 = discord.File(fp=pag3, filename="rank_page_3.png")
    file4 = discord.File(fp=pag4, filename="rank_page_4.png")
    await interact.followup.send(content=f"{leaderboard.name} Leaderboard requested by {interact.user}")
    await interact.followup.send(file=file1)
    await interact.followup.send(file=file2)
    await interact.followup.send(file=file3)
    await interact.followup.send(file=file4)



bot.run("your_token")
