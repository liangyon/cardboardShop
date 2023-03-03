from django.urls import path

from . import views
from .views import card_detail

urlpatterns = [
    path('', views.index, name='index'),
    path('card/<str:sanitized_card_name>', views.card_detail, name='card_detail'),
    path('update_records/', views.update_records, name='update_records'),
]