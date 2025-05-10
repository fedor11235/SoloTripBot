from aiogram import types
from keyboards.main import get_guide_keyboard
from utils.logger import setup_logger

logger = setup_logger(__name__)

async def handle_guide_callback(callback_query: types.CallbackQuery):
    """Обработчик callback-запросов для покупки гайда"""
    try:
        if callback_query.data == "buy_pdf":
            text = (
                "📱 *PDF версия гайда*\n\n"
                "🎯 *Что включено:*\n"
                "• Полный текст гайда\n"
                "• Иллюстрации и схемы\n"
                "• Доступ навсегда\n\n"
                "💰 *Цена: 399₽*\n\n"
                "📝 *Для покупки напишите мне в личные сообщения*"
            )
        elif callback_query.data == "buy_voice":
            text = (
                "🎤 *Голосовая версия гайда*\n\n"
                "🎯 *Что включено:*\n"
                "• Аудиозапись гайда\n"
                "• Дополнительные комментарии\n"
                "• Доступ навсегда\n\n"
                "💰 *Цена: 499₽*\n\n"
                "📝 *Для покупки напишите мне в личные сообщения*"
            )
        elif callback_query.data == "buy_package":
            text = (
                "📦 *Пакет «Выживи сам»*\n\n"
                "🎯 *Что включено:*\n"
                "• PDF версия гайда\n"
                "• Голосовая версия\n"
                "• Дополнительные материалы\n"
                "• Доступ навсегда\n\n"
                "💰 *Цена: 699₽*\n\n"
                "📝 *Для покупки напишите мне в личные сообщения*"
            )
        elif callback_query.data == "free_sample":
            text = (
                "📖 *Бесплатный отрывок гайда*\n\n"
                "🎯 *Что включено:*\n"
                "• Первая глава\n"
                "• Базовые советы\n"
                "• Примеры из практики\n\n"
                "💫 *Хотите получить полную версию?*\n"
                "Выберите формат выше 👆"
            )
        else:
            logger.warning(f"Unknown callback data: {callback_query.data}")
            await callback_query.answer("Произошла ошибка. Попробуйте позже.")
            return

        await callback_query.message.edit_text(text, parse_mode="Markdown")
        await callback_query.answer()
        logger.info(f"User {callback_query.from_user.id} selected guide option: {callback_query.data}")
    except Exception as e:
        logger.error(f"Error in handle_guide_callback: {e}")
        await callback_query.answer("Произошла ошибка. Попробуйте позже.") 