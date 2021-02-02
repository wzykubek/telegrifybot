from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    Dispatcher,
    InlineQueryHandler,
)
from telegram import (
    InlineQueryResultAudio,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
import logging
from settings import TOKEN, CLIENT_ID, CLIENT_SECRET, SOURCE_URL
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)
updater = None


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))


def query(query):
    results = sp.search(q=query, limit=20)
    results_ = []
    for _, track in enumerate(results["tracks"]["items"]):
        results_.append(
            {
                "artist": track["artists"][0]["name"],
                "title": track["name"],
                "preview_url": track["preview_url"],
                "url": track["external_urls"]["spotify"],
                "id": track["id"],
                "type": track["type"],
            }
        )
    return results_


def inline(update, context):
    query_ = str(update.inline_query.query)
    results = query(query_)
    answers = []
    for result in results:
        if result["type"] == "track" and result["preview_url"] is not None:
            answers.append(
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
            print(result)
    context.bot.answer_inline_query(
        update.inline_query.id, answers, cache_time=0, timeout=30
    )


def start(update, context):
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


def main():
    global updater
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(["start", "help"], start))
    dispatcher.add_handler(InlineQueryHandler(inline))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
