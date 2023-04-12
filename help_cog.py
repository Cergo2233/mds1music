import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):     
        embed=discord.Embed(color=0xEF7197, title="Список команд:",
        description="\n"
                   "-p + (посилання) - Уввімкнути трек.\n"
                   "-s - Пропустити трек.\n"
                   "-loop - Повторити пісню.\n"
                   "-list - Показати чергу.\n"
                   "-remove - Видалити вказану пісню з черги (використовуйте номер замовлення з -queue).\n"
                   "-pause - Пауза.\n"
                   "-resume - Відновити.\n"
                   "-skipall - Пропустити всі пісні.\n"
                   "-stop - Зупинити програвання та вийти з каналу.\n"
                   "-help - Список команд (це повідомлення).")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))