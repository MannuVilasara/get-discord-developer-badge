import discord
from discord.ext import commands
from config import TOKEN

class Mannu(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
    
    async def on_ready(self):
        print("Created By Mannu. GitHub: https://github.com/MannuVilasara")
        print(f"Logged in as {self.user}")
        print(f"Use the below link to add the bot in server")
        print(f"https://discord.com/oauth2/authorize?client_id={self.user.id}&permissions=8&scope=applications.commands+bot")
        await self.tree.sync()



bot = Mannu()

@bot.tree.command(name="badge",description="get the badge")
async def badge(interaction: discord.Interaction):
    embed = discord.Embed(color=discord.Colour.green(),title="Get the badge", description="After running the command wait atleast 24 hours to get the badge. \n\n after 24 hours if u don't get the badge, try running the command again and wait for another 24 hours. \n\n  Make sure this is a community server. \n\n visit https://discord.com/developers/active-developer and follow the on screen instructions to claim the badge \n\n Make sure to star the repo 🌟")
    await interaction.response.send_message(content=f"https://discord.com/developers/active-developer \n https://github.com/MannuVilasara", embed=embed)

if __name__ == "__main__":
    bot.run(token=TOKEN)
