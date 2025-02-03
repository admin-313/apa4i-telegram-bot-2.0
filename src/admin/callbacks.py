from aiogram.filters.callback_data import CallbackData

class AdminCallback(CallbackData, prefix="admin"):
    action: str
    target_page: int