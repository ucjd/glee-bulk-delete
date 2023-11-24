import ctypes
import discord
from discord.ext import commands
from os import system
import colorama
from colorama import Fore

def clear_screen():
    # Implementation of clear_screen function
    pass

def fade_pinkred(text):
    colorama.init()  # Initialize Colorama for cross-platform color support
    pinkred_text = f"{Fore.MAGENTA}{text}{Fore.RESET}"
    return pinkred_text

def startup():
    # Implementation of startup function
    pass

try:
    clear_screen()
    ctypes.windll.kernel32.SetConsoleTitleW('glee | bulk delete')
    system('mode con: cols=95 lines=25')

    raw_dashboard_bulk_delete = '''
╔════════════════════════════════════════════════════════════════════════════════════════╗
║ ██████╗ ██╗   ██╗██╗     ██╗  ██╗    ██████╗ ███████╗██╗     ███████╗████████╗███████╗ ║    
║ ██╔══██╗██║   ██║██║     ██║ ██╔╝    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝ ║   
║ ██████╔╝██║   ██║██║     █████╔╝     ██║  ██║█████╗  ██║     █████╗     ██║   █████╗   ║   
║ ██╔══██╗██║   ██║██║     ██╔═██╗     ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝   ║   
║ ██████╔╝╚██████╔╝███████╗██║  ██╗    ██████╔╝███████╗███████╗███████╗   ██║   ███████╗ ║   
║ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝ ║
╚════════════════════════════════════════════════════════════════════════════════════════╝'''
    dashboard_bulk_delete = fade_pinkred(raw_dashboard_bulk_delete)
    print(dashboard_bulk_delete)

    token = "yourtokenhere"

    lithium = commands.Bot(command_prefix='g', self_bot=True, help_command=None) # Prefix
    
    @lithium.event
    async def on_ready():
        print("Type glee in the channel you want to delete messages in") # Edit if u change the word that deletes

    @lithium.command()
    async def lee(channel): # edit for word to say to delete
        async for msg in channel.message.channel.history(limit=int(9999999)): # Change how much messages u delete
            if msg.author.id == lithium.user.id:
                try:  
                    await msg.delete()
                    print("Deleted")
                except:
                    continue

    lithium.run(token)

except KeyboardInterrupt:
    startup()
