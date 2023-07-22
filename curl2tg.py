import os

import requests
import asyncio
import telegram

url = os.environ.get("CURL2TG_URL")
tg_token = os.environ.get("CURL2TG_TOKEN")
tg_chats = os.environ.get("CURL2TG_CHATS")


async def main():
    if url is None:
        raise Exception("CURL2TG_URL not set")

    if tg_token is None:
        raise Exception("CURL2TG_TOKEN not set")
    bot = telegram.Bot(tg_token)

    if tg_chats is None:
        async with bot:
            print(await bot.get_updates())
        raise Exception("CURL2TG_CHATS not set")

    res = requests.get(url, headers={"Accept": "text/plain"})
    res.raise_for_status()

    async with bot:
        for chat in tg_chats.split(","):
            print(await bot.send_message(chat_id=chat, text=res.text))


if __name__ == "__main__":
    asyncio.run(main())
