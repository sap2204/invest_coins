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
        coin_name = coin.find('.name')[0]

        coin_weight = coin.find('.weight')[0]

        coin_me = coin.find('li')[0]

        coin_nominal = coin.find('li')[4]

        coin_price = coin.find('.selling-price')[0]
        
        print(coin_name.text)
        print(coin_weight.text)
        print(coin_me.text)
        print(coin_nominal.text)
        print(coin_price.text)
        print()

 
        


asession.run(get_jtbank)


