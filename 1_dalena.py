from requests_html import AsyncHTMLSession
from fake_useragent import UserAgent
import re


# Паттерны регулярных выражений
weight_pattern = r'\d+[.,]\d+'
me_pattern = r'(серебро|золото)'
nominal_pattern = r'\d+'
price_pattern = r'\d+'


# Создание фейкового юзер агента
user = UserAgent().random
header = {"user_agent": user}





url = "https://www.dalenabank.ru/chastnym-klientam/monety/"

asession = AsyncHTMLSession()


async def get_dalenabank():
    r = await asession.get(url, headers=header)
    coin_list = r.html.find('.bx-newslist-block')
    
    for coin in coin_list:
        coin_name = coin.find('.bx-newslist-title')[0]

        coin_weight = coin.find('.bx-newslist-other')[0]

        coin_me = coin.find('.bx-newslist-other')[1]

        coin_nominal = coin.find('.bx-newslist-other')[2]

        coin_price = coin.find('.bx-newslist-other')[3]
        
        print(coin_name.text)
        print(coin_weight.text)
        print(coin_me.text)
        print(coin_nominal.text)
        print(coin_price.text)
        print()


asession.run(get_dalenabank)