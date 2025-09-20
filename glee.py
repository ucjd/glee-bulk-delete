import asyncio, discord, os
from os import system


def clear_screen():
    system("cls" if os.name == "nt" else "clear")


delete_sequence = [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    2.2,
    1.7,
    0.0,
    2.2,
    0.0,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    0.0,
    2.2,
    1.5,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    0.0,
    2.2,
    1.7,
    2.2,
    1.5,
    2.2,
    3.2,
    2.2,
    1.0,
    2.2,
    1.7,
    2.2,
    3.2,
    2.2,
    1.0,
    2.2,
    1.7,
    0.0,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    0.0,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    3.2,
    2.2,
    1.7,
    2.2,
    0.0,
    2.2,
    1.7,
    2.2,
    3.2,
    1.7,
    2.2,
    3.2,
    2.2,
    1.7,
    0.0,
    2.2,
    1.7,
    2.2,
    1.7,
    2.2,
    1.0,
    2.2,
    1.7,
    2.2,
    0.0,
    2.2,
    1.7,
    2.2,
    3.2,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    0.0,
    2.2,
    1.7,
    2.2,
    1.5,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    3.2,
    1.7,
    2.2,
    1.0,
    2.2,
    1.7,
    2.2,
    3.2,
    2.2,
    1.0,
    2.2,
    1.7,
    2.2,
    0.0,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    0.0,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    1.5,
    2.2,
    3.2,
    2.2,
    1.7,
    0.0,
    2.2,
    1.7,
    2.2,
    1.0,
    2.2,
    1.0,
    2.2,
    3.2,
    2.2,
    1.7,
    2.2,
    0.0,
    2.2,
    1.7,
    2.2,
    1.5,
    2.2,
    3.2,
    1.7,
    2.2,
    9.9,
]


async def delete_message(msg, delay):
    try:
        await msg.delete()
        print("Deleted message ID:", msg.id)
        await asyncio.sleep(delay)
    except discord.NotFound:
        print("Message not found.")
    except discord.Forbidden:
        print("Unable to delete message (Forbidden).")
    except Exception as e:
        print(f"An error occurred: {e}")


client = discord.Client()


@client.event
async def on_ready():
    clear_screen()
    system("mode con: cols=95 lines=25")
    while True:
        channel_id = input("Enter the channel ID to delete messages from: ")
        try:
            channel = client.get_channel(int(channel_id))
            if channel:
                index = 0
                async for msg in channel.history(limit=9999999):
                    if msg.author.id == client.user.id:
                        await delete_message(msg, delete_sequence[index])
                        index = (index + 1) % len(delete_sequence)
            else:
                print(f"Channel with ID {channel_id} not found.")
        except ValueError:
            print("Invalid channel ID. Please enter a valid integer.")


try:
    token = "put your token here"
    client.run(token)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    startup()
