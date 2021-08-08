from telegram import InlineQueryResultAudio
from .urlbutton import URLButton
from . import spotify


def get_answers(query: str):
    query_results = spotify.search(q=query, limit=20)
    results = []
    for track in query_results["tracks"]["items"]:
        if track["type"] == "track" and track["preview_url"] is not None:
            results.append(
                InlineQueryResultAudio(
                    id=track["id"],
                    audio_url=track["preview_url"],
                    title=track["name"],
                    performer=track["artists"][0]["name"],
                    reply_markup=URLButton(
                        "Open in Spotify", url=track["external_urls"]["spotify"]
                    )
                )
            )
    return results
