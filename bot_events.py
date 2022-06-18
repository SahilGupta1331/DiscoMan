from player import players


async def on_reaction_add(reaction, user):

    if user.bot:
        return

    emoji = reaction.emoji
    await reaction.remove(user)

    if user.id not in players:
        return

    if reaction.message != players[user.id]['game']:
        return

    if emoji == "⬅️":
        players[user.id]['dir'] = "left"
    if emoji == "➡️":
        players[user.id]['dir'] = "right"
    if emoji == "⬇️":
        players[user.id]['dir'] = "down"
    if emoji == "⬆️":
        players[user.id]['dir'] = "up"
