from datetime import date

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import CardInfo
from .shop_scrapers.shop_401_games import card_prices_401_helper


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
        card.card_prices[0]['401_games'] = card_prices_401_helper(card.name, card.card_sets)
        card.save()
        data = {'message': 'Last updated date has been updated.'}
        return JsonResponse(data)
