import requests
from .utils import (
    fetch_pokemon_data,
)
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Pokemon


class PokemonList(TemplateView):
    template_name = 'pokemonapp/pokemon_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not Pokemon.objects.exists():
            fetch_pokemon_data()
            
        context['pokemon_data'] = Pokemon.objects.all()
        return context

class Pokemon_detail(DetailView):
    model = Pokemon
    template_name = 'pokemonapp/pokemon_detail.html'
    context_object_name: 'pokemon'