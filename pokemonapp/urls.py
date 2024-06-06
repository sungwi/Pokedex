from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PokemonList.as_view(), name='pokemon_list'),
    path('pokedex/<int:pk>/', views.Pokemon_detail.as_view(), name='pokemon_detail'),
]
