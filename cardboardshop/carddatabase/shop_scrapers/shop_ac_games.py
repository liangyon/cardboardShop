import requests
from bs4 import BeautifulSoup


def card_prices_ac_helper(card_name):
    results = []
    url = "https://acgamesonline.crystalcommerce.com/products/search?q=" + card_name.replace(' ', '+')

    results = get_data(url, card_name)

    return results


def get_data(url, card_name):
    try:
        response = requests.get(url)
        html = response.content

        # Create a BeautifulSoup object
        soup = BeautifulSoup(html, 'html.parser')

        # Extract all the links in the page
        # I need to get different information here
        results = []
        products = soup.find_all('div', {'class': ['inner']})
        products = products[1:]
        for product in products:
            title = product.find('h4', class_={'name', 'small-12', 'medium-4'}).get_text()
            stock_price = product.find('span', class_={'name', 'small-12', 'medium-4'}).get_text()
            if card_name in title:
                results.append(title + " " + stock_price.replace("\n", "").replace("\r", ""))
        return results

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print('404 error: page not found')
        else:
            print('HTTP error:', e)
