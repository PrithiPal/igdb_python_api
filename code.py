import requests 
import os 
import sys 



class IGBRequest : 
    

    def getGames(self) : 
        url = os.path.join(self.BASE_URL,"games")
        resp = requests.get(url,headers=self.BASE_PARAM)
        print(resp.text)

    def getGameById(self,id) : 
        url = os.path.join(self.BASE_URL,"games")
        resp = requests.get(url,headers=self.BASE_PARAM,params={'id':id,'fields':['name']})
        print(resp.text)       

    def getGenres(self) : 
        url = os.path.join(self.BASE_URL,"genres")
        resp = requests.get(url,headers=self.BASE_PARAM)
        print(resp.text)        

    def __init__(self) : 
        self.BASE_URL="https://api-v3.igdb.com/"
        self.SECRET_TOKEN=os.getenv("IGDB_TOKEN")
        self.BASE_PARAM = {'user-key':self.SECRET_TOKEN}

    def __str__(self) : 
        return "IGDB API FETCHER"

if __name__=='__main__' : 
    
    handler = IGBRequest() 
    #handler.getGenres()
    handler.getGameById(88041)