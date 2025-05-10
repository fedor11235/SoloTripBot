from aiogram import types
from keyboards.menu import main_menu
from keyboards.main import get_main_keyboard
from handlers.commands import (
    free_guide_command,
    support_command,
    shop_command
)
from utils.logger import setup_logger

logger = setup_logger(__name__)

async def handle_text(message: types.Message):
    """Обработчик текстовых сообщений"""
    try:
        if message.text == '🎁 Получить бесплатный гайд':
            await free_guide_command(message)
        elif message.text == '💰 Поддержать':
            await support_command(message)
        elif message.text == '📦 Магазин':
            await shop_command(message)
        else:
            await message.answer("Выберите раздел из меню ниже:", reply_markup=main_menu())
        
        logger.info(f"User {message.from_user.id} sent message: {message.text}")
    except Exception as e:
        logger.error(f"Error in handle_text: {e}")
        await message.answer("Произошла ошибка. Пожалуйста, попробуйте позже.") 