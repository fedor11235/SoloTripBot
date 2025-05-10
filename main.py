import asyncio
import logging
from notion_client import Client
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from handlers.commands import (
    start_command,
    help_command,
    gear_command,
    tips_command,
    channel_command,
    guide_command,
    premium_command
)
from handlers.messages import handle_text
from handlers.callbacks import handle_guide_callback
from utils.logger import setup_logger

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Настройка логирования
logger = setup_logger(__name__)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Регистрация хендлеров
async def register_handlers():
    try:
        # Команды
        dp.message.register(start_command, CommandStart())
        dp.message.register(help_command, Command(commands=["help"]))
        dp.message.register(gear_command, Command(commands=["gear"]))
        dp.message.register(tips_command, Command(commands=["tips"]))
        dp.message.register(channel_command, Command(commands=["channel"]))
        dp.message.register(guide_command, Command(commands=["guide"]))
        dp.message.register(premium_command, Command(commands=["premium"]))
        
        # Обработка текстовых сообщений
        dp.message.register(handle_text)
        
        # Обработка callback-запросов
        dp.callback_query.register(handle_guide_callback)
        
        logger.info("Handlers registered successfully")
    except Exception as e:
        logger.error(f"Error registering handlers: {e}")
        raise

async def main():
    try:
        # Регистрация хендлеров
        await register_handlers()
        
        # Запуск бота
        logger.info("Starting bot...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error in main: {e}")
    finally:
        # Закрытие сессии бота
        await bot.session.close()

if __name__ == "__main__":
    try:
        # Добавляем задержку перед запуском
        asyncio.sleep(1)
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}") 