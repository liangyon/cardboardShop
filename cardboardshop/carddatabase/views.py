from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import CardInfo
import random


def index(request):
    # Get a set of 5 random cards
    random_cards = CardInfo.objects.order_by('?')[:5]
    context = {'random_cards': random_cards}
    return render(request, 'carddatabase/home.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def card_detail(request, card_id):
    card = get_object_or_404(CardInfo, id=card_id)
    return render(request, 'carddatabase/card_detail.html', {'card': card})
