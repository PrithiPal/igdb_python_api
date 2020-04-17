import requests 
import os 
import sys 



class IGBRequest : 
    

    def getAllGames(self) : 
        url = os.path.join(self.BASE_URL,"games")
        resp = requests.get(url,headers=self.BASE_PARAM,params={"fields":'*'})
        return resp.json()

    def getGameById(self,id) : 
        url = os.path.join(self.BASE_URL,"games")
        resp = requests.get(url,headers=self.BASE_PARAM,params={'id':id,'fields':['*']})
        return resp.json()       

    def getGameByName(self,name,**kwargs) : 
        url = os.path.join(self.BASE_URL,"games")
        
        PARAMS={'search':name}
        if 'fields' in kwargs : 
            FIELDS=",".join(kwargs['fields'])
            PARAMS = {**PARAMS,**{'fields':FIELDS}}
        
        print(PARAMS)
        resp = requests.get(url,headers=self.BASE_PARAM,params=PARAMS)
        return resp.json()



    def getGenres(self,**kwargs) : 
        url = os.path.join(self.BASE_URL,"genres")

        PARAMS={}
        if 'fields' in kwargs : 
            PARAMS['fields'] = kwargs['fields']

        print(PARAMS)
        resp = requests.get(url,headers=self.BASE_PARAM,params=PARAMS)
        return resp.json()

    def __init__(self) : 
        self.BASE_URL="https://api-v3.igdb.com/"
        self.SECRET_TOKEN=os.getenv("IGDB_TOKEN")
        self.BASE_PARAM = {'user-key':self.SECRET_TOKEN,
                           'Accept' : 'application/json'
                          }

        self.GAME_FIELDS_ALL=[
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


        self.GAME_CATEGORY_MAP={
            0 : 'main_game',
            1 : 'dlc_addon',
            2 : 'expansion', 
            3 : 'bundle' , 
            4 : 'standalone_expansion' , 
            5 : 'mod' , 
            6 : 'episode'
        }

        self.GAME_STATUS_MAP={
            0 : 'released' , 
            2 : 'alpha' , 
            3 : 'beta' , 
            4 : 'early_access',  
            5 : 'offline' , 
            6 : 'cancelled' , 
            7 : 'rumored'
        }


        self.GENRES_FIELDS=[
            'created_at',
            'name',
            'slug',
            'updated_at',
            'url'
        ]

    def __str__(self) : 
        return "IGDB API FETCHER"

if __name__=='__main__' : 
    
    handler = IGBRequest() 
    
    #handler.getAllGames()
    #handler.getGameByName("fifa",fields=["name","age_ratings"])

    resp = handler.getGameByName("fifa",fields=["name"])
    resp = handler.getGameByName("tom clancy",fields=["name","category","summary"])

    #resp = handler.getAllGames()
    print(resp)