from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру главного меню"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🎁 Получить бесплатный гайд')],
            [KeyboardButton(text='💰 Поддержать')],
            [KeyboardButton(text='📦 Магазин')]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_guide_keyboard() -> InlineKeyboardMarkup:
    """Создает инлайн клавиатуру для покупки гайда"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📱 PDF версия • 399₽", callback_data="buy_pdf")],
            [InlineKeyboardButton(text="🎤 Голосовая версия • 499₽", callback_data="buy_voice")],
            [InlineKeyboardButton(text="📦 Пакет «Выживи сам» • 699₽", callback_data="buy_package")],
            [InlineKeyboardButton(text="📝 Бесплатный отрывок", callback_data="free_sample")]
        ]
    )
    return keyboard 