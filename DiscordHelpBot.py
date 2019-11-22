# Work with Python 3.6
import discord,os
PATH = str(os.getcwd())
TOKEN = 'XXXXXXXXXX'

client = discord.Client()
def get_settings():
  file = open(PATH + "/bot/bot_settings.properties").readlines()
  for line in file:
    if line.endswith("welcome_msg"):
      welcome_msg = line
    elif line.endswith("role"):
      bot_role = line
    elif line.endswith("admin_role")
      admin_role = line
    elif line.endswith("new_user_role"):
      new_role = line
    #end check
 #end func


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    #Commands
    

@client.event
async def on_ready():
    #Get the settings
    get_settings()
    #Now continue execution
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
