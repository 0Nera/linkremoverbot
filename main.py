from aiogram import Bot, Dispatcher, Router, types

import asyncio
import re


# https://t.me/BotFahter
TOKEN = ""

router = Router()

@router.channel_post()
async def channel_post_handler(channel_post: types.Message):
    await channel_post.edit_text(
            re.sub(
                r'<(a|/a).*?>', 
                "", 
                channel_post.html_text
            )
        )


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)

    bot = Bot(TOKEN, parse_mode="HTML")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())