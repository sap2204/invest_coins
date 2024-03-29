from requests_html import AsyncHTMLSession, HTML
from fake_useragent import UserAgent
import re
import requests


class SimpleScraper:
    '''
    Класс для парсинга обычных сайтов, код которых генерируется на сервере
    '''
    def __init__(self, url:str):
        # Паттерны регулярных выражений
        self.weight_pattern = r'\d+[.,]\d+'
        self.me_pattern = r'(серебро|золото)'
        self.nominal_pattern = r'\d+'
        self.price_pattern = r'\d+'

        # Фейковый юзер агент
        self.user = UserAgent().random
        self.header = {"user_agent": self.user}

        
        # Адрес сайта
        self.url = url


        # Метод получения данных с сайтов
    async def get_data_from_bank(self, asession,
                                     coin_list_selector = None,
                                     coin_name_selector = None,
                                     name_index = 0,
                                     coin_weight_selector = None,
                                     weight_index = 0,
                                     coin_me_selector = None,
                                     me_index = 0,
                                     coin_nominal_selector = None,
                                     nominal_index = 0,
                                     coin_price_selector = None,
                                     price_index = 0
                                     ):
            
            try:
                r = await asession.get(url=self.url, headers=self.header)

                # Список монет
                data = []

                coin_list = r.html.find(coin_list_selector)

                for coin in coin_list:
                    # Получения данных со страницы

                    coin_name = coin.find(coin_name_selector)[name_index].text.strip()

                    coin_we = coin.find(coin_weight_selector)[weight_index].text.strip().replace(' ', '')
                    coin_weight = re.search(self.weight_pattern, coin_we).group(0)

                    coin_met = coin.find(coin_me_selector)[me_index].text.strip().lower()
                    coin_me = re.search(self.me_pattern, coin_met).group(0)  + ' ' + re.search(r'\d+', coin_met).group(0) + '-'

                    coin_nom = coin.find(coin_nominal_selector)[nominal_index].text.strip()
                    coin_nominal = re.search(self.nominal_pattern, coin_nom).group(0) + '-' , # добавление разделителя '-'

                    coin_pr = coin.find(coin_price_selector)[price_index].text.strip().replace(' ', '')
                    coin_price = int(re.search(self.price_pattern, coin_pr).group(0))
                
                                      

                    data.append([coin_name, '', coin_price, coin_weight, coin_me, coin_nominal])
            except requests.exceptions.RequestException as e:
                print(e)
            
            return data

            