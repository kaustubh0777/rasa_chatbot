import requests
import json

def api_stock_price(stockname):

    #url = "https://yh-finance.p.rapidapi.com/auto-complete"
    #url = "https://query1.finance.yahoo.com/v11/finance/quoteSummary/{stockname}"
    #querystring = {"q":stockname,"region":"IN"}
    #querystring = {"symbol":"AMRN","region":"US"}

    f = open("apikeys.txt","r")
    keys = f.readlines()
    apikey = keys[0][keys[0].find(" ")+1:]
    f.close()

    url = "https://yh-finance.p.rapidapi.com/auto-complete"
    querystring = {"q":stockname,"region":"US"}

    headers = {
        "X-RapidAPI-Key": apikey,
        "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    parse_symbol = json.loads(response.text)
    symbolname = parse_symbol['quotes'][0]['symbol']

    url1 = "https://yh-finance.p.rapidapi.com/stock/v3/get-chart"
    querystring1 = {"interval":"1d","symbol":symbolname,"range":"5d","region":"US"}
    response1 = requests.get(url1, headers=headers, params=querystring1)
    parse_text = json.loads(response1.text)

    stockprice = parse_text['chart']['result'][0]['indicators']['quote'][0]['close'][-1]
    return stockprice

#api_stock_price("AMRN")
#api_stock_price("tesla")