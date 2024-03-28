from requests_html import AsyncHTMLSession, HTML
from fake_useragent import UserAgent
import re
import requests


class SimpleScraper:
    def __init__(self, url:str):
        # Паттерны регулярных выражений
        self.weight_pattern = r'\d+[.,]\d+'
        self.me_pattern = r'(серебро|золото)'
        self.nominal_pattern = r'\d+'
        self.price_pattern = r'\d+'

        # Фейковый юзер агент
        self.user = UserAgent().random
        self.header = {"user_agent": self.user}

        # Асинхронная сессия
        self.asession = AsyncHTMLSession()

        # Адрес сайта
        self.url = url


        # Метод получения данных с сайтов
        async def get_data_from_bank(self,
                                     coin_list_selector = None,
                                     coin_name_selector = None,
                                     name_index = 0,
                                     coin_weight_selector = None,
                                     weight_index = 0,
                                     coin_me_selector = None,
                                     me_index = 0,
                                     coin_nominal_selector = None,
                                     nominal_index = 0
                                     coin_price_selector = None,
                                     price_index = 0
                                     ):
            try:
                r = await self.asession.get(url=self.url, headers=self.header)
                coin_list = r.html.find(coin_list_selector)

                for coin in coin_list:
                    coin_name = coin.find(coin_name_selector)[name_index].text

                    coin_weight = coin.find(coin_weight_selector)[weight_index].text

                    coin_me = coin.find(coin_me_selector)[me_index].text

                    coin_nominal = coin.find(coin_nominal_selector)[nominal_index].text

                    coin_price = coin.find(coin_price_selector)[price_index].text

            except requests.exceptions.RequestException as e:
                print(e)
            
            return coin_name, coin_weight, coin_me, coin_nominal, coin_price

            