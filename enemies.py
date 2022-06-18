from player import players, game_over
from utils import stuff, up, down, left, right
from random import choice


async def pac_ghost(enemy, user):
    e = enemy[0]
    next_dirs = []
    next_pos = ''
    if players[user]['room'][e[0]][e[1]+1] not in [stuff['wall'], stuff['ghost']]:
        next_dirs.append('right')
    if players[user]['room'][e[0]][e[1]-1] not in [stuff['wall'], stuff['ghost']]:
        next_dirs.append('left')
    if players[user]['room'][e[0]+1][e[1]] not in [stuff['wall'], stuff['ghost']]:
        next_dirs.append('down')
    if players[user]['room'][e[0]-1][e[1]] not in [stuff['wall'], stuff['ghost']]:
        next_dirs.append('up')
    move = choice(next_dirs)
    if move == 'right':
        next_pos += players[user]['room'][e[0]][e[1]+1]
        enemy[1] = players[user]['room'][e[0]][e[1]+1]
        enemy[0] = (e[0], e[1]+1)
        await right(players[user]['room'], enemy[1], stuff['ghost'], e)
    elif move == 'left':
        next_pos += players[user]['room'][e[0]][e[1]-1]
        enemy[1] = players[user]['room'][e[0]][e[1]-1]
        enemy[0] = (e[0], e[1]-1)
        await left(players[user]['room'], enemy[1], stuff['ghost'], e)
    elif move == 'up':
        next_pos += players[user]['room'][e[0]-1][e[1]]
        enemy[1] = players[user]['room'][e[0]-1][e[1]]
        enemy[0] = (e[0]-1, e[1])
        await up(players[user]['room'], enemy[1], stuff['ghost'], e)
    elif move == 'down':
        next_pos += players[user]['room'][e[0]+1][e[1]]
        enemy[1] = players[user]['room'][e[0]+1][e[1]]
        enemy[0] = (e[0]+1, e[1])
        await down(players[user]['room'], enemy[1], stuff['ghost'], e)
    if next_pos == stuff['pacman']:
        return await game_over(players[user])
