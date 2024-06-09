from django.core.management.base import BaseCommand
from django.db import models
from pokemonapp.models import Pokemon
from tqdm import tqdm

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # 同じidが複数あるポケモンを取得
        duplicates = Pokemon.objects.values('id_number')\
                                    .annotate(count_id_number=models.Count('id_number'))\
                                    .filter(count_id_number__gt=1)
        for duplicate in tqdm(duplicates):
            pokemons = Pokemon.objects.filter(id_number=duplicate['id_number'])
            pokemon_to_keep = pokemons.first()
            pokemon_to_delete = pokemons.exclude(id=pokemon_to_keep.id)
            pokemon_to_delete.delete()
