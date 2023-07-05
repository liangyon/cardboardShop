import threading

import requests
from bs4 import BeautifulSoup


def card_prices_401_helper(card_name, card_sets, card_edition=None):
    urls = []
    set_informations = []
    for sets in card_sets:
        set_informations.append(sets['set_code'].replace(' ', '-') + ' ' + sets['set_rarity'].replace(' ', '-'))
        urls.append(("https://store.401games.ca/products/"
                     + (card_name.replace(' ', '-').replace(':', '').replace('.', '-').replace('!', '').replace('?', '')
                        .replace('\'', '').replace('\"', '')
                        .replace(',', '').replace('@', '').replace('/', '-')).replace('---', '-').replace('--', '-')
                     + "-" + sets['set_code'].replace(' ', '-')
                     + "-" + sets['set_rarity'].replace(' ', '-') + "-" + "1st-edition").replace('--', ''))

    results = []

    def worker_data(url, set_information):
        result = get_data(url, set_information)
        results.append(result)

    # implement multithreading
    threads = []
    i = 0
    for url in urls:
        t = threading.Thread(target=worker_data, args=(url, set_informations[i]))
        threads.append(t)
        t.start()
        i += 1

    for t in threads:
        t.join()

    print(results)
    return results


def get_data(url, set_information):
    try:
        response = requests.get(url)
        html = response.content

        # Create a BeautifulSoup object
        soup = BeautifulSoup(html, 'html.parser')

        # Extract the title of the webpage
        title = soup.title.string
        print("Title:", title)

        # Extract all the links in the page
        cost = soup.find(id="ProductPrice-product-template").text.strip()
        stock_status = soup.find(id="AddToCartText-product-template").text.strip()
        rarity = set_information
        if stock_status == 'Add to Cart':
            stock_status = 'In Stock'
        else:
            stock_status = 'Out of Stock'

        return [cost, stock_status, rarity]
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print('404 error: page not found')
        else:
            print('HTTP error:', e)
