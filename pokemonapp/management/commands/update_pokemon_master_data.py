from django.core.management.base import BaseCommand
from pokemonapp.utils import (
    fetch_pokemon_data
)

"""
モデル等の修正があった場合に、実行
update_pokemon_master_data
"""

class Command(BaseCommand):
    BASE_URL = 'https://pokeapi.co/api/v2/'
    def handle(self, *args, **kwargs):
        fetch_pokemon_data()