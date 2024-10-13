import ctypes
import discord
from discord.ext import commands
from os import system

def clear_screen():
    pass

def startup():
    pass

async def delete_message(msg):
    try:
        await msg.delete()
        print("Deleted")
    except discord.errors.NotFound:
        print("Message not found.")
    except discord.errors.Forbidden:
        print("Unable to delete message (Forbidden).")
    except Exception as e:
        print(f"An error occurred: {e}")

try:
    clear_screen()
    ctypes.windll.kernel32.SetConsoleTitleW('channel | bulk delete')
    system('mode con: cols=95 lines=25')

    token = "yourtokenhere"

    lithium = commands.Bot(command_prefix='g', self_bot=True, help_command=None)

    @lithium.event
    async def on_ready():
        try:
            while True:
                channel_id = input("Enter the channel ID to delete messages from: ")

                try:
                    channel = lithium.get_channel(int(channel_id))
                    if channel:
                        async for msg in channel.history(limit=int(9999999)):
                            if msg.author.id == lithium.user.id:
                                await delete_message(msg)
                    else:
                        print(f"Channel with ID {channel_id} not found.")
                except ValueError:
                    print("Invalid channel ID. Please enter a valid integer.")

        except KeyboardInterrupt:
            print("\nInterrupted. Press enter to enter another channel ID.")
            input()

    @lithium.event
    async def on_message(message):
        await lithium.process_commands(message)

    lithium.run(token)

    input("Press Enter to exit...")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    startup()
