import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Romeo"])

async def join(client):
    try:
        await client.join_chat("Classics0012")
    except BaseException:
        pass
