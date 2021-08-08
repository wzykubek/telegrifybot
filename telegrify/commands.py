from telegrask import InlineQuery
from telegram.ext import CallbackContext
from telegram import (
    Update,
    InlineQueryResultAudio,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from .config import SOURCE_URL
from .functions import spotify_query
from . import bot


@bot.inline_query
def inline(query: InlineQuery):
    query_str = query.query_str
    results = spotify_query(query_str)
    for result in results:
        if result["type"] == "track" and result["preview_url"] is not None:
            query.add_answer(
                InlineQueryResultAudio(
                    id=result["id"],
                    audio_url=result["preview_url"],
                    title=result["title"],
                    performer=result["artist"],
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Open in Spotify", url=result["url"])]]
                    ),
                )
            )
    query.send_answers()


@bot.custom_help_command
def help(update: Update, context: CallbackContext, desc: dict):
    update.message.reply_text(
        """
To use this bot start typing
@telegrifybot <name of song/artist>
and select your song to send it's preview to current chat.
                              """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Source Code", url=SOURCE_URL)]]
        ),
    )
