from pyrogram import Client, filters
import os, requests

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client(
    "terabox-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def terabox_direct(url):
    api = "https://api.kaiz-chi.fun/terabox?url=" + url
    r = requests.get(api).json()
    return r.get("HD", None)

@app.on_message(filters.text)
async def link_handler(client, message):
    url = message.text
    if "terabox" not in url:
        return await message.reply("Send a valid TeraBox link.")

    msg = await message.reply("Processing...")

    link = terabox_direct(url)
    if link:
        await msg.edit(f"Direct Download Link:\n{link}")
    else:
        await msg.edit("Failed to fetch direct link.")

app.run()
