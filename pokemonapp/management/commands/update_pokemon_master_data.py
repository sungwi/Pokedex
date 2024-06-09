from django.core.management.base import BaseCommand
from pokemonapp.utils import (
    fetch_pokemon_data
)

class Command(BaseCommand):
    BASE_URL = 'https://pokeapi.co/api/v2/'
    def handle(self, *args, **kwargs):
        fetch_pokemon_data()