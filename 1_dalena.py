from base_simple_scraper import SimpleScraper
from requests_html import AsyncHTMLSession
import asyncio

dalena = SimpleScraper("https://www.dalenabank.ru/chastnym-klientam/monety/")

async def main():
    asession = AsyncHTMLSession()
    task = dalena.get_data_from_bank(asession,
                                     coin_list_selector = '.bx-newslist-block',
                                     coin_name_selector = '.bx-newslist-title',
                                     name_index = 0,
                                     coin_weight_selector = '.bx-newslist-other',
                                     weight_index = 0,
                                     coin_me_selector = '.bx-newslist-other',
                                     me_index = 1,
                                     coin_nominal_selector = '.bx-newslist-other',
                                     nominal_index = 2,
                                     coin_price_selector = '.bx-newslist-other',
                                     price_index = 3)
    return await asyncio.gather(task)

results = asyncio.run(main())
print(results)
'''
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
        coin_name = coin.find('.bx-newslist-title')[0].text

        coin_weight = coin.find('.bx-newslist-other')[0].text

        coin_me = coin.find('.bx-newslist-other')[1].text

        coin_nominal = coin.find('.bx-newslist-other')[2].text

        coin_price = coin.find('.bx-newslist-other')[3].text
        
        print(coin_name)
        print(coin_weight)
        print(coin_me)
        print(coin_nominal)
        print(coin_price)
        print()


asession.run(get_dalenabank)

'''