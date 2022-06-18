stuff = {
    'empty': ':black_large_square:',
    'wall': ':blue_square:',
    'ghost': ':ghost:',
    'pacman': ':yum:',
    'dot': ':white_small_square:',
    'ded': ':dizzy_face:'
}


async def left(dictionary, inst_replace, inst_player, pos):
    """ Function to move object left """

    (dictionary[pos[0]]).pop(pos[1])
    (dictionary[pos[0]]).insert(pos[1], inst_replace)
    (dictionary[pos[0]]).pop(pos[1]-1)
    (dictionary[pos[0]]).insert(pos[1]-1, inst_player)


async def right(dictionary, inst_replace, inst_player, pos):
    """ Function to move object right """

    (dictionary[pos[0]]).pop(pos[1])
    (dictionary[pos[0]]).insert(pos[1], inst_replace)
    (dictionary[pos[0]]).pop(pos[1]+1)
    (dictionary[pos[0]]).insert(pos[1]+1, inst_player)


async def up(dictionary, inst_replace, inst_player, pos):
    """ Function to move object up """

    (dictionary[pos[0]]).pop(pos[1])
    (dictionary[pos[0]]).insert(pos[1], inst_replace)
    (dictionary[pos[0]-1]).pop(pos[1])
    (dictionary[pos[0]-1]).insert(pos[1], inst_player)


async def down(dictionary, inst_replace, inst_player, pos):
    """ Function to move object down """

    (dictionary[pos[0]]).pop(pos[1])
    (dictionary[pos[0]]).insert(pos[1], inst_replace)
    (dictionary[pos[0]+1]).pop(pos[1])
    (dictionary[pos[0]+1]).insert(pos[1], inst_player)
