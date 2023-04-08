from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

recipes = {
    'recipes': [x for x in DATA.keys()]
}


def recipes_list_view(request):
    context = recipes
    return render(request, 'calculator/recipes.html', context)


def recipe_view(request):
    recipe_name: str = request.path.replace('/','')
    servings = int(request.GET.get('servings',1))
    for recipe, ing in DATA.items():
        if recipe == recipe_name:
            if servings:
                for ing_name, ing_sum in ing.items():
                        ing[ing_name] = ing_sum * servings
                context = {'recipe': ing, 'title': recipe_name}
                return render(request, 'calculator/index.html', context) 

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
