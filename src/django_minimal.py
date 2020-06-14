from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string

from dominion.config import Config
from dominion.draw import pick_cards
from dominion.model import CardDeck

DEBUG = True
SECRET_KEY = 'f5ov167pjh156u7$l2z89b9jblhf4f4n9fv316$!0o3ova$bxx'
ROOT_URLCONF = __name__
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['./templates'],
}]


def home(request):
    title = 'Dominion'
    parameters = {'title': title}

    if request.method == 'POST':
        config = Config()
        picked_cards = [card.get_name() for card in pick_cards(CardDeck(config), config.get_num_of_picks())]
        parameters['picked_cards'] = picked_cards

    html = render_to_string('home.html', parameters)
    return HttpResponse(html)


urlpatterns = [
    url(r'^$', home, name='homepage')
]
