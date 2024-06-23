"""
汎用関数
"""

from urllib.request import BaseHandler
import requests
from .models import Pokemon
from tqdm import tqdm
from django.core.cache import cache

BASE_URL = 'https://pokeapi.co/api/v2/'
LANGUAGE = 'ja'

"""
APIからポケモンのマスタ情報の追加・更新
"""
def fetch_pokemon_data():
    # キャッシュ内にあれば、それを返す。（速度改善のため）
    cache_key = 'pokeon_data'
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data
        
    # get api
    url = BASE_URL + 'pokemon?limit=151/'
    response = requests.get(url)
    data = response.json()
    cache.set(cache_key, data, timeout=60*10) # マスタをキャッシュ内に10分間保持
    # TODO: ポケモン151体：02:11→01:48　もう少し速度改善したい

    for pokemon_data in tqdm(data['results']):
        pokemon_indiv_response = requests.get(pokemon_data['url'])
        pokemon_indiv_json = pokemon_indiv_response.json()
        # タイプが複数ある対応処理
        types = [type_data['type']['name'] for type_data in pokemon_indiv_json['types']]
        # 分類、日本名、説明
        species_response = requests.get(pokemon_indiv_json['species']['url'])
        species_data = species_response.json()
        name_ja = next((name_info['name'] for name_info in species_data['names'] if name_info['language']['name'] == LANGUAGE))
        genus = next((genera_info['genus'] for genera_info in species_data['genera'] if genera_info['language']['name'] == LANGUAGE))
        text = next((text_info['flavor_text'].replace('\n', '').replace('　', '') for text_info in species_data['flavor_text_entries'] if text_info['language']['name'] == LANGUAGE))
        # 特性
        ability_urls = [ability_dict['ability']['url'] for ability_dict in pokemon_indiv_json['abilities']]
        ability = []
        for ability_url in ability_urls:
            ability_response = requests.get(ability_url)
            ability_data = ability_response.json()
            ability.append(next((ability_info['name'] for ability_info in ability_data['names'] if ability_info['language']['name'] == LANGUAGE)))
        Pokemon.objects.update_or_create(
            id_number=pokemon_indiv_json['id'],
            defaults={
                'name_en':pokemon_data['name'],
                'name_ja': name_ja,
                'image_url':pokemon_indiv_json['sprites']['front_default'],
                'type': types,
                'genus': genus,
                'text': text,
                'ability': ability
            }
        )