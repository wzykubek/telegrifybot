from telegrask import InlineQuery
from telegram.ext import CallbackContext
from telegram import Update
from .config import SOURCE_URL
from .functions import get_answers
from .urlbutton import URLButton
from . import bot


@bot.inline_query
def inline(query: InlineQuery):
    query_str = query.query_str
    query.answers = get_answers(query_str)
    query.send_answers()


@bot.custom_help_command
def help(update: Update, context: CallbackContext, desc: dict):
    update.message.reply_text(
        """
To use this bot start typing
@telegrifybot <name of song/artist>
and select your song to send it's preview to current chat.
                              """,
        reply_markup=URLButton("Source Code", url=SOURCE_URL),
    )
