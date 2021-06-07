from discord.ext import commands
bot = commands.Bot(command_prefix='!')

toDo = []

@bot.command(name="add", help="add an item to the list")
async def add(ctx, *, item: str):
    toDo.append(item)
    await ctx.send(item + " has been added to your to-do list")

@bot.command(name="remove", help="remove an item from the list")
async def remove(ctx, *, item: str):
    if (item in toDo):
        toDo.remove(item)
        await ctx.send(item + " has been removed from your to-do list")
    else:
        await ctx.send("That is not on the list")
    
@bot.command(name="remove#", help="remove an item from the list by the number")
async def remove(ctx, num: int):
    if (len(toDo) < num):
        newNumber = str(num)
        await ctx.send("There is not an item " + newNumber + " on the list")
    else:
        toDo.pop(num - 1)
        newNum = str(num)
        await ctx.send("Item " + newNum + " has been removed from your to-do list")

@bot.command(name="list", help="display the list")
async def list(ctx):
    await ctx.send("To-do list:")
    for i in toDo:
        num = toDo.index(i) + 1
        newNum = str(num)
        await ctx.send(newNum + ". " + i)


with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)

