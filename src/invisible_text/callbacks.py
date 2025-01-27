from aiogram.filters.callback_data import CallbackData

class InvisibleTextCallback(CallbackData, prefix="invisible_text"):
    action: str