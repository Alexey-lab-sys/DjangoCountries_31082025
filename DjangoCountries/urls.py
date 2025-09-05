from django.contrib import admin
from django.urls import path
from countries import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Главная страница
    path('countries-list/', views.country_list, name='country_list'),  # Страница со списком стран
    path('country/<str:country_name>/', views.country_detail, name='country_detail'),  # Персональная страница страны
    path('countries/<str:letter>/', views.countries_by_letter, name='countries_by_letter'),  # Страница по первой букве
    path('languages/', views.language_list, name='language_list'),  # Страница со списком языков
    path('language/<str:language_name>/', views.countries_by_language, name='countries_by_language'),  # Страница по языку
]
