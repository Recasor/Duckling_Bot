import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode

from config_data.config import Config, load_config
from aiogram.filters import Command
from aiogram.types import Message


async def main() -> None:
    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    async def process_start_command(message: Message) -> None:
        await message.answer(text='Хаюшки, я работаю!')

    dp.message.register(process_start_command, Command(commands=["start"]))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
