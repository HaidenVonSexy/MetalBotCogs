import discord
from discord.ext import commands

class KarateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @self.bot.event
    async def on_message(self, msg):
        martial_art = [
            'kung foo',
            'tae kwon do',
            'jujutsu',
            'sumo',
            'karate',
            'judo',
            'kendo',
            'tai chi',
            'ninjutsu',
            'ninjago',
        ]

        if msg.author.id == 648659772500869120:
            return

        for art in martial_art:
            if art in msg.contents:
                await msg.channel.send(f"No {art} in the pit!")



def setup(bot):
    bot.add_cog(KarateCog(bot))