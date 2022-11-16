import requests
import json

def market_news():
	f = open("apikeys.txt","r")
	keys = f.readlines()
	apikey = keys[0][keys[0].find(" ")+1:]
	f.close()
	
	url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/ne/news"
	headers = {
		"X-RapidAPI-Key": apikey,
		"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
		}
	response = requests.request("GET", url, headers=headers)
	parse_text=json.loads(response.text)
	market_news=""
	for i in range(4):
		market_news+=parse_text[i]['title']+'\n'
	return market_news


print(market_news())
