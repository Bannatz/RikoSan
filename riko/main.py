import discord, requests, pyfiglet, datetime, aiohttp, urllib3, asyncio, praw, random, json
from Config.config import *
from discord.ext import commands as riko
from termcolor import colored
bot = riko.Bot(command_prefix=prefix, self_bot=True)
#bot.remove_command("help")

Output = "[Error] = "

class Main(riko.Cog):
    def __init__(self, bot):
        self.bot = bot

    @riko.command()
    async def ascii(self, ctx, args):
        await ctx.message.delete()
        text = pyfiglet.figlet_format(args)
        await ctx.send(f'''{text}''')

    @riko.command()
    async def housechanger(self, ctx, house):
        await ctx.message.delete()
        request = requests.session()
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        global payload

        if house == "bravery":
            payload = {'house_id': 1}
            color = "purple"
        elif house == "brilliance":
            payload = {'house_id': 2}
            color = "red"
        elif house == "balance":
            payload = {'house_id': 3}
            color = "green"
        try:
            requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload)
            print(colored(f"Successfully changed your Hypesquad house to {house}", f"{color}"))
        except:
            print(colored(f"Failed to set your Hypesquad House to {house}."))

    @riko.command()
    async def help(self, ctx, category=None):
        await ctx.message.delete()
        if category is None:
            embed = discord.Embed(timestamp=ctx.message.created_at)
            embed.set_author(name="RikoSan Self-Bot | Prefix: " + str(bot.command_prefix))
            embed.set_image(url="https://static.wixstatic.com/media/8e41ed_670d7497312b4e2cb58cdd14b045f5bd.gif")
            embed.add_field(name="Reddit Commands", value="Shows all Reddit Commands and allows you to Post Memes, Hentai. You can use your own Subreddit!")
            embed.add_field(name="Emotions Commands", value="Allows you to Cuddle/Hug/Kiss/Fuck somebody you like!")
            embed.add_field(name="User Info", value="Sends the User information")
            embed.add_field(name="Troll Stuff", value="Troll Commands")
            await ctx.send(embed=embed)
        elif str(category).lower() == "reddit":
            embed = discord.Embed(timestamp=ctx.message.created_at)
            embed.set_author(name="RikoSan Self-Bot | Prefix: " + str(bot.command_prefix))
            embed.add_field(name="sub", value="Sends an Image from an Subreddit you chose!")
            embed.add_field(name="hentai", value="Sends Hentai")
            await ctx.send(embed=embed)
        elif str(category).lower() == "user":
            embed = discord.Embed(timestamp=ctx.message.created_at)
            embed.set_author(name="RikoSan Self-Bot | Prefix: " + str(bot.command_prefix))
            embed.add_field(name="pfp", value="Get the Profile Picture of the User!")
            embed.add_field(name="joined", value="Get the Creation Date from the User!")
            embed.add_field(name="info", value="Get Information about the User")
            await ctx.send(embed=embed)
        elif str(category).lower() == "emotions":
            embed = discord.Embed(timestamp=ctx.message.created_at)
            embed.set_author(name="RikoSan Self-Bot | Prefix: " +str(bot.command_prefix))
            embed.add_field(name="hug", value="Hug someone you like!")
            embed.add_field(name="kiss", value="Kiss Someone you Like/Love")
            embed.add_field(name="cry", value="Cry Baby")
            embed.add_field(name="fuck", value="Fuck someone you Love/like")
            embed.add_field(name="slap", value="Slap someone you love/like")
            embed.add_field(name="cuddle", value="Cuddle with Someone you Like/Love")
            embed.add_field(name="angry", value="Be Angry")
            embed.add_field(name="smile", value="Smile :)")
            embed.add_field(name="baka", value="Send A Baka to your Friend!")
            embed.add_field(name="lick", value="Lick Somebody!")
            embed.add_field(name="bite", value="Bite Somebody!")
            embed.add_field(name="kick", value="Kick Somebody you hate!")
            embed.add_field(name="simp", value="Tell Somebody that hes an Simp!")
            embed.add_field(name="adore", value="Adore Somebody!")
            await ctx.send(embed=embed)
        elif str(category).lower() == "troll":
            embed = discord.Embed(timestamp=ctx.message.created_at)
            embed.set_author(name="RikoSan Self-Bot | Prefix: " + str(bot.command_prefix))
            embed.add_field(name="spam", value="Activate Spammer")
            embed.add_field(name="fakeit", value="Fake CCV2 Credit Card Numbers etc etc")
            embed.add_field(name="fakedox(dox)", value="Sends a Dox ;)")
            await ctx.send(embed=embed)
    @riko.command()
    async def sub(self, ctx, sub):
        await ctx.message.delete()
        reddit = praw.Reddit(
            client_id = rclient_id,
            client_secret = rclient_scret,
            user_agent = user_agent
        )
        sub = reddit.subreddit(sub)
        rpost = sub.random()
        await ctx.send(rpost.url)

    @riko.command()
    async def hentai(self, ctx):
        await ctx.message.delete()
        reddit = praw.Reddit(
            client_id = rclient_id,
            client_secret = rclient_scret,
            user_agend = user_agent
        )
        sub = reddit.get_subreddit("hentai")
        new_posts = sub.get_new(limit=100)
        hot_posts = sub.get_hot(limit=100)
        picker = random.randint(0, 2)
        random_post_number = random.randint(0,100)
        if picker == "0":
            submission = sub.random()
        if picker == "1":
            for i,post in enumerate(new_posts):
                if i == random_post_number:
                    ctx.send(random_post_number)
        if picker == "2":
            for i,post in enumerate(hot_posts):
                if i == random_post_number:
                    ctx.message.send(i)
        else:
            ctx.message.send("Ich bin scheiße programmiert!")
    
    @riko.command()
    async def hug(self, ctx, user: discord.User = None):
        if user is None:
            ctx.message.send("Please tag somebody you want to Hug!")
        embed = discord.Embed(description=f"Bannätzchen hugs {user.mention}")
        embed.set_image(url="https://tenor.com/view/crying-cry-dont-be-happy-gif-13401899")
        await ctx.send(embed=embed)
    @riko.command()
    async def kiss(self, ctx, user: discord.User = None):
        if user.mention is None:
            ctx.message.send("Please Tag somebody you want to Kiss!")
        embed = discord.Embed(description=f"**Bannätzchen Kisses {user.mention}**")
        embed.set_image(url="https://api.kawaii.red/gif/kiss/kiss18.gif")
        await ctx.send(embed=embed)
    @riko.command()
    async def cry(self, ctx):
        embed = discord.Embed(description="**Bannätzchen Cries**")
        embed.set_image(url="https://tenor.com/view/anime-umaru-cry-crying-tears-gif-5184314")
        await ctx.send(embed=embed)
    
    @riko.command()
    async def fuck(self, ctx, user: discord.User = None):
        embed = discord.Embed(description=f"**{ctx.author.mention} Fucks {user.mention}**")
        embed.set_image(url="http://besthentaipics.com/plog-content/images/best-hentai-pictures/hentai-gifs/awesome-anal-penetration-anime-porn-animated-photo.gif")
        await ctx.send(embed=embed)

    @riko.command()
    async def slap(self, ctx, user: discord.User = None):
        embed = discord.Embed(description=f"**Bannätzchen Slaps {user.mention}**")
        embed.set_image(url="https://tenor.com/view/slap-bear-slap-me-you-gif-17942299")
        await ctx.send(embed=embed)
    
    @riko.command()
    async def cuddle(self, ctx, user: discord.User = None):
        embed = discord.Embed(description=f"**Bannätzchen cuddled {user.mention}**")
        embed.set_image(url="https://tenor.com/view/horimiya-izumi-miyamura-hori-kyoko-couple-hug-gif-14539121")
        await ctx.send(embed=embed)
    
    @riko.command()
    async def angry(self, ctx, user: discord.User = None):
        embed = discord.Embed(description=f"**Bannätzchen is angry at {user.mention}**")
        embed.set_image(url="")
        await ctx.send(embed=embed)

    @riko.command()
    async def pfp(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        if user == None:
            await ctx.send("please Mention someone!")
            await ctx.message.delete()
        pfp = user.avatar_url
        embed = discord.Embed(description=f"Profile Picture from {user.mention}")
        embed.set_image(url=pfp)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))
