from requests_html import AsyncHTMLSession, HTML
from fake_useragent import UserAgent
import re

# Паттерны регулярных выражений
weight_pattern = r'\d+[.,]\d+'
me_pattern = r'(серебро|золото)'
nominal_pattern = r'\d+'
price_pattern = r'\d+'
user = UserAgent().random
header = {"user_agent": user}


user = UserAgent().random
header = {"user_agent": user}

url = "https://www.energotransbank.com/private/precious_coins/yubileynye-monety/"

asession = AsyncHTMLSession()

# ['Серебро', ' 8.53\xa0грамм', ' 925/1000\xa0проба']
async def get_nmbank():
    r = await asession.get(url=url, headers=header)

    coin_list = r.html.find('.coins__item')

    for coin in coin_list:
        coin_name = coin.find('span')[0].text

        coin_description = coin.find('.composition')[0].text.split(',')

        coin_weight = coin_description[1]

        coin_me = coin_description[0] + ' ' + coin_description[2]

        coin_nominal = None

        coin_price = coin.find('.price ')[0].text

        print(coin_name)
        print(coin_weight)
        print(coin_me)
        print(coin_nominal)
        print(coin_price)

        print()
    
    
    


    
    
   


asession.run(get_nmbank)