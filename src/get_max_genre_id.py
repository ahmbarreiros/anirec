def get_max_genre_id(anime_list_data):
    max_genre_id = 0
    for anime in anime_list_data:
        try:
            for genre in anime["genres"]:
                max_genre_id = max(genre["id"], max_genre_id)
        except:
            pass
    max_genre_id += 1
    return max_genre_id