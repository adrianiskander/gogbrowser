import json, random, time
import requests
from .settings import config


def parse_gog_data(data):
    """
        Keep only data used client-side to save bandwith.
    """
    parsed = {
        'products': [],
        'lastUpdate': ''
    }

    for product in data['products']:
        product = {
            'title': product['title'],
            'rating': product['rating'],
            'price': {
                'finalAmount': product['price']['finalAmount'],
                'symbol': product['price']['symbol']
            },
            'url': product['url']
        }
        parsed['products'].append(product)

    with open(config.GOG_JSON_PARSED_PATH, 'w', encoding='utf-8') as file:
        json.dump(parsed, file, indent=2)    

    print('JOB DONE: Parse GOG data.')


def request_gog_data():
    """
        Request paginated GOG data and save as single json at given path.
    """
    res = requests.get(config.GOG_API_URL, cookies=config.GOG_API_COOKIES)
    data = json.loads(res.text)

    for i in range(2, data['totalPages'] + 1):
        time.sleep(random.randrange(1, 3))
        url = f'{ config.GOG_API_URL }?page={ i }'
        res = requests.get(url, cookies=config.GOG_API_COOKIES)
        res = json.loads(res.text)
        data['products'].extend(res['products'])

    with open(config.GOG_JSON_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)

    parse_gog_data(data)

    print('JOB DONE: Request GOG data.')
