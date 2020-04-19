# igdb_python_api

Python Wrapper to use the IGDB API to fetch Video game data.

### Usage:
- Create an Account and acuquire the API token here : https://api.igdb.com/signup
- Set the enviornmental variable `IGDB_TOKEN` to your token
- To use the Python wrapper, import the class and declare a ` IGBRequest ` object.
``` 
from code import IGBRequest
handler = IGBRequest()
```
The member functions of `handler` performs the `POST` request with the primary argument such as `name` in the example and positional arguments such as `fields` to filter down the results. The output is a `JSON` object
```
handler.getGameByName(name="splinter cell",fields=["name","rating"])
```
creates outputs
```
[{'id': 874, 'name': "Tom Clancy's Splinter Cell: Pandora Tomorrow", 'rating': 83.87425133491749}, {'id': 910, 'name': "Tom Clancy's Splinter Cell", 'rating': 83.4016321809699}, {'id': 66229, 'name': 'Splinter Cell Trilogy'}, {'id': 22632, 'name': "Tom Clancy's Splinter Cell: Essentials"}, {'id': 7469, 'name': "Tom Clancy's Splinter Cell: Double Agent", 'rating': 75.6519863501662}, {'id': 911, 'name': "Tom Clancy's Splinter Cell: Chaos Theory", 'rating': 84.4553761866856}, {'id': 53944, 'name': "Tom Clancy's Splinter Cell: Blacklist - Digital Deluxe Edition"}, {'id': 562, 'name': "Tom Clancy's Splinter Cell: Conviction", 'rating': 77.6105219566901}, {'id': 1305, 'name': "Tom Clancy's Splinter Cell: Blacklist", 'rating': 82.5718633441144}, {'id': 20573, 'name': "Tom Clancy's Splinter Cell Trilogy HD"}]
```
Some available filtering positional arguments are 
- `limit`
- `search`
- `exclude`
- `where`

Refer to the IGDB official documentation for query meanings. 
Other examples: 
```
handler.getGameByName(name="splinter cell",fields=["*"],exclude=['summary'],limit=2)
```
```
handler.getGameByName(name="splinter cell",fields=["name","rating","platforms"])
```
```
handler.getTopnPopularGames(n=5,fields=['name','cover','platforms','genres'])
```

```
handler.getTopnPopularGames(n=2,fields=['name'],where="platforms = (13,24)")
```
### To do :
- Creating unit tests
- Caching support 


### Notes : 

- IGDB API : https://api-docs.igdb.com/
