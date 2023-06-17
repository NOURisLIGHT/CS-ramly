#import requests adn time modules
import requests
import time

#global variables (api_key and bot_key and chat_id and limit and time_interval)
api_key = "304deb64-0ef9-4d7b-8fc5-77b41f4175df"
bot_key = "5349411076:AAF9nL21L18UrH4z0CPNgbqUypRk7-ctkYY"
chat_id = "1450142197"
limit = 51000 #when the price goes below this, it will send us a message
time_interval = 5 * 60  # chechks the price every 5 minutes (5 * 60)

def get_price():
    url = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        'start':'1',
        'limit':'5000',
        'convert':'USD'
    }  
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers).json()
    return response
    
print(get_price)

