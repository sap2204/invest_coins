from requests_html import AsyncHTMLSession
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

url = "https://ndb24.ru/bank/coins.html"

asession = AsyncHTMLSession()


async def get_ndb():
    r = await asession.get(url=url, headers=header)

    coin_list = r.html.find('.col-sm-8')
    
    for coin in coin_list:
        coin_name = coin.find('h6')[0].text

        coin_weight = coin.find('li')[2].text

        coin_me = coin.find('li')[1].text

        coin_nominal = coin.find('li')[0].text

        coin_price = coin.find('li')[6].text

        print(coin_name)
        print(coin_weight)
        print(coin_me)
        print(coin_nominal)
        print(coin_price)
        print()


asession.run(get_ndb)