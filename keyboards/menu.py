from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎒 Снаряжение", callback_data="gear")],
        [InlineKeyboardButton(text="📱 Приложения (платно)", callback_data="apps")],
    ])
