from discord import Embed
from player import players
from utils import stuff
from enemies import pac_ghost


async def gamemap(ctx, user):
    """ Function to update the game map """

    to_send = 'loading...'
    if user.id not in players:
        embed = Embed(title=":space_invader: __**PACMAN**__ :space_invader:",
                      description=to_send)
        sent = await ctx.send(embed=embed)

        await sent.add_reaction("⬆️")
        await sent.add_reaction("⬇️")
        await sent.add_reaction("⬅️")
        await sent.add_reaction("➡️")

        room = {1: ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', ],
                2: ['b', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'b', ],
                3: ['b', '.', 'b', 'b', 'b', '.', 'b', 'b', 'b', '.', 'b', ],
                4: ['b', '.', 'b', 'g', 'b', '.', 'b', 'g', 'b', '.', 'b', ],
                5: ['b', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'b', ],
                6: ['b', '.', 'b', 'b', 'b', '.', 'b', 'b', 'b', '.', 'b', ],
                7: ['b', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'b', ],
                8: ['b', '.', 'b', '.', 'b', '.', 'b', '.', 'b', '.', 'b', ],
                9: ['b', '.', 'b', '.', 'b', '.', 'b', '.', 'b', '.', 'b', ],
                10: ['b', '.', 'b', '.', 'b', '.', 'b', '.', 'b', '.', 'b', ],
                11: ['b', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'b', ],
                12: ['b', '.', 'b', 'b', 'b', '.', 'b', 'b', 'b', '.', 'b', ],
                13: ['b', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'b', ],
                14: ['b', '.', 'b', 'g', 'b', '.', 'b', 'g', 'b', '.', 'b', ],
                15: ['b', '.', 'b', 'b', 'b', '.', 'b', 'b', 'b', '.', 'b', ],
                16: ['b', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'b', ],
                17: ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', ],
                }

        player = {
            'game': sent,
            'room': room,
            'dir': '',
            'score': 0,
            'playerPos': [],
            'enemy_poses': [],
            'dots': -1,
            'user': user
        }

        for i in player['room']:
            for ii in range(11):
                if player['room'][i][ii] == 'b':
                    player['room'][i].pop(ii)
                    player['room'][i].insert(ii, stuff['wall'])
                elif player['room'][i][ii] == 'g':
                    player['room'][i].pop(ii)
                    player['room'][i].insert(ii, stuff['ghost'])
                    player['enemy_poses'].append([(i, ii), stuff['dot']])
                else:
                    player['room'][i].pop(ii)
                    player['room'][i].insert(ii, stuff['dot'])
                    player['dots'] += 1

        player['room'][9].pop(5)
        player['room'][9].insert(5, stuff['pacman'])
        players[user.id] = player

    to_send = f"""
Use the arrows below to move around
Player: **{players[user.id]['user'].name}**
Score: **{players[user.id]['score']}**
Pellets left: **{players[user.id]['dots']}** """

    for enemy in players[user.id]['enemy_poses']:
        await pac_ghost(enemy, user.id)
    if players[user.id]['dir'] != '':
        to_send += f"\nGoing **{players[user.id]['dir']}**"

    for i in range(1, len(players[user.id]['room'])+1):
        to_send += '\n' + "".join(players[user.id]['room'][i])

    embed = Embed(title=":space_invader: __**PACMAN**__ :space_invader:",
                  description=to_send)
    message = players[user.id]['game']
    await message.edit(embed=embed)
