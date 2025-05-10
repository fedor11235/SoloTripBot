from aiogram import Router, types
from services.notion import get_item_by_command
from filters.is_premium import IsPremiumUser  # если есть проверка оплаты

router = Router()

@router.message(commands=["gear", "intro", "apps", "route_th"])
async def send_notion_content(message: types.Message):
    cmd = message.text.lstrip("/")
    item = get_item_by_command(cmd)

    if item:
        if item["access"] == "платно" and not await IsPremiumUser().check(message):
            await message.answer("🔒 Это платный контент. Купи доступ, чтобы читать дальше.")
        else:
            await message.answer(item["content"])
    else:
        await message.answer("Контент не найден.")
