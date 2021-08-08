from telegram import InlineKeyboardMarkup, InlineKeyboardButton


class URLButton(InlineKeyboardMarkup):
    def __init__(self, text: str, url: str):
        super().__init__([[InlineKeyboardButton(text, url=url)]])
