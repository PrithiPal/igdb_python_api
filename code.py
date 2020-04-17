import requests 
import os 
import sys 



class IGBRequest : 

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


        self.GENRES_FIELDS_ALL=[
            'created_at',
            'name',
            'slug',
            'updated_at',
            'url'
        ]

        self.DEFAULT_GAME_FIELDS=[
            "name",
            "summary",
            "rating",
            "cover.url",   
            "platforms",
            "screenshots"
        ]

        self.all_genres_count = 0 
        self.all_games_count = 0 


    def __str__(self) : 
        return "IGDB API FETCHER"

    def __getGamesRequest(self,params_args,sub_link=None) :

        url = os.path.join(self.BASE_URL,"games")
        
        if sub_link is not None : 
            for x in sub_link : 
                url = os.path.join(url,x)
        
        resp = requests.get(url,headers=self.BASE_PARAM,params=params_args)
        return resp.json()

    def __getSearchRequest(self,param_args,sub_link=None) : 
        url = os.path.join(self.BASE_URL,"search")
        
        if sub_link is not None : 
            for x in sub_link : 
                url = os.path.join(url,x)
        
        resp = requests.get(url,headers=self.BASE_PARAM,params=param_args)
        return resp.json()

    def __getCounts(self) : 

        PARAMS = self.__updateFields()
        return self.__getGamesRequest(PARAMS,["count"])


    def __updateFields(self,kwargs) : 
        
        PARAMS={}
        
        if 'fields' in kwargs : 
            FIELDS=",".join(kwargs['fields'])
            PARAMS = {'fields':FIELDS}
        else:
            PARAMS['fields']=','.join(self.DEFAULT_GAME_FIELDS)

        return PARAMS

    def getTopnGames(self,n=10,**kwargs) : 
        
        PARAMS = self.__updateFields(kwargs)
        PARAMS['limit'] = n 

        return self.__getGamesRequest(PARAMS)


    def getGameById(self,id=1,**kwargs) : 
        
        PARAMS = self.__updateFields(kwargs)
        PARAMS['where id'] = id 

        return self.__getGamesRequest(PARAMS)


    def getGameByName(self,name,**kwargs) : 
        
        PARAMS = self.__updateFields(kwargs)
        PARAMS['search'] = str(name)

        return self.__getGamesRequest(PARAMS)


        

if __name__=='__main__' : 
    
    handler = IGBRequest() 

    #resp = handler.getTopnGames(n=500)
    resp = handler.getGameById(id=4,fields=['name'])
    
    print(resp)  
