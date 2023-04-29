# one-off command

from bs4 import BeautifulSoup
import requests
from sapdb.models import Food, Use, Pack
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load golden pack foods into the database'

    def handle(self, *args, **options):
      golden: Pack = Pack.objects.get(name="Golden Pack")

      golden_foods = ["https://superautopets.fandom.com/wiki/Avocado", "https://superautopets.fandom.com/wiki/Banana", "https://superautopets.fandom.com/wiki/Blueberry", "https://superautopets.fandom.com/wiki/Cherry", "https://superautopets.fandom.com/wiki/Chocolate_Cake", "https://superautopets.fandom.com/wiki/Egg", "https://superautopets.fandom.com/wiki/Eggplant", "https://superautopets.fandom.com/wiki/Tomato", "https://superautopets.fandom.com/wiki/Onion"]

      for food in golden_foods:

        response = requests.get(food)
        soup = BeautifulSoup(response.text, 'html.parser')

        name = soup.find('span', class_='mw-page-title-main').text.strip()
        divs = soup.find_all('div', class_='pi-data-value')
        tier = divs[0].text.strip()
        effect = divs[1].text.strip()

        food = Food.objects.create(
            tier=tier,
            name=name,
            image=f'{name}.webp',
            effect=effect,
        )

        golden.foods.add(food)
        food.packs.add(golden)
