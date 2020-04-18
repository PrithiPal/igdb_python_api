import requests 
import os 
import sys 
import field_info


class IGBRequest : 

    def __init__(self) : 
        self.BASE_URL="https://api-v3.igdb.com/"
        self.SECRET_TOKEN=os.getenv("IGDB_TOKEN")
        self.BASE_PARAM = {'user-key':self.SECRET_TOKEN,
                           'Accept' : 'application/json'
                          }

        self.GAME_FIELDS_ALL=field_info.GAME_FIELDS_ALL
        self.GAME_CATEGORY_MAP=field_info.GAME_CATEGORY_MAP
        self.GAME_STATUS_MAP=field_info.GAME_STATUS_MAP
        self.GENRES_FIELDS_ALL=field_info.GAME_FIELDS_ALL
        self.DEFAULT_GAME_FIELDS=field_info.DEFAULT_GAME_FIELDS
        
        self.GENRE_MAP =  self.__setGenresMap()

        self.all_genres_count = 0 
        self.all_games_count = 0 

    def __str__(self) : 
        return "IGDB API FETCHER"

    def __getGamesRequest(self,params_args,sub_link=None) :

        url = os.path.join(self.BASE_URL,"games")
        
        if sub_link is not None : 
            for x in sub_link : 
                url = os.path.join(url,x)
        print(params_args)
        
        resp = requests.post(url,headers=self.BASE_PARAM,data=params_args)
        return resp.json()

    def __getSearchRequest(self,param_args,sub_link=None) : 
        url = os.path.join(self.BASE_URL,"search")
        
        if sub_link is not None : 
            for x in sub_link : 
                url = os.path.join(url,x)
        
        print(param_args)
        resp = requests.get(url,headers=self.BASE_PARAM,params=param_args)
        return resp.json()

    def __getGenreRequest(self,params_args,sub_link=None) :

        url = os.path.join(self.BASE_URL,"genres")
        
        if sub_link is not None : 
            for x in sub_link : 
                url = os.path.join(url,x)
        
        resp = requests.post(url,headers=self.BASE_PARAM,data=params_args)
        return resp.json()


    def __processQuery(self,kwargs) : 
        
        PARAMS=""
        
        ## fields query 
        if 'fields' in kwargs : 
            FIELDS=",".join(kwargs['fields'])  
        else:
            FIELDS=','.join(self.DEFAULT_GAME_FIELDS)
        PARAMS+="fields {} ;".format(FIELDS)

        # where query 
        if 'where' in kwargs: 
            PARAMS+="where {} ; ".format(kwargs['where'])

        if 'limit' in kwargs : 
            PARAMS+="limit {} ;".format(kwargs['limit'])

        if 'search' in kwargs :
            PARAMS+="search \"{}\" ;".format(kwargs['search'])

        if 'exclude' in kwargs : 
            EXCLUDE=",".join(kwargs['exclude'])  
            PARAMS+="exclude {} ;".format(EXCLUDE)

        return PARAMS

    def __setGenresMap(self) : 

        PARAMS = "fields name ;"
        obj = self.__getGenreRequest(PARAMS)
        

        ret = {}
        for genre in obj: 
            ret[genre['id']]=genre['name']

        return ret

    def getTopnGames(self,n=10,**kwargs) : 
        
        kwargs['limit']=n
        
        PARAMS = self.__processQuery(kwargs)
        
        return self.__getGamesRequest(PARAMS)


    def getGameById(self,game_id,**kwargs) : 
        
        if isinstance(game_id,int) : 
            kwargs['where']= "id = {}".format(game_id)
        elif isinstance(game_id,list) : 
            kwargs['where'] = "id = ({})".format(','.join([str(x) for x in game_id]))

        PARAMS = self.__processQuery(kwargs)

        print(PARAMS)
        
        return self.__getGamesRequest(PARAMS)


    def getGameByName(self,name,**kwargs) : 
        
        kwargs['search'] = str(name)
        PARAMS = self.__processQuery(kwargs)
        
        return self.__getGamesRequest(PARAMS)

    def getTopnPopularGames(self,n,**kwargs):

        PARAMS = self.__processQuery(kwargs)
        PARAMS+="sort popularity desc ;"

        return self.__getGamesRequest(PARAMS)


     

if __name__=='__main__' : 
    
    handler = IGBRequest() 

    #resp = handler.getTopnGames(n=2,fields=['name'])
    #resp = handler.getGameById(game_id=2,fields=['name'])
    #resp = handler.getGameByName(name="tom clancy",fields=["name","rating"])

    #print(resp)
    
