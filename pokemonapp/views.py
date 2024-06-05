from email.mime import base
import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Pokemon


class PokemonList(TemplateView):
    template_name = 'pokemonapp/pokemon_list.html'
    BASE_URL = 'https://pokeapi.co/api/v2/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get api
        url = self.BASE_URL + 'pokemon?limit=151/'
        response = requests.get(url)
        data = response.json()

        for pokemon_data in data['results']:
            pokemon_indiv_response = requests.get(pokemon_data['url'])
            pokemon_indiv_json = pokemon_indiv_response.json()
            Pokemon.objects.update_or_create(
                id_number=pokemon_indiv_json['id'],
                defaults={
                    'name_en':pokemon_data['name'],
                    'name_ja': self._get_ja_name(pokemon_data['name']),
                    'image_url':pokemon_indiv_json['sprites']['front_default']
                }
            )
        context['pokemon_data'] = Pokemon.objects.all()
        return context

    @staticmethod
    def _get_ja_name(enName):
        url = PokemonList.BASE_URL + f'pokemon-species/{enName.lower()}'
        response = requests.get(url)
        data = response.json()
        
        for name_info in data['names']:
            if name_info['language']['name'] == 'ja-Hrkt':
                return name_info['name']
            else:
                return None
