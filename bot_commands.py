from player import players
from gamemap import gamemap
from discord import Embed


async def play(ctx):
    if ctx.author.id in players:
        message = players[ctx.author.id]['game']
        return await message.reply(f"<@{ctx.message.author.id}>, you are already playing!\nHere is the running game! Use **$stop** to stop playing.", mention_author=True)

    return await gamemap(ctx, ctx.author)


async def stop(ctx):
    if ctx.author.id not in players:
        return await ctx.reply(f"You are not playing! Use **$play** to start playing.", mention_author=True)

    embed = Embed(title=":space_invader: __**PACMAN**__ :space_invader:",
                  description=f"Game stopped!\nYour Score: {players[ctx.author.id]['score']}")
    sent = players[ctx.author.id]['game']
    players.pop(ctx.author.id)
    return await sent.edit(embed=embed)
