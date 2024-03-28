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


asession = AsyncHTMLSession()

url = "https://timerbank.ru/individuals/metal-coins/?type=list"

async def get_timer():
    r = await asession.get(url=url, headers= header)

    coin_list = r.html.find('.coinMiniCard')

    for coin in coin_list:
        coin_name = coin.find('.cmc_name')[0].text

        coin_weight = coin.find('li')[3].text

        coin_me = coin.find('li')[1].text

        coin_nominal = coin.find('li')[0].text

        coin_price = coin.find('p')[1].text

        print(coin_name)
        print(coin_weight)
        print(coin_me)
        print(coin_nominal)
        print(coin_price)
        print()

    



asession.run(get_timer)