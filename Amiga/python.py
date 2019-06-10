import requests
import sys
url = 'http://www.omdbapi.com/?apikey=72bc447a&t='+sys.argv[1]


k = requests.get(url)
json_data = k.json()


for key,v  in json_data.items():
       if key == 'Ratings':      
	 print v[1].get('Source') + ':' +  v[1].get('Value')
