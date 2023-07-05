from datetime import date
import datetime

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import CardInfo
from .shop_scrapers.shop_401_games import card_prices_401_helper
from .shop_scrapers.shop_ac_games import card_prices_ac_helper


def index(request):
    # Get a set of 5 random cards
    random_cards = CardInfo.objects.order_by('?')[:25]
    cards = CardInfo.objects.all()
    context = {'random_cards': random_cards, 'cards': cards}
    return render(request, 'carddatabase/home.html', context)


def card_detail(request, sanitized_card_name):
    card = get_object_or_404(CardInfo, sanitized_name=sanitized_card_name)
    update_records(request, card.id)
    return render(request, 'carddatabase/card_detail.html', {'card': card})


def update_records(request, card_id=None):
    if not card_id:
        card_id = request.POST.get('card_id')
    card = CardInfo.objects.get(id=card_id)
    if card.updated_date.date() != datetime.datetime.today().date():
        card.updated_date = date.today()

        card.card_prices[0]['401_games'] = card_prices_401_helper(card.name, card.card_sets)
        card.card_prices[0]['AC_games'] = card_prices_ac_helper(card.name)

        card.save()
        data = {'message': 'Last updated date has been updated.'}
        return JsonResponse(data, status=200)
    else:
        data = {'message': 'Already updated today!!.'}
        return JsonResponse(data, status=200)
