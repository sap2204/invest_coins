from requests_html import AsyncHTMLSession
from fake_useragent import UserAgent


user = UserAgent().random
header = {"user_agent": user}

url = "https://www.nmbank.ru/uslugi/chastnym-licam/monety-iz-dragocennyh-metallov/"

asession = AsyncHTMLSession()


async def get_nmbank():
    r = await asession.get(url=url, headers=header)

    #coin_area = r.html.find('.item-content')
    coin_list = r.html.find('.item-content')[0].html

    print(coin_list)


asession.run(get_nmbank)