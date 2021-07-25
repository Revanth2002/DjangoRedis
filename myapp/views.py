from django.shortcuts import render
from django.http import HttpResponse

from .task import my_first_task,adding_task

# Create your views here.
from .models import Recipe

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

CACHE_TTL = getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)

def get_recipe(filter_recipe = None):
    if filter_recipe:
        print("Data coming from DB")
        recipes = Recipe.objects.filter(name__contains = filter_recipe)
    else:
        recipes = Recipe.objects.all()
    return recipes

def home(request):
    filter_recipe = request.GET.get('recipe')
    if cache.get(filter_recipe):
        print("Data Coming from CACHE")
        recipe = cache.get(filter_recipe)
    else:        
        if filter_recipe:
            recipe = get_recipe(filter_recipe)
            cache.set(filter_recipe,recipe)
        else:
            recipe = get_recipe() 
    context = {'recipe':recipe}
    return render(request,'home.html',context)

def show(request,id):
    if cache.get(id):
        print("Data from DB")
        recipe = cache.get(id)
    else:
        print("Data from Cache")
        recipe = Recipe.objects.get(id = id)
        cache.set(id,recipe)
    context = {'recipe':recipe}
    return render(request,'show.html',context)

def task(request):
    my_first_task.delay(10)
    print("----")
    adding_task.delay(10,20)
    return HttpResponse('response done')
