
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.models import User

from .models import Pokemon, PokemonFood

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class PokemonList(TemplateView):
    template_name = "pokemonlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["pokemons"] = Pokemon.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["pokemons"] = Pokemon.objects.all()
            context["header"] = "All Pokemon"
        return context

class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    template_name = "pokemon-create.html"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/pokemon')

class PokemonDetail(DetailView):
    model = Pokemon
    template_name = "pokemon-detail.html"

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['name', 'species', 'img', 'level', 'gender', 'pokemonfood']
    template_name = "pokemon-update.html"
    def get_success_url(self):
        return reverse('pokemon-detail', kwargs={'pk': self.object.pk})

class PokemonDelete(DeleteView):
    model = Pokemon
    template_name = "pokemon-delete-confirm.html"
    success_url = "/pokemon/"

def profile(request, username):
    user = User.objects.get(username=username)
    pokemon = Pokemon.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'pokemon': pokemon})

def pokemonfood_index(request):
    pokemonfood = PokemonFood.objects.all()
    return render(request, 'pokemonfood-index.html', {'pokemonfoods': pokemonfood})

def pokemonfood_show(request, pokemonfood_id):
    pokemonfood = PokemonFood.objects.get(id=pokemonfood_id)
    return render(request, 'pokemonfood-show.html', {'pokemonfood': pokemonfood})

class PokemonFoodCreate(CreateView):
    model = PokemonFood
    fields = '__all__'
    template_name = "pokemonfood-form.html"
    success_url = '/pokemonfood'

class PokemonFoodUpdate(UpdateView):
    model = PokemonFood
    fields = ['name']
    template_name = "pokemonfood-update.html"
    success_url = '/pokemonfood'

class PokemonFoodDelete(DeleteView):
    model = PokemonFood
    template_name = "pokemonfood-confirm-delete.html"
    success_url = '/pokemonfood'