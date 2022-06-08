from time import sleep
import requests
from bs4 import BeautifulSoup
import vk_api

vk_session = vk_api.VkApi(token="vk1.a.7aZ4dsmqKu_OKJwO-FezhmhQjgemguczMCzD6Z5C2ToGiwNiSX7U-0DEGsNLS1-zAVkVVi-0VEQPrz93vztJF3EToVRwKY06me2QClgARMdALoy3ujHf-RKSOD1ZzHcuBLTnL2DylPqIZRg3KW9L_qHiqrJwL_ou-0u_2qF87aBL5VGyqvAE7HwrAq4XhDF8")
vk = vk_session.get_api()

normal_price = 2350
message = "Цена Solana меньше 2.350 руб"

url = "https://coinmarketcap.com/ru/currencies/green-satoshi-token/" #"https://coinmarketcap.com/ru/currencies/solana/"

headers = {
    'authority': 'coinmarketcap.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'gtm_session_first=%222022-06-02T13%3A01%3A28.611Z%22; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221812481b591980-0424160a957d86-1c655926-1440000-1812481b592d92%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fyandex.ru%2F%22%7D%2C%22%24device_id%22%3A%221812481b591980-0424160a957d86-1c655926-1440000-1812481b592d92%22%7D; _ga=GA1.2.499422437.1654174890; _gid=GA1.2.259051909.1654601531; gtm_session_last=%222022-06-07T18%3A27%3A51.476Z%22; _dc_gtm_UA-40475998-1=1',
    'referer': 'https://yandex.ru/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Yandex";v="22"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.1.985 Yowser/2.5 Safari/537.36',
}

while True:

        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, 'lxml')

        price = soup.find('div', class_ = "priceValue").find('span').text

        price = price[1:].replace(',', '')

        if float(price) <= normal_price:
            vk.messages.send(user_id=456149681, random_id=0, message=message)
            sleep(60)
