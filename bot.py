import discord
import random
import argparse


class Game:
    def __init__(self, title, description):
        self.title = title
        self.description = description

games = [
    Game(
        "Vape Nation",
        "You must throw a smoke grenade towards an enemy before engaging."
    ),
    Game(
        "Respect the Dead",
        "No looting bodies."
    ),
    Game(
        "Fuckboy",
        "You can only loot fuckboy shacks."
    ),
    Game(
        "Minimalism",
        "You can not use a backpack."
    ),
    Game(
        "Bird Watcher",
        "You must go to every airdrop you see falling."
    ),
    Game(
        "Viking Funeral",
        "Throw a Molotov on an enemy after killing them."
    ),
    Game(
        "Grounded",
        "You can only loot the bottom floor of any structure."
    ),
    Game(
        "Roadrage",
        "Only vehicle kills. No guns or grenades."
    ),
    Game(
        "Call of Duty Master",
        "No-scoping only."
    ),
    Game(
        "Hitman",
        "Silenced pistol only with any other attachments. No armor or helmet."
    ),
    Game(
        "This Is My Rifle",
        "The first gun you find is the only weapon you can use for the entire game."
    ),
    Game(
        "Origin",
        "Go to the center of the circle as fast as you can every time the circle shrinks."
    )
]

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("Invite: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot".format(client.user.id))
    print("------")


@client.event
async def on_message(message):
    if message.content.startswith("!pubg") or message.content.startswith("!strat"):
        game = random.choice(games)
        embed = discord.Embed(title=game.title, description=game.description, color=0xff4500)
        await client.send_message(message.channel, embed=embed)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("token", help="discord bot token")
    args = parser.parse_args()
    client.run(args.token)

if __name__ == "__main__":
    main()
