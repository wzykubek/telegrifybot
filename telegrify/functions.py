from . import spotify


def spotify_query(query: str):
    query_results = spotify.search(q=query, limit=20)
    results = []
    for track in query_results["tracks"]["items"]:
        results.append(
            {
                "artist": track["artists"][0]["name"],
                "title": track["name"],
                "preview_url": track["preview_url"],
                "url": track["external_urls"]["spotify"],
                "id": track["id"],
                "type": track["type"],
            }
        )
    return results
