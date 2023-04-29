# one-off command

from bs4 import BeautifulSoup
import requests
from sapdb.models import Food, Trigger, Pack
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load foods into the database'

    def handle(self, *args, **options):
      turtle: Pack = Pack.objects.get(name="Turtle Pack")
      puppy: Pack = Pack.objects.get(name="Puppy Pack")
      star: Pack = Pack.objects.get(name="Star Pack")

      foods = 'https://superautopets.fandom.com/wiki/Food'
      response = requests.get(foods)
      soup = BeautifulSoup(response.text, 'html.parser')

      tbody = soup.find('tbody')
      trows = tbody.select('tr')

      for row in trows:
        if row.select_one('td:nth-of-type(1)'):
          tier = row.select_one('td:nth-of-type(1)').text.strip()
          name = row.select_one('td:nth-of-type(2)').text.strip()
          effect = row.select_one('td:nth-of-type(3)').text.strip()
          in_turtle = row.select_one('td:nth-of-type(4)').text.strip()
          in_puppy = row.select_one('td:nth-of-type(5)').text.strip()
          in_star = row.select_one('td:nth-of-type(6)').text.strip()

          if type(tier) == str:
            tier = 0

          food = Food.objects.create(
              tier=tier,
              name=name,
              image=f'{name}.webp',
              effect=effect,
          )

          if in_turtle:
            turtle.foods.add(food)

          if in_puppy:
            puppy.foods.add(food)

          if in_star:
            star.foods.add(food)
