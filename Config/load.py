import requests, os
from discord.ext import commands as riko
from art import tprint
from Config.config import *

bot = riko.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')

class load:
    def __init__(self):
        global token

        token = self.check_token(auth)

        @bot.event
        async def on_ready():

            self.load_cogs()
            os.system("clear")
            tprint("RikoSan")
            print(f"Ver. 1.0.0 | Prefix: '::' | type ::help for commands")

        bot.run(token, bot=False)


    def check_token(self, authorization):
        headers = {'Content-Type': 'application/json', 'authorization': authorization}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            token = authorization
            return token
        else:
            print("Check Config/config.py")
            print("Please insert your token below:")
            token_input = input()
            token = token_input
            return token

    def load_cogs(self):
        bot.load_extension("riko.main")

