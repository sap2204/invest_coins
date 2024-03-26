from requests_html import AsyncHTMLSession
from fake_useragent import UserAgent


user = UserAgent().random
header = {"user_agent": user}

url = "https://ndb24.ru/bank/coins.html"

asession = AsyncHTMLSession()


async def get_ndb():
    r = await asession.get(url=url, headers=header)

    coin_list = r.html.find('.col-sm-8')
    
    for coin in coin_list:
        coin_name = coin.find('h6')[0]

        coin_weight = coin.find('li')[2]

        coin_me = coin.find('li')[1]

        coin_nominal = coin.find('li')[0]

        coin_price = coin.find('li')[6]

        print(coin_name.text)
        print(coin_weight.text)
        print(coin_me.text)
        print(coin_nominal.text)
        print(coin_price.text)
        print()


asession.run(get_ndb)