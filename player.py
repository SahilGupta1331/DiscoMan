from utils import left, right, up, down, stuff
from discord import Embed

players = {}


async def pacman(player):
    ded = False
    if player['dir'] == "left":
        if player['room'][player['playerPos'][0]][player['playerPos'][1]-1] != stuff['wall']:
            if player['room'][player['playerPos'][0]][player['playerPos'][1]-1] == stuff['dot']:
                player['score'] += 10
                player['dots'] -= 1
            elif player['room'][player['playerPos'][0]][player['playerPos'][1]-1] == stuff['ghost']:
                ded = True
            await left(player['room'], stuff['empty'], stuff['pacman'], player['playerPos'])
    elif player['dir'] == "right":
        if player['room'][player['playerPos'][0]][player['playerPos'][1]+1] != stuff['wall']:
            if player['room'][player['playerPos'][0]][player['playerPos'][1]+1] == stuff['dot']:
                player['score'] += 10
                player['dots'] -= 1
            elif player['room'][player['playerPos'][0]][player['playerPos'][1]+1] == stuff['ghost']:
                ded = True
            await right(player['room'], stuff['empty'], stuff['pacman'], player['playerPos'])
    elif player['dir'] == "down":
        if player['room'][player['playerPos'][0]+1][player['playerPos'][1]] != stuff['wall']:
            if player['room'][player['playerPos'][0]+1][player['playerPos'][1]] == stuff['dot']:
                player['score'] += 10
                player['dots'] -= 1
            elif player['room'][player['playerPos'][0]+1][player['playerPos'][1]] == stuff['ghost']:
                ded = True
            await down(player['room'], stuff['empty'], stuff['pacman'], player['playerPos'])
    elif player['dir'] == "up":
        if player['room'][player['playerPos'][0]-1][player['playerPos'][1]] != stuff['wall']:
            if player['room'][player['playerPos'][0]-1][player['playerPos'][1]] == stuff['dot']:
                player['score'] += 10
                player['dots'] -= 1
            elif player['room'][player['playerPos'][0]-1][player['playerPos'][1]] == stuff['ghost']:
                ded = True
            await up(player['room'], stuff['empty'], stuff['pacman'], player['playerPos'])
    if ded:
        return await game_over(player)
    if player['dots'] == 0:
        embed = Embed(title=":cookie: __**You Won!!!**__ :cookie:",
                      description=f"Your score: {player['score']:,}")
        embed.set_footer(
            text=f"Use $play to play again.")

        # Edits the "Now playing" message to the "Game over" message
        message = player['game']
        await message.edit(content=None, embed=embed)
        players.pop(player['user'].id)
        return


def player_pos(user):
    """ Function to update player position """

    for i in range(1, len(players[user]['room'])+1):
        if stuff['pacman'] in players[user]['room'][i] or stuff['pacman'] in players[user]['room'][i]:
            x_axis = i
            y_axis = players[user]['room'][i].index(stuff['pacman'])
            del players[user]['playerPos'][:]
            players[user]['playerPos'].append(x_axis)
            players[user]['playerPos'].append(y_axis)


async def game_over(player):
    to_send = f"Your score: {player['score']:,}"
    player['room'][player['playerPos'][0]].pop(player['playerPos'][1])
    player['room'][player['playerPos'][0]].insert(
        player['playerPos'][1], stuff['ded'])
    for i in player['room']:
        to_send += f"\n{''.join(player['room'][i])}"
    embed = Embed(title=":ghost: __**GAME OVER**__ :ghost:",
                  description=to_send)
    embed.set_footer(
        text=f"Better luck next time! Use $play to play again.")

    # Edits the "Now playing" message to the "Game over" message
    message = player['game']
    players.pop(player['user'].id)
    return await message.edit(content=None, embed=embed)
