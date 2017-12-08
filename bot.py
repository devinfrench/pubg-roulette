import discord
import random
import argparse
import json

strats = json.load(open('strats.json'))
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
        strat = random.choice(strats)
        embed = discord.Embed(title=strat["title"], description=strat["description"], color=0xff4500)
        await client.send_message(message.channel, embed=embed)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("token", help="discord bot token")
    args = parser.parse_args()
    client.run(args.token)

if __name__ == "__main__":
    main()
