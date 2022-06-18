from discord import Intents
from discord.ext import commands, tasks
from player import player_pos, pacman, players
from gamemap import gamemap
import bot_commands
import bot_events

client = commands.Bot(
    command_prefix="$",
    description="PACMAN discord bot",
    case_insensitive=True,
    intents=Intents.all(),
    owner_ids=[760331432479686666])


@tasks.loop(reconnect=True, seconds=1.75)
async def updater():
    try:
        vals = players.values()
        for player in vals:
            await pacman(player)
            player_pos(player['user'].id)
            await gamemap(player['game'].channel, player['user'])
    except Exception as e:
        pass


@client.event
async def on_ready():
    print(f"We have logged in as {client.user.name} ({client.user.id})")
    if not updater.is_running():
        updater.start()


@client.command()
async def play(ctx):
    """ Starts a new game """
    await bot_commands.play(ctx)


@client.command()
async def stop(ctx):
    """ Stops the current game """
    await bot_commands.stop(ctx)


@client.event
async def on_reaction_add(reaction, user):
    await bot_events.on_reaction_add(reaction, user)

client.run(
    "TOKEN", reconnect=True)
