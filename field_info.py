
GAME_FIELDS_ALL=[
    'age_ratings',
    'aggregated_rating',
    'aggregarted_rating_count',
    'alternative_names',
    'artworks',
    'bundles',
    'category',
    'collection',
    'cover',
    'created_at',
    'dlcs',
    'expansions',
    'external_games',
    'first_release_data',
    'follows',
    'franchise',
    'franchises',
    'game_engines',
    'game_modes',
    'genres',
    'hypes',
    'involved_companies',
    'keywords',
    'multiplayer_modes',
    'name',
    'parent_game',
    'platforms',
    'player_perspectives', 
    'popularity',
    'pulse_count',
    'rating',
    'rating_count',
    'release_dates',
    'screenshots',
    'similar_games',
    'status',
    'storyline',
    'summary',
    'tags',
    'themes',
    'time_to_beat',
    'total_rating',
    'total_rating_count',
    'updated_at',
    'url',
    'version_parent',
    'version_title',
    'videos',
    'websites'

]

GAME_CATEGORY_MAP={
    0 : 'main_game',
    1 : 'dlc_addon',
    2 : 'expansion', 
    3 : 'bundle' , 
    4 : 'standalone_expansion' , 
    5 : 'mod' , 
    6 : 'episode'
}

GAME_STATUS_MAP={
    0 : 'released' , 
    2 : 'alpha' , 
    3 : 'beta' , 
    4 : 'early_access',  
    5 : 'offline' , 
    6 : 'cancelled' , 
    7 : 'rumored'
}


GENRES_FIELDS_ALL=[
    'created_at',
    'name',
    'slug',
    'updated_at',
    'url'
]

DEFAULT_GAME_FIELDS=[
    "name",
    "summary",
    "rating",
    "cover.url",   
    "platforms",
    "screenshots"
]