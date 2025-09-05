import json
from countries.models import Country
from django.core.management import execute_from_command_line
import sys


sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoCountries.settings')
import django
django.setup()

with open('country-by-languages.json') as f:
    data = json.load(f)
    for item in data:
        Country.objects.create(name=item['country'], languages=item['languages'])
