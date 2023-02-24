import threading

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from datetime import date

from .models import CardInfo
from bs4 import BeautifulSoup
import requests
import random


def index(request):
    # Get a set of 5 random cards
    random_cards = CardInfo.objects.order_by('?')[:5]
    context = {'random_cards': random_cards}
    return render(request, 'carddatabase/home.html', context)


def card_detail(request, card_id):
    card = get_object_or_404(CardInfo, id=card_id)
    return render(request, 'carddatabase/card_detail.html', {'card': card})


def update_records(request):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        card = CardInfo.objects.get(id=card_id)
        card.updated_date = date.today()
        card.card_prices[0]['401_games'] = _card_prices_401_helper(card.name, card.card_sets)
        card.save()
        data = {'message': 'Last updated date has been updated.'}
        return JsonResponse(data)


def _card_prices_401_helper(card_name, card_sets, card_edition=None):
    url = "https://store.401games.ca/products/pot-of-prosperity-blvo-en065-secret-rare-1st-edition"
    urls = []
    for sets in card_sets:
        urls.append("https://store.401games.ca/products/" + card_name.replace(' ', '-') \
                    + "-" + sets['set_code'].replace(' ', '-') + "-" + sets['set_rarity'].replace(' ',
                                                                                                  '-') + "-" + "1st-edition")

    print(urls)

    results = []

    def worker_data(url):
        result = get_data(url)
        results.append(result)

    # implement multithreading
    threads = []
    for url in urls:
        t = threading.Thread(target=worker_data, args=(url,))

        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(results)
    return results


def get_data(url):
    try:
        response = requests.get(url)
        html = response.content

        # Create a BeautifulSoup object
        soup = BeautifulSoup(html, 'html.parser')

        # Extract the title of the webpage
        title = soup.title.string
        print("Title:", title)

        # Extract all the links in the page
        cost = soup.find(id="ProductPrice-product-template")
        print(cost.text.strip())
        return cost.text.strip()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print('404 error: page not found')
        else:
            print('HTTP error:', e)
    else:
        print(response.content)


