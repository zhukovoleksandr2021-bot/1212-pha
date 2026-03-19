from itertools import count

import requests

url = 'https://coinmarketcap.com/'

response_text = (requests.get(url).text)

parsed_text = response_text.split('<span>')

coins = []

for parsed in  parsed_text:
    if parsed.startswith("$"):
        for item in parsed.split('</span>'):
            if item.startswith("$"):
                coins.append(item)


print(f'Bitcoin: {coins[1]}')
print(f'Ethereum: {coins[2]}')
print(f'All: {coins}')

def get_price(price:str):
    return float(price[1:].replace(",", ""))

bit_coin_price = get_price(coins[1])

count = int(input("Введіть число:"))
print(f'{count} BTC = ${bit_coin_price*count:.2f}')