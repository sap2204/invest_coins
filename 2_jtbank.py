from requests_html import AsyncHTMLSession
from fake_useragent import UserAgent


user = UserAgent().random
header = {"user_agent": user}


url = "https://jtbank.ru/fizicheskim-litsam/monety/"

asession = AsyncHTMLSession()

async def get_jtbank():
    r = await asession.get(url, headers=header)
    coin_list = r.html.find('.item')
    print(len(coin_list))

    for coin in coin_list:
        coin_name = coin.find('.name')[0].text

        coin_weight = coin.find('.weight')[0].text

        coin_me = coin.find('li')[0].text

        coin_nominal = coin.find('li')[4].text

        coin_price = coin.find('.selling-price')[0].text
        
        print(coin_name)
        print(coin_weight)
        print(coin_me)
        print(coin_nominal)
        print(coin_price)
        print()

 
        


asession.run(get_jtbank)


