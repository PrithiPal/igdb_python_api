import requests 
import os 
import sys 
import field_info
import shutil

class IGBRequest : 

    def __init__(self,media_path) : 
        assert media_path!=None 
        assert media_path!=""

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
        self.MEDIA_PATH = media_path
        self.IMAGE_BASE_URL="https://images.igdb.com/igdb/image/upload/t_thumb/"

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


    def __processPreQuery(self,kwargs) : 
        
        PARAMS=""
        
        ## fields query 

        if 'fields' in kwargs : 
            FIELDS=",".join(kwargs['fields'])  
        else:
            FIELDS=','.join(self.DEFAULT_GAME_FIELDS)
        
        if 'cover' in kwargs: 
            if kwargs['cover']:
                FIELDS+=", cover.* "

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


    def __processPostQuery(self,orig_resp,kwargs): 
        print("processPostQuery")

        DOWNLOAD_IMAGE=False
        if 'cover' in kwargs : 
            if kwargs['cover']: 
                DOWNLOAD_IMAGE=True

        for obj in orig_resp : 
            if DOWNLOAD_IMAGE:  
                if 'cover' in obj : 
                    image_id=obj['cover']['image_id'] + ".jpg"
                    self.__downloadGameCover(dir_name=self.MEDIA_PATH,image_id=image_id,local_name=image_id)
    

        pass 

    def __setGenresMap(self) : 

        PARAMS = "fields name ;"
        obj = self.__getGenreRequest(PARAMS)
        
        ret = {}
        for genre in obj: 
            ret[genre['id']]=genre['name']

        return ret
        
    def __downloadGameCover(self,dir_name,image_id,local_name) : 
        assert os.path.isdir(dir_name)
        full_link = os.path.join(self.IMAGE_BASE_URL,image_id)
        resp = requests.get(full_link,stream=True)
        local_file = open(os.path.join(dir_name,local_name),'wb')
        resp.raw.decode_content=True 
        shutil.copyfileobj(resp.raw,local_file)
        del resp

    def getTopnGames(self,n=10,**kwargs) : 
        
        kwargs['limit']=n
        PARAMS = self.__processPreQuery(kwargs)
        
        original_response = self.__getGamesRequest(PARAMS)
        self.__processPostQuery(original_response,kwargs)
        return original_response


    def getGameById(self,game_id,**kwargs) : 
        
        if isinstance(game_id,int) : 
            kwargs['where']= "id = {}".format(game_id)
        elif isinstance(game_id,list) : 
            kwargs['where'] = "id = ({})".format(','.join([str(x) for x in game_id]))

        PARAMS = self.__processPreQuery(kwargs)

        print(PARAMS)
        
        original_response = self.__getGamesRequest(PARAMS)
        self.__processPostQuery(original_response,kwargs)
        return original_response


    def getGameByName(self,name,**kwargs) : 
        
        kwargs['search'] = str(name)

        PARAMS = self.__processPreQuery(kwargs)
        
        original_response = self.__getGamesRequest(PARAMS)
        self.__processPostQuery(original_response,kwargs)
        return original_response

    def getTopnPopularGames(self,n,**kwargs):

        PARAMS = self.__processPreQuery(kwargs)
        PARAMS+="sort popularity desc ;"
        PARAMS+="limit {} ;".format(n)

        original_response = self.__getGamesRequest(PARAMS)
        self.__processPostQuery(original_response,kwargs)
        return original_response

    def setMediaPath(self,path) : 
        self.MEDIA_PATH=path 
        pass 



     

if __name__=='__main__' : 
    
    handler = IGBRequest(media_path=".") 

    #resp = handler.getTopnGames(n=2,fields=['name'])
    #resp = handler.getGameById(game_id=2,fields=['name'])
    #resp = handler.getGameByName(name="tom clancy",fields=["name","rating"])

    genre_map=handler.GENRE_MAP
    resp=handler.getTopnPopularGames(n=2,fields=['name'],where="platforms = (13,24)",cover=True)


    ##print(resp)

    #resp = handler.getTopnPopularGames(n=5,fields=['name','cover','platforms','genres'])
    #print(resp)

    #handler.downloadGameCover(dir_name='.',image_id='bbboosegdval1pmsvm9n.jpg',local_name="sample.jpg")
    
