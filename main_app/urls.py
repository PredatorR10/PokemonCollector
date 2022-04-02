from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('pokemon/', views.PokemonList.as_view(), name="pokemon-list"),
    path('pokemon/new/', views.PokemonCreate.as_view(), name="pokemon-create"),
    path('pokemon/<int:pk>/', views.PokemonDetail.as_view(), name="pokemon-detail"),
    path('pokemon/<int:pk>/update', views.PokemonUpdate.as_view(), name="pokemon-update"),
    path('pokemon/<int:pk>delete', views.PokemonDelete.as_view(), name="pokemon-delete"),
    path('user/<username>/', views.profile, name='profile'),
    path('pokemonfood/', views.pokemonfood_index, name='pokemonfood-index'),
    path('pokemonfood/<int:pokemonfood_id>', views.pokemonfood_show, name='pokemonfood-show'),
    path('pokemonfood/create/', views.PokemonFoodCreate.as_view(), name='pokemonfood-create'),
    path('pokemonfood/<int:pk>/update/', views.PokemonFoodUpdate.as_view(), name='pokemonfood-update'),
    path('pokemonfood/<int:pk>/delete/', views.PokemonFoodDelete.as_view(), name='pokemonfood-delete'),
]