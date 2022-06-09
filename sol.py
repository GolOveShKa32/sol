from time import sleep
import requests
from bs4 import BeautifulSoup
import vk_api

vk_session = vk_api.VkApi(token="vk1.a.7aZ4dsmqKu_OKJwO-FezhmhQjgemguczMCzD6Z5C2ToGiwNiSX7U-0DEGsNLS1-zAVkVVi-0VEQPrz93vztJF3EToVRwKY06me2QClgARMdALoy3ujHf-RKSOD1ZzHcuBLTnL2DylPqIZRg3KW9L_qHiqrJwL_ou-0u_2qF87aBL5VGyqvAE7HwrAq4XhDF8")
vk = vk_session.get_api()

url = "https://coinmarketcap.com/ru/currencies/green-satoshi-token/" #"https://coinmarketcap.com/ru/currencies/solana/"

headers = {
    'authority': 'coinmarketcap.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
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
    try:
        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, 'lxml')

        price = soup.find('div', class_ = "priceValue").find('span').text

        price = price[1:].replace(',', '')

        if float(price) <= 33:
            for x in range(3):
                vk.messages.send(user_id=456149681, random_id=0, message=f"продавай кросы, цена GST {price} руб")
                sleep(3)
            sleep(60*60)

        elif float(price) >= 39:
            for x in range(3):
                vk.messages.send(user_id=456149681, random_id=0, message=f"покупай кросы, цена GST {price} руб")
                sleep(3)
            sleep(60*60)
        sleep(10)
    except:
        print("error")
