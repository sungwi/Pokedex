import requests
from .utils import (
    fetch_pokemon_data,
)
from django.shortcuts import render, redirect
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

def pokemon_search(request):
        query = request.GET.get('query')
        if query:
            try:
                pokemon = Pokemon.objects.get(name_ja__iexact=query)
                return redirect('pokemon_detail', pk=pokemon.pk)
            except Pokemon.DoesNotExist:
                return render(request, 'pokemonapp/pokemon_not_found.html', {'error': 'ポケモンが見つかりませんでした'})
        return render(request, 'pokemonapp/pokemon_list.html')

class Pokemon_detail(DetailView):
    model = Pokemon
    template_name = 'pokemonapp/pokemon_detail.html'
    context_object_name: 'pokemon'
    # 英語から日本語へのタイプ名のマッピング
    type_mapping = {
        'normal': 'ノーマル',
        'fire': 'ほのお',
        'water': 'みず',
        'electric': 'でんき',
        'grass': 'くさ',
        'ice': 'こおり',
        'fighting': 'かくとう',
        'poison': 'どく',
        'ground': 'じめん',
        'flying': 'ひこう',
        'psychic': 'エスパー',
        'bug': 'むし',
        'rock': 'いわ',
        'ghost': 'ゴースト',
        'dragon': 'ドラゴン',
        'dark': 'あく',
        'steel': 'はがね',
        'fairy': 'フェアリー',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_mapping'] = self.type_mapping
        # 図鑑No前後のポケモンの情報を取得
        pokemon = self.get_object()
        
        prev_pokemon = Pokemon.objects.filter(id__lt=pokemon.id).order_by('-id').first()
        next_pokemon = Pokemon.objects.filter(id__gt=pokemon.id).order_by('id').first()
        context['prev_pokemon'] = prev_pokemon
        context['next_pokemon'] = next_pokemon
        
        return context
