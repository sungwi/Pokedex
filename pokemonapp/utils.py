"""
汎用関数
"""

import requests
from .models import Pokemon
from tqdm import tqdm
from django.core.cache import cache

BASE_URL = 'https://pokeapi.co/api/v2/'

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
        Pokemon.objects.update_or_create(
            id_number=pokemon_indiv_json['id'],
            defaults={
                'name_en':pokemon_data['name'],
                'name_ja': get_ja_name(pokemon_data['name']),
                'image_url':pokemon_indiv_json['sprites']['front_default']
            }
        )

"""
英名から日名の取得
"""
def get_ja_name(enName):
        url = BASE_URL + f'pokemon-species/{enName.lower()}'
        response = requests.get(url)
        data = response.json()
        
        for name_info in data['names']:
            if name_info['language']['name'] == 'ja-Hrkt':
                return name_info['name']
            else:
                return None