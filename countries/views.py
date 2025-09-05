import json
from django.shortcuts import render
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def country_list(request):
    with open('country-by-languages.json', 'r', encoding='utf-8') as file:
        countries_data = json.load(file)

    countries = [(country['country'], country['languages']) for country in countries_data]
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Пагинация
    paginator = Paginator(countries, 10)  # 10 стран на странице
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-запроса
    page_obj = paginator.get_page(page_number)

    return render(request, 'country_list.html', {'page_obj': page_obj, 'alphabet': alphabet})

def countries_by_letter(request, letter):
    with open('country-by-languages.json', 'r', encoding='utf-8') as file:
        countries_data = json.load(file)

    filtered_countries = [country for country in countries_data if country['country'].startswith(letter)]

    return render(request, 'countries_by_letter.html', {'countries': filtered_countries, 'letter': letter})

def country_detail(request, country_name):
    with open('country-by-languages.json', 'r', encoding='utf-8') as file:
        countries_data = json.load(file)

    country_info = next((country for country in countries_data if country['country'] == country_name), None)

    return render(request, 'country_detail.html', {'country': country_info})

def language_list(request):
    with open('country-by-languages.json', 'r', encoding='utf-8') as file:
        countries_data = json.load(file)

    languages = set()
    for country in countries_data:
        languages.update(country['languages'])

    return render(request, 'language_list.html', {'languages': sorted(languages)})

def countries_by_language(request, language_name):
    with open('country-by-languages.json', 'r', encoding='utf-8') as file:
        countries_data = json.load(file)

    # Фильтрация стран по языку
    filtered_countries = [country for country in countries_data if language_name in country['languages']]

    return render(request, 'countries_by_language.html', {'countries': filtered_countries, 'language': language_name})
