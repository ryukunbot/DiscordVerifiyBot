import discord
from discord.ext import commands
import json

with open('config.json') as f:
	config = json.load(f)

intents = discord.Intents.default()  
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix=config['prefix'],intents=intents)

@bot.event
async def on_ready():
	print(f"正常に起動しました\nBot:{bot.user}")

@bot.command()
async def verifiy(ctx,role:discord.Role=None,messages:discord.Message=None):
	if ctx.author.guild_permissions.administrator:
		if role == None:
			await ctx.send("ロールを指定してください")
			return
		if messages == None:
			embed=discord.Embed(title=config['verifiy_title'],description=config['verifiy_description'])
			messages = await ctx.send(embed=embed)	
		else:
			messages = messages
		await messages.add_reaction(config['verifiy_emoji'])
		with open('verifiy.json','r') as f:
			verifiys = json.load(f)
			verifiys['verifiy_role'] = str(role.id)
			verifiys['verifiy_id'] = str(messages.id)
		with open('verifiy.json','w') as f:
			json.dump(verifiys,f,indent=4)
	else:
		await ctx.send("このコマンドを実行するためには管理者権限が必要です")		

@bot.event
async def on_raw_reaction_add(payload:discord.RawReactionActionEvent):
  with open('verifiy.json','r') as f:
    verifiys = json.load(f)
  if not payload.member == bot.user:
    if payload.message_id == int(verifiys['verifiy_id']):
      if payload.emoji.name == config['verifiy_emoji']:
        guild = bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        role = guild.get_role(int(verifiys['verifiy_role']))
        await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload:discord.RawReactionActionEvent):
  with open('verifiy.json','r') as f:
    verifiys = json.load(f)
  if not payload.member == bot.user:
    if payload.message_id == int(verifiys['verifiy_id']):
      if payload.emoji.name == config['verifiy_emoji']:
        guild = bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        role = guild.get_role(int(verifiys['verifiy_role']))
        await member.remove_roles(role)	

bot.run(config['token'])			