import discord
from discord.ext import commands
import scrapping
import calculations
import guilds
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    sincs = await bot.tree.sync()
    print(f"{len(sincs)} comandos sincronizados")
    print("Bot inicializado")

@bot.tree.command(name="show-leaderboard", description="Displays the leaderbord according to the selected")
@app_commands.describe(leaderboard="Select which leaderboard to display.")
@app_commands.choices(leaderboard=[
    app_commands.Choice(name='Experience', value=0),
    app_commands.Choice(name='Melee', value=1),
    app_commands.Choice(name='Distance', value=2),
    app_commands.Choice(name='Mage', value=3),
    app_commands.Choice(name='Defense', value=4),
])
async def showleaderboard(interact:discord.Interaction, leaderboard: app_commands.Choice[int]):
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

@bot.tree.command(name="stat-calculator-ptraining", description="Calculates useful information about leveling up your stats.")
@app_commands.describe(initial_stat="Current stat")
@app_commands.describe(final_stat="Final stat")
@app_commands.describe(tickrate="Stat XP/h")
async def stat_calculator_ptraining(interact:discord.Interaction,initial_stat:app_commands.Range[int, 55, 999], final_stat:app_commands.Range[int, 56, 1000], tickrate:app_commands.Range[(int, 3600, 14400)]):
    if final_stat <= initial_stat:
        await interact.response.send_message("Final stat must be higher than initial stat.", ephemeral=True)
    else:
        result_calculation = calculations.stat_calculation(initial_stat, final_stat, tickrate)
        file1 = discord.File(fp=result_calculation, filename="calculation.png")
        await interact.response.send_message(file=file1)


@bot.tree.command(name="level-calculator", description="Calculates useful information about leveling up your base.")
@app_commands.describe(initial_level="Current stat")
@app_commands.describe(final_level="Final stat")
async def level_calculator(interact:discord.Interaction, initial_level:app_commands.Range[int, 1, 998], final_level:app_commands.Range[int, 2, 999]):
    if final_level <= initial_level:
        await interact.response.send_message("Final level must be higher than initial level.", ephemeral=True)
    else:
        result_calculation = calculations.level_calculation(initial_level, final_level)
        file1 = discord.File(fp=result_calculation, filename="calculation.png")
        await interact.response.send_message(file=file1)

@bot.tree.command(name="guild-info", description="Shows information about the chosen guild.")
@app_commands.describe(guild_name="Name of the guild")
@app_commands.describe(show="Select if you want to show all members or just online members.")
@app_commands.choices(show=[
    app_commands.Choice(name="All members", value=0),
    app_commands.Choice(name="Online members", value=1)
])
async def guild_info(interact:discord.Interaction, guild_name:str, show: app_commands.Choice[int]):
    await interact.response.defer()
    if show.value == 0:
        status, imagens = guilds.show_members(guild_name)
        if status == 0:
            await interact.followup.send("This guild does not exist or you entered the wrong name.", ephemeral=True)
        else:
            for i, imagem in enumerate(imagens):
                file = discord.File(fp=imagem, filename=f"{guild_name}_members_page_{i}.png")
                await interact.followup.send(file=file)
    elif show.value == 1:
        status, imagens = guilds.show_online(guild_name)
        if status == 0:
            await interact.followup.send("This guild does not exist or you entered the wrong name.", ephemeral=True)
        elif status == 1:
            await interact.followup.send("This guild does not have online members.", ephemeral=True)
        else:
            for i, imagem in enumerate(imagens):
                file = discord.File(fp=imagem, filename=f"{guild_name}_members_page_{i}.png")
                await interact.followup.send(file=file)
    

        
# @bot.tree.command(name="stat-calculator-training", description="Calculates useful information about leveling up your stats.")
# @app_commands.describe(initial_stat="Current stat")
# @app_commands.describe(final_stat="Final stat")
# @app_commands.describe(tickrate="Stat XP/h")

# async def stat_calculator_training(interact:discord.Interaction,initial_stat:app_commands.Range[int, 100, 999], final_stat:app_commands.Range[int, 99, 1000], tickrate:app_commands.Range[(int, 1, 3600)]):
#     if final_stat <= initial_stat:
#         await interact.response.send_message("Final stat must be higher than initial stat.", ephemeral=True)
#     else:
#         result_calculation = calculations.stat_calculation(0, initial_stat, final_stat, tickrate)
#         file1 = discord.File(fp=result_calculation, filename="calculation.png")
#         await interact.response.send_message(file=file1)



bot.run("x")
